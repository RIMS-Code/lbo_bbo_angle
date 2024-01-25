# Pytests for calculation

from hypothesis import given, strategies as st
import numpy as np
import pytest

from lbo_bbo_angle import calc

# create number between 940 and 950 with hypothesis


def test_second_harmonic_lbo():
    """Test second harmonic generation in LBO."""
    wavelength = 800
    angle, walkoff = calc.second_harmonic_lbo(wavelength)

    assert angle == pytest.approx(31.6)
    assert walkoff == pytest.approx(16.48)


def test_third_harmonic_bbo():
    """Test third harmonic generation in BBO."""
    wavelength = 700
    angle, walkoff = calc.third_harmonic_bbo(wavelength)

    assert angle == pytest.approx(53.3)
    assert walkoff == pytest.approx(85.81)


@given(calc_x=st.floats(min_value=940, max_value=950))
def test_calculate(calc_x):
    """Test interpolation with a simple dataset."""
    data = np.array([[940, 950], [10, 20], [100, 200]]).transpose()
    exp_values = []
    for idx in range(2):
        slope = (data[1][idx + 1] - data[0][idx + 1]) / (data[1][0] - data[0][0])
        intercept = data[1][idx + 1] - slope * data[1][0]
        exp_values.append(calc_x * slope + intercept)

    assert pytest.approx(calc._calculation(calc_x, data)) == exp_values


def test_calculate_spot_on():
    """Test interpolation with a simple dataset."""
    data = np.array([[940, 950], [10, 20], [100, 200]]).transpose()
    calc_x = 950

    assert calc._calculation(calc_x, data) == (20, 200)
