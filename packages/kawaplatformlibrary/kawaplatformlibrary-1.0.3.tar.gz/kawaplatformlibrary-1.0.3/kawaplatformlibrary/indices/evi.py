"""
Calculation of Enhanced Vegetation Index[EVI] using the NIR, Red and Blue bands

Formula : 2.5 * ((NIR - RED) / (NIR + 6*RED - 7.5*BLUE + 1))
Wavelengths : NIR, Red and Blue
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

def calculate(band_blue, band_red, band_nir, ground_sampling_distance):
    """
    Function for calculating the CIGreen
    
    Input Parameters:
        1. band_nir  => NIR band of the satellite image
        2. band_red  => Red band of the satellite image
        3. band_blue => Blue band of the satellite image

    Output Parameters:
        1. evi => EVI for the entire satellite image
    """

    if band_nir.transform[0] != ground_sampling_distace:
        band_nir_array = reSampleBand(band_nir, ground_sampling_distance)
    else:
        band_nir_array = np.array(band_nir,read(1), dtype=np.float32)

    if band_red.transform[0] != ground_sampling_distance:
        band_red_array = reSampleBand(band_red, ground_sampling_distance)
    else:
        band_red_array = np.array(band_red.read(1), dtype=np.float32)

    if band_blue.transform[0] != ground_sampling_distance:
        band_blue_array = reSampleBand(band_blue, ground_sampling_distance)
    else:
        band_blue_array = np.array(band_blue.read(1), dtype=np.float32)
    
    evi = 2.5 * ((band_nir_array - band_red_array) / (band_nir_array + 6*band_red_array - 7.5*band_blue_array + 1))

    return np.array(evi, dtype=np.float32)
    pass
