'''
    Utility functions for tart2ms
    Author: Tim Molteno, tim@elec.ac.nz
    Copyright (c) 2019-2022.

    License. GPLv3.
'''

import logging

import numpy as np

from astropy import constants

LOGGER = logging.getLogger("tart2ms")
LOGGER.setLevel(logging.INFO)


def rayleigh_criterion(max_freq, baseline_lengths):
    '''
        The accepted criterion for determining the diffraction limit to resolution
        developed by Lord Rayleigh in the 19th century.

        approx resolution given by first order Bessel functions
        assuming array is a flat disk of length max_baseline
    '''
    min_wl = constants.c.value / max_freq
    max_baseline = np.max(baseline_lengths)
    min_baseline = np.min(baseline_lengths)

    LOGGER.info("Baseline lengths:")
    LOGGER.info(f"\tMinimum: {min_baseline:.4f} m")
    LOGGER.info(
        f"\tMaximum: {max_baseline:.4f} m --- {max_baseline/min_wl:.4f} wavelengths")
    return np.degrees(1.220 * min_wl / max_baseline)


def resolution_min_baseline(max_freq, resolution_deg):
    '''
        Return the minimum baseline to achieve an angular resolution

        solve res_rad = 1.220 * min_wl / max_baseline to get

        max_baseline = 1.220 * min_wl / res_rad
    '''
    min_wl = constants.c.value / max_freq
    res_rad = np.radians(resolution_deg)

    return 1.220 * min_wl / res_rad
