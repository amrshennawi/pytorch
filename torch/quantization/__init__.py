from .quantize import *  # noqa: F403
from torch.ao.quantization.observer import *  # noqa: F403
from torch.ao.quantization.qconfig import *  # noqa: F403
from .fake_quantize import *  # noqa: F403
from .fuse_modules import fuse_modules
from .stubs import *  # noqa: F403
from .quant_type import *  # noqa: F403
from .quantize_jit import *  # noqa: F403
# from .quantize_fx import *
from .quantization_mappings import *  # noqa: F403
from .fuser_method_mappings import *  # noqa: F403

def default_eval_fn(model, calib_data):
    r"""
    Default evaluation function takes a torch.utils.data.Dataset or a list of
    input Tensors and run the model on the dataset
    """
    for data, target in calib_data:
        model(data)

# TODO(future PR): fix the typo, should be `__all__`
_all__ = [
    'QuantWrapper', 'QuantStub', 'DeQuantStub',
    # Top level API for eager mode quantization
    'quantize', 'quantize_dynamic', 'quantize_qat',
    'prepare', 'convert', 'prepare_qat',
    # Top level API for graph mode quantization on TorchScript
    'quantize_jit', 'quantize_dynamic_jit',
    # Top level API for graph mode quantization on GraphModule(torch.fx)
    # 'fuse_fx', 'quantize_fx',  # TODO: add quantize_dynamic_fx
    # 'prepare_fx', 'prepare_dynamic_fx', 'convert_fx',
    'QuantType', 'quant_type_to_str',  # quantization type
    # custom module APIs
    'get_default_static_quant_module_mappings', 'get_static_quant_module_class',
    'get_default_dynamic_quant_module_mappings',
    'get_default_qat_module_mappings',
    'get_default_qconfig_propagation_list',
    'get_default_compare_output_module_list',
    'get_quantized_operator',
    'get_fuser_method',
    # Sub functions for `prepare` and `swap_module`
    'propagate_qconfig_', 'add_quant_dequant', 'add_observer_', 'swap_module',
    'default_eval_fn', 'get_observer_dict',
    'register_activation_post_process_hook',
    # Observers
    'ObserverBase', 'WeightObserver', 'HistogramObserver',
    'observer', 'default_observer',
    'default_weight_observer', 'default_placeholder_observer',
    'default_per_channel_weight_observer',
    # FakeQuantize (for qat)
    'default_fake_quant', 'default_weight_fake_quant',
    'default_symmetric_fixed_qparams_fake_quant',
    'default_affine_fixed_qparams_fake_quant',
    'default_per_channel_weight_fake_quant',
    'default_histogram_fake_quant',
    # QConfig
    'QConfig', 'default_qconfig', 'default_dynamic_qconfig', 'float16_dynamic_qconfig',
    'float_qparams_weight_only_qconfig',
    # QAT utilities
    'default_qat_qconfig', 'prepare_qat', 'quantize_qat',
    # module transformations
    'fuse_modules',
]
