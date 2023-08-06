from .core import (BackendType, Padding, PoolType, LayerType, HwVersion, NP,
                   MeshMapper, Model, Layer, AkidaUnsupervised, Device,
                   HardwareDevice, devices, NSoC_v1, NSoC_v2, Latest,
                   TwoNodesIP_v1, AKD500_v1, PowerMeter, PowerEvent, Sequence,
                   Pass, soc, LayerParams, Optimizer, __version__,
                   get_program_memory_infos, nn)

from .layer import *
from .input_data import InputData
from .fully_connected import FullyConnected
from .convolutional import Convolutional
from .separable_convolutional import SeparableConvolutional
from .input_convolutional import InputConvolutional
from .add import Add
from .dense2d import Dense2D
from .shiftmax import Shiftmax
from .attention import Attention
from .stem import Stem
from .model import *
from .statistics import Statistics
from .sparsity import evaluate_sparsity
from .np import *
from .sequence import *
from .virtual_devices import *

Model.__str__ = model_str
Model.__repr__ = model_repr
Model.statistics = statistics
Model.summary = summary
Model.predict_classes = predict_classes

Layer.__str__ = layer_str
Layer.__repr__ = layer_repr
Layer.set_variable = set_variable
Layer.get_variable = get_variable
Layer.get_variable_names = get_variable_names
Layer.get_learning_histogram = get_learning_histogram

Sequence.__repr__ = sequence_repr
Pass.__repr__ = pass_repr

NP.Info.__repr__ = np_info_repr
NP.Mesh.__repr__ = np_mesh_repr
NP.Mapping.__repr__ = np_mapping_repr
