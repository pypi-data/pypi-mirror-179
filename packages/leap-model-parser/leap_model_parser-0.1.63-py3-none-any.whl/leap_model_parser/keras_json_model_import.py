import copy
from dataclasses import dataclass
import json
from collections import defaultdict
from pathlib import Path
import string
from typing import Set, Dict, Any, List, Type, Optional

import numpy as np
import tensorflow as tf  # type: ignore
from keras.engine.keras_tensor import KerasTensor
from tensorflow.python.keras.utils.generic_utils import func_load  # type: ignore

from leap_model_parser.contract.importmodelresponse import DatasetInfo, NodeResponse, WrapperData

layer_attributes_adaptation = {'bias_initializer', 'kernel_initializer'}


class KerasJsonModelImport:
    def __init__(self, custom_layers: Optional[Dict[str, Type[tf.keras.layers.Layer]]] = None,
                 dataset_info: Optional[DatasetInfo] = None) -> None:
        self.id = 1
        self.nodes_cache: Dict[str, NodeResponse] = defaultdict()
        self.layer_name_to_layer: Dict[str, Dict] = defaultdict()
        self.visited_connections: Set[str] = set()
        self.ui_components: Dict[str, Dict] = defaultdict()
        self.dataset_info = dataset_info

        if custom_layers is None:
            custom_layers = {}
        self.custom_layers = custom_layers

    def prepare_model_to_import(self, model_schema) -> None:
        ui_components_file_path = Path(__file__).parent / 'contract' / 'ui_components.json'
        with open(str(ui_components_file_path), 'r') as f:
            ui_component_json = json.load(f)

        for layer in model_schema['config']['layers']:
            layer['is_representation_block'] = KerasJsonModelImport.is_representation_block(layer)
            self.layer_name_to_layer[layer['name']] = layer

        self.ui_components = {layer['name']: layer for layer in ui_component_json}

    @staticmethod
    def is_representation_block(layer: Dict[str, Any]) -> bool:
        return len(layer['inbound_nodes']) > 1

    def generate_graph(self, model_schema: Dict, layer_name_to_inbound_nodes: Dict[str, List]) -> Dict[str, NodeResponse]:
        self.prepare_model_to_import(model_schema)
        for graph_output_layer in model_schema['config']['output_layers']:
            current_layer = self.layer_name_to_layer[graph_output_layer[0]]
            self.generate_graph_recursive(current_layer, graph_output_layer[1], layer_name_to_inbound_nodes)

        nodes = {node.id: node for node in self.nodes_cache.values()}
        _add_origin_name_to_nodes(nodes)
        return nodes

    '''
    Convert tf ops inbound nodes to the same format as the regular layers, while removing _CONSTANT_VALUE.
    examples:
    1.
        ['conv2d_2', 0, 0, {'slice_spec': [{'start': None, 'stop': None, 'step': None}]}
        will be converted to:
        [['conv2d_2', 0, 0]]
    2.
        ['tf.__operators__.getitem_1', 0, 0, {'y': ['tf.__operators__.getitem_1', 0, 0]}]
        will be converted to:
        [['tf.__operators__.getitem_1', 0, 0], ['tf.__operators__.getitem_1', 0, 0]]
    3.
        ['_CONSTANT_VALUE', -1, 1.0, {'y': ['tf.__operators__.add_2', 0, 0], 'name': None}]
        will be converted to:
        [['tf.__operators__.add_2', 0, 0]]
    '''

    @staticmethod
    def prepare_inbound_nodes(inbound_nodes_to_enumerate: List):
        inbound_nodes_to_enumerate_prepared = []
        single_inbound_node_to_enumerate = []
        for element in inbound_nodes_to_enumerate:
            if type(element) in (int, str):
                single_inbound_node_to_enumerate.append(element)
            elif isinstance(element, dict):
                if single_inbound_node_to_enumerate and type(single_inbound_node_to_enumerate[0]) == str and \
                        single_inbound_node_to_enumerate[0] != '_CONSTANT_VALUE':
                    inbound_nodes_to_enumerate_prepared.append(single_inbound_node_to_enumerate)
                single_inbound_node_to_enumerate = []
                for inbound_nodes in element.values():
                    if isinstance(inbound_nodes, list):
                        inbound_nodes_to_enumerate_prepared.extend(
                            KerasJsonModelImport.prepare_inbound_nodes(inbound_nodes))
        if single_inbound_node_to_enumerate and type(single_inbound_node_to_enumerate[0]) == str:
            inbound_nodes_to_enumerate_prepared.append(single_inbound_node_to_enumerate)

        return inbound_nodes_to_enumerate_prepared

    def generate_graph_recursive(self, current_layer: Dict[str, Any], instance_index: int, layer_name_to_inbound_nodes):
        self.generate_node(current_layer, instance_index, layer_name_to_inbound_nodes)

        inbound_nodes = current_layer['inbound_nodes']
        if len(inbound_nodes) == 0:
            return
        inbound_nodes_to_enumerate = inbound_nodes[instance_index]
        if isinstance(inbound_nodes_to_enumerate, dict):
            inbound_nodes_to_enumerate = list(inbound_nodes_to_enumerate.values())
        if isinstance(inbound_nodes_to_enumerate[0], list):
            inbound_nodes_to_enumerate_prepared = []
            for inbound_node in inbound_nodes_to_enumerate:
                inbound_nodes_to_enumerate_prepared.extend(self.prepare_inbound_nodes(inbound_node))
        else:
            inbound_nodes_to_enumerate_prepared = self.prepare_inbound_nodes(inbound_nodes_to_enumerate)

        for input_index, input_layer_item in enumerate(inbound_nodes_to_enumerate_prepared):
            input_layer = self.layer_name_to_layer[input_layer_item[0]]
            self.generate_node(input_layer, input_layer_item[1], layer_name_to_inbound_nodes)

            input_node_name = f"{input_layer['name']}_{input_layer_item[1]}"
            current_node_name = f"{current_layer['name']}_{instance_index}"
            connection_name = f"{input_node_name}_{current_node_name}_{input_index}"
            if connection_name in self.visited_connections:
                continue

            self.visited_connections.add(connection_name)
            self.attach(input_layer, input_node_name, current_node_name, input_index)
            self.generate_graph_recursive(current_layer=input_layer, instance_index=input_layer_item[1],
                                          layer_name_to_inbound_nodes=layer_name_to_inbound_nodes)

    def attach(self, input_layer: Dict, node_input_layer_name: str, node_output_layer_name: str, input_index: int):
        node_output_layer = self.nodes_cache[node_output_layer_name]
        if input_layer['class_name'] == 'InputLayer':
            if node_output_layer.name == 'Lambda':
                return
            node_input_layer_name = 'Dataset'

        node_input_layer = self.nodes_cache[node_input_layer_name]
        node_output_key = self.get_connection_key(input_layer, node_input_layer, 'outputs', input_index)
        node_input_key = self.get_connection_key(input_layer, node_output_layer, 'inputs', input_index)
        if node_output_key is None or node_input_key is None:
            return

        if node_output_key not in node_input_layer.outputs:
            node_input_layer.outputs[node_output_key] = {'connections': []}
        node_input_layer.outputs[node_output_key]['connections'].append({
            "node": node_output_layer.id,
            "input": node_input_key
        })

        if node_input_key not in node_output_layer.inputs:
            node_output_layer.inputs[node_input_key] = {'connections': []}
        node_output_layer.inputs[node_input_key]['connections'].append({
            "node": node_input_layer.id,
            "output": node_output_key
        })

    def _get_layer_metadata(self, layer_json: Dict) -> Optional[Dict]:
        layer_metadata = self.ui_components.get(layer_json['class_name'])
        if layer_metadata is None:
            if layer_json['class_name'] in self.custom_layers:
                layer_metadata = {
                    'type': 'CustomLayer',
                    'class_name': 'CustomLayer',
                    'selected': layer_json['class_name']
                }
        return layer_metadata

    def generate_node(self, layer: Dict[str, Any], instance_index: int, layer_name_to_inbound_nodes):
        if layer['class_name'] == 'InputLayer':
            self.handle_input_layer(layer)
            return

        node_key = f"{layer['name']}_{instance_index}"
        if node_key in self.nodes_cache:
            return

        layer = self.handle_cudnn(layer)
        layer_metadata = self._get_layer_metadata(layer)
        if layer_metadata is None:
            raise Exception(f"{layer['class_name']} layer is not supported, please try to contact Tensorleap support")

        if layer_metadata['type'] == 'wrapper':
            wrapped_layer = self.handle_wrapper_layer(layer)
            self.generate_node(wrapped_layer, instance_index, layer_name_to_inbound_nodes)
            return

        if layer['is_representation_block']:
            self.generate_rp_node(layer, layer_metadata, node_key)
        else:
            self.generate_regular_node(layer, layer_metadata, node_key, layer_name_to_inbound_nodes)
        self.id += 1

    def bbb(self, arg):
        if isinstance(arg, KerasTensor):
            return arg.name
        if isinstance(arg, tf.Tensor):
            return arg.numpy()
        if isinstance(arg, (str, float, int, bool, np.ndarray, type(None))):
            return arg
        if isinstance(arg, list):
            return [self.bbb(a) for a in arg]
        if isinstance(arg, dict):
            return {k: self.bbb(v) for k, v in arg.items()}
        else:
            x = 1

    def _serialize_call_args(self, call_args, call_kwargs):
        serialized_call_args = []
        for arg in call_args:
            serialized_call_args.append(self.bbb(arg))

        serialized_call_kwargs = {}
        for k, v in call_kwargs.items():
            serialized_call_kwargs[k] = self.bbb(v)

        return serialized_call_args, serialized_call_kwargs

    def generate_regular_node(self, layer: Dict[str, Any], layer_metadata: Dict[str, Any], node_key: str, layer_name_to_inbound_nodes):
        data = layer['config']
        if layer['class_name'] in ('TFOpLambda', 'SlicingOpLambda') or layer['class_name'] in self.custom_layers:
            call_args = layer_name_to_inbound_nodes[layer['config']['name']][0].call_args
            call_kwargs = layer_name_to_inbound_nodes[layer['config']['name']][0].call_kwargs
            serialized_call_args, serialized_call_kwargs = self._serialize_call_args(call_args, call_kwargs)
            data['call_args'] = {'serialized_call_args': serialized_call_args,
                                 'serialized_call_kwargs': serialized_call_kwargs}
            # data['inbound_nodes'] = layer['inbound_nodes'][0]
        elif layer['class_name'] == "Lambda":
            lambda_func = func_load(layer['config']['function'])
            data['arg_names'] = list(lambda_func.__code__.co_varnames)

        self.layer_data_adjustments(data, layer_metadata)
        node = NodeResponse(id=str(self.id), name=layer_metadata.get("class_name", layer["class_name"]), data=data)
        if 'wrapper' in layer:
            node.wrapper = layer['wrapper']
        self.nodes_cache[node_key] = node

    @classmethod
    def handle_wrapper_layer(cls, layer):
        wrapped_layer = layer['config']['layer']
        wrapped_layer['name'] = layer['name']
        wrapped_layer['is_representation_block'] = layer['is_representation_block']
        wrapper_data = layer['config'].copy()
        wrapper_data.pop('layer')
        wrapper_data.pop('name')
        # TODO: remove this hard coded condition after support
        if 'merge_mode' in wrapper_data and wrapper_data.get('merge_mode') is None:
            raise Exception(f"{layer['class_name']} layer with merge_mode None is not supported,"
                            f" please try to contact Tensorleap support")
        wrapped_layer['wrapper'] = WrapperData(layer['class_name'], wrapper_data)
        return wrapped_layer

    @classmethod
    def layer_data_adjustments(cls, layer_config: Dict[str, Any], layer_metadata: Dict[str, Any]) -> None:
        for layer_attribute in layer_attributes_adaptation:
            if layer_attribute in layer_config:
                layer_config[layer_attribute] = layer_config[layer_attribute]['class_name']

        layer_config["type"] = layer_metadata.get('type')
        if 'selected' in layer_metadata:
            layer_config["selected"] = layer_metadata['selected']
        # TODO: remove this hard coded condition after support
        if layer_config.get('return_state'):
            raise Exception(f"{layer_metadata.get('name')} layer with return_state True is not supported,"
                            f" please try to contact Tensorleap support")

    def generate_rp_node(self, layer: Dict[str, Any], layer_metadata: Dict[str, Any], node_key: str) -> None:
        if layer['name'] not in self.nodes_cache:
            data = layer['config']
            self.layer_data_adjustments(data, layer_metadata)
            data["output_blocks"] = []
            node = NodeResponse(id=str(self.id), name=layer["class_name"], data=data)
            if 'wrapper' in layer:
                node.wrapper = layer['wrapper']
            self.nodes_cache[layer['name']] = node

            self.id += 1
        data = {
            "output_name": "Action",
            "node_id": self.nodes_cache[layer["name"]].id,
            "parent_name": layer["class_name"]
        }
        self.nodes_cache[node_key] = NodeResponse(id=str(self.id), name='Representation Block', data=data)
        self.nodes_cache[layer["name"]].data["output_blocks"].append({
            "block_node_id": self.nodes_cache[node_key].id,
            "output_name": "Action"
        })

    def get_connection_key(self, node_input_layer, node: NodeResponse, direction: str, index: int) -> Optional[str]:
        layer_metadata = self.ui_components.get(node.name)
        if _is_represntaion_block_node(node) or layer_metadata is None:
            if direction == 'inputs':
                connection_format = f"{node.id}-input"
            else:
                connection_format = f"{node.id}-feature_map"
        elif _is_dataset_node(node):
            inputs = _get_dataset_inputs_from_dataset_node(node)
            has_dataset_but_no_input_is_match = self.dataset_info is not None and not any(
                input_data['name'] == node_input_layer['name'] for input_data in inputs)
            if has_dataset_but_no_input_is_match:
                return None
            connection_format = f"{node.id}-{node_input_layer['name']}"
        else:
            try:
                connection_format = layer_metadata[f"{direction}_data"][direction][index]['name']
            except IndexError:
                connection_format = layer_metadata[f"{direction}_data"][direction][0]['name']
            if connection_format.count('${id}') > 0:
                connection_format = f"{node.id}-{index}"
                if 'custom_input_keys' not in node.data:
                    node.data['custom_input_keys'] = []
                node.data['custom_input_keys'].append(connection_format)
            else:
                connection_format = f"{node.id}-{connection_format}"
        return connection_format

    def handle_cudnn(self, layer: Dict[str, Any]) -> Dict[str, Any]:
        if layer['class_name'] == 'CuDNNGRU':
            layer['class_name'] = 'GRU'
            gru_metadata = self.ui_components['GRU']
            gru_config = {}
            for gru_prop in gru_metadata["properties"]:
                if gru_prop["name"] in layer['config']:
                    gru_config[gru_prop["name"]] = layer['config'][gru_prop["name"]]
                elif gru_prop["isdefault"]:
                    gru_config[gru_prop["name"]] = gru_prop["default_val"]

            gru_config["name"] = layer['config']["name"]
            gru_config["trainable"] = layer['config']["trainable"]

            layer['config'] = gru_config
        return layer

    def get_and_add_dataset_node_if_not_existed(self) -> NodeResponse:
        datasetNode = self.nodes_cache.get('Dataset')
        if datasetNode is None:
            dataset_copy = copy.deepcopy(DATASET_DATA)
            datasetNode = NodeResponse(
                id=str(self.id), name='Dataset', data=dataset_copy)
            if self.dataset_info is not None:
                datasetNode.data['datasetVersion'] = self.dataset_info.dataset_version
                datasetNode.data['selected_dataset'] = self.dataset_info.name
            self.nodes_cache['Dataset'] = datasetNode
            self.id += 1
        return datasetNode

    def handle_input_layer(self, layer: Dict[str, Any]):
        datasetNode = self.get_and_add_dataset_node_if_not_existed()
        if self.dataset_info is None:
            self.handle_input_layer_without_dataset(layer, datasetNode)

    def handle_input_layer_without_dataset(self, layer: Dict[str, Any], datasetNode: NodeResponse):
        inputs = datasetNode.data['datasetVersion']['metadata']['setup']['inputs']

        if not any(input_data['name'] == layer['name'] for input_data in inputs):
            shape = layer['config']['batch_input_shape']
            input_data = {'name': layer['name'], 'shape': shape[1:]}
            inputs.append(input_data)


def _add_origin_name_to_nodes(nodes: Dict[str, NodeResponse]):
    for node in nodes.values():
        if "name" in node.data:
            node.data["origin_name"] = node.data["name"]
            node.data.pop("name")


def _is_dataset_node(node: NodeResponse) -> bool:
    return node.name == 'Dataset'


def _is_represntaion_block_node(node: NodeResponse) -> bool:
    return node.name == 'Representation Block'


def _get_dataset_inputs_from_dataset_node(node: NodeResponse):
    return node.data['datasetVersion']['metadata']['setup']['inputs']


DATASET_DATA = {'datasetVersion': {'metadata': {'setup': {'preprocess': {'training_length': 0, 'validation_length': 0},
                                                          'inputs': [], 'metadata': [], 'outputs': [],
                                                          'visualizers': [], 'prediction_types': [],
                                                          'custom_loss_names': []}}},
                'type': 'dataset'}
