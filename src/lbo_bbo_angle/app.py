"""Streamlit app for LBO-BBO angle calculation."""

import streamlit as st

from .calc import second_harmonic_lbo, third_harmonic_bbo

st.title("Crystal calculations for second and third harmonic generation")

# Add a descritpiton
st.markdown(
    """
    This app calculates the angle and walk-off of the beam in a crystal for second
    or third harmonic generation.
    The crystals currently included are:
    - LBO for second harmonic generation
    - BBO for third harmonic generation
    """
)

# Entry field for wavelength
wavelength = st.number_input(
    "Wavelength (nm)",
    min_value=700,
    max_value=1000,
    value=800,
    step=10,
)

# Radio buttons for harmonic generation
harmonic = st.radio(
    "Harmonic generation",
    options=["Second", "Third"],
)

# A results field
results = st.empty()

# Button to run calculation
if st.button("Calculate"):
    if harmonic == "Second":
        angle, walkoff = second_harmonic_lbo(wavelength)
        xtal = "LBO"
        harm = 2
    elif harmonic == "Third":
        angle, walkoff = third_harmonic_bbo(wavelength)
        xtal = "BBO"
        harm = 3

    results.markdown(
        f"""**Results {harmonic} Harmonic Generation**:

| Parameter | Value |
| --- | --- |
| 1HG wavelength | {wavelength:.1f} nm |
| {harm}HG wavelength | {wavelength / harm:.1f} nm |
| Crystal | {xtal} |
| Angle | {angle:.2f} deg |
| Walk-off | {walkoff:.2f} mrad |"""
    )

print(results)
