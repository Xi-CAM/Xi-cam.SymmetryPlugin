"""Simple example operations that are used to demonstrate some image processing in Xi-CAM.
"""
import numpy as np
from xicam.plugins.operationplugin import (limits, describe_input, describe_output,
                                           operation, opts, output_names, visible)
# TODO remove dependency
from ttictoc import tic, toc

from .colorwheel import create_sym, fake_create_sym


# Define an operation that applies Symmetry to an image
@operation
@output_names("output_image")
@describe_input("image", "Create Orientation Map")
@describe_input("symmetry", "The factor of noise to add to the image")
@limits("order", [1.0, 10.0])
@opts("order", step=1.0)
@visible("image", is_visible=False)
def symmetry(image: np.ndarray, order: float = 2) -> np.ndarray:
    if issubclass(image.dtype.type, np.integer):
        max_value = np.iinfo(image.dtype).max
    else:
        max_value = np.finfo(image.dtype).max
    tic()
    # using fake image for now
    whl, rgb2 = fake_create_sym(image, order)
    #whl, rgb2 = create_sym(image,order)
    print(toc())
    #clrwhl , rgb = create_sym(img, order)
    #print(img.shape)
    return rgb2
