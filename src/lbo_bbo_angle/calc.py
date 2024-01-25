"""Calculate the angles and walkoff for second and third harmonic generation.

Allowed wavelengths: 700-1000 nm

Data will be read from `data.py` numpy arrays. The data is linearly
between the closest wavelengths.
"""

import numpy as np

from lbo_bbo_angle.data import SECOND_HARMONIC_LBO, THIRD_HARMONIC_BBO


def second_harmonic_lbo(wavelength: float) -> tuple[float, float]:
    """Calculate the angle and walk-off for second harmonic generation in LBO.

    :param wavelength: Wavelength of beam in nm.

    :returns: Tuple of angle and walk-off in degrees and mrad respectively.
    """
    return _calculation(wavelength, SECOND_HARMONIC_LBO)


def third_harmonic_bbo(wavelength: float) -> tuple[float, float]:
    """Calculate the angle and walk-off for third harmonic generation in BBO.

    :param wavelength: Wavelength of beam in nm.

    :returns: Tuple of angle and walk-off in degrees and mrad respectively.
    """
    return _calculation(wavelength, THIRD_HARMONIC_BBO)


def _calculation(wavelength: float, data: np.ndarray) -> tuple[float, float]:
    """Calculate the angle and walk-off for second harmonic generation in LBO.

    :param wavelength: Wavelength of beam in nm.
    :param data: Data to interpolate from. The columns of the array are
        wavelength, angle and walk-off respectively. The closest two wavelengths
        to the input wavelength will be used for interpolation.

    :returns: Tuple of angle and walk-off in degrees and mrad respectively.
    """
    # If we have a match:
    if wavelength in data[:, 0]:
        idx = np.where(data[:, 0] == wavelength)[0]
        return float(data[idx, 1][0]), float(data[idx, 2][0])

    # Find the closest two wavelengths
    idx = np.argsort(np.abs(data[:, 0] - wavelength))[:2]
    idx = np.sort(idx)

    # Interpolate the angle and walk-off
    angle = np.interp(wavelength, data[idx, 0], data[idx, 1])
    walkoff = np.interp(wavelength, data[idx, 0], data[idx, 2])
    return float(angle), float(walkoff)
