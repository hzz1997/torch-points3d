import sys
from .networks import *
from .res16unet import *

_custom_models = sys.modules[__name__]


def initialize_minkowski_unet(
    model_name, in_channels, out_channels, D, conv1_kernel_size=3, dilations=[1, 1, 1, 1], **kwargs
):
    net_cls = getattr(_custom_models, model_name)
    return net_cls(in_channels=in_channels, out_channels=out_channels, D=D)
