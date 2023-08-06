"""
Calculation of Enhanced Vegetation Index 2 using Near-Infrared and Red bands

Formula: 2.4 * ((NIR - RED) / (NIR + RED + 1))

Wavelengths: 640nm :760nm , 780nm :1400nm
"""

import numpy as np
import pandas as pd
import rasterio, os

from kawaplatformlibrary.postprocessing.mosiac import reSampleBand

def store():
    """
    This will be done when we have decided on the data storage strategy.
    """
    pass

def calculate(band_red, band_nir, ground_sampling_distance):
    """
    Function for calculating the EVI
    
    Input Parameters:
        1. band_nir => NIR band of the satellite image
        2. band_red => Red band of the satellite image

    Output Parameters:
        1. evi_two => EVI 2 for the entire satellite image
    """

    if band_nir.transform[0] != ground_sampling_distance:
        band_nir_array = reSampleBand(band_nir, ground_sampling_distance)
    else:
        band_nir_array = np.array(band_nir.read(1), dtype=np.float32)

    if band_red.transform[0] != ground_sampling_distance:
        band_red_array = reSampleBand(band_red, ground_sampling_distance)
    else:
        band_red_array = np.array(band_red.read(1), dtype=np.float32)

    evi_two = 2.4 * ((band_nir_array - band_red_array)/(band_nir_array + band_red_array + 1))

    return np.array(evi_two, dtype=np.float32)
    pass
