"""Standardized CubeSat and PocketQube form factor data.

Sources
-------
- CubeSat Design Specification (CDS) Rev 14.1, Cal Poly, 2022
  https://www.cubesat.org/cubesatinfo
  https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/
  t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf
- PocketQube Standard Issue 1, 2018
  https://static1.squarespace.com/static/53d7dcdce4b07a1cdbbc08a4/
  t/5b34c395352f5303fcec6f45/1530184648111/PocketQube+Standard+issue+1+-+Published.pdf

Height values for CubeSat use the *maximum structural envelope* along the
deployment (Z) axis as defined in CDS Rev 14.1 Table 2-1, which includes the
rail extension beyond the nominal 100 mm cube (≈ 13.5 mm for 1U).

PocketQube Z-axis heights for 2p and 3p include the deployer backplate
interface per the PocketQube Standard (114 mm for 2p, 178 mm for 3p).
"""

from typing import Dict

from cubesat_specs._models import CubeSatFormFactor

# ---------------------------------------------------------------------------
# CubeSat Form Factors
# ---------------------------------------------------------------------------
#   width/depth/height in mm
#   Minimum natural frequency (all axes): 100 Hz (CDS Rev 14.1 §3.4.1)
# ---------------------------------------------------------------------------

CUBESAT_FORM_FACTORS: Dict[str, CubeSatFormFactor] = {
    "0.5U": CubeSatFormFactor(
        name="0.5U CubeSat",
        units=0.5,
        width_mm=100.0, depth_mm=100.0, height_mm=56.75,
        min_mass_kg=0.10, typical_mass_kg=0.50, max_mass_kg=1.0,
        min_freq_hz=100.0,
    ),
    "1U": CubeSatFormFactor(
        name="1U CubeSat",
        units=1.0,
        width_mm=100.0, depth_mm=100.0, height_mm=113.5,
        min_mass_kg=0.10, typical_mass_kg=1.50, max_mass_kg=2.0,
        min_freq_hz=100.0,
    ),
    "1.5U": CubeSatFormFactor(
        name="1.5U CubeSat",
        units=1.5,
        width_mm=100.0, depth_mm=100.0, height_mm=170.25,
        min_mass_kg=0.30, typical_mass_kg=2.00, max_mass_kg=3.0,
        min_freq_hz=100.0,
    ),
    "2U": CubeSatFormFactor(
        name="2U CubeSat",
        units=2.0,
        width_mm=100.0, depth_mm=100.0, height_mm=227.0,
        min_mass_kg=0.50, typical_mass_kg=3.00, max_mass_kg=4.0,
        min_freq_hz=100.0,
    ),
    "3U": CubeSatFormFactor(
        name="3U CubeSat",
        units=3.0,
        width_mm=100.0, depth_mm=100.0, height_mm=340.5,
        min_mass_kg=1.00, typical_mass_kg=4.50, max_mass_kg=6.0,
        min_freq_hz=100.0,
    ),
    "3U+": CubeSatFormFactor(
        name="3U+ CubeSat",
        units=3.0,
        width_mm=100.0, depth_mm=100.0, height_mm=360.0,
        min_mass_kg=1.00, typical_mass_kg=4.50, max_mass_kg=6.0,
        min_freq_hz=100.0,
    ),
    "6U": CubeSatFormFactor(
        name="6U CubeSat",
        units=6.0,
        width_mm=226.3, depth_mm=100.0, height_mm=366.0,
        min_mass_kg=3.00, typical_mass_kg=8.00, max_mass_kg=12.00,
        min_freq_hz=100.0,
    ),
    "12U": CubeSatFormFactor(
        name="12U CubeSat",
        units=12.0,
        width_mm=226.3, depth_mm=226.3, height_mm=366.0,
        min_mass_kg=6.00, typical_mass_kg=20.00, max_mass_kg=24.00,
        min_freq_hz=100.0,
    ),
    "16U": CubeSatFormFactor(
        name="16U CubeSat",
        units=16.0,
        width_mm=226.3, depth_mm=226.3, height_mm=488.0,
        min_mass_kg=8.00, typical_mass_kg=28.00, max_mass_kg=32.00,
        min_freq_hz=100.0,
    ),
    "27U": CubeSatFormFactor(
        name="27U CubeSat",
        units=27.0,
        width_mm=300.0, depth_mm=300.0, height_mm=340.5,
        min_mass_kg=15.00, typical_mass_kg=50.00, max_mass_kg=54.00,
        min_freq_hz=100.0,
    ),
}

# ---------------------------------------------------------------------------
# PocketQube Form Factors  (PocketQube Standard Issue 1)
# 1p = 50 × 50 × 50 mm base unit; mass ≤ 250 g per unit
# Z-axis heights for 2p/3p include backplate interface per standard.
# ---------------------------------------------------------------------------

POCKETQUBE_FORM_FACTORS: Dict[str, CubeSatFormFactor] = {
    "1p": CubeSatFormFactor(
        name="1p PocketQube",
        units=1.0,
        width_mm=50.0, depth_mm=50.0, height_mm=50.0,
        min_mass_kg=0.020, typical_mass_kg=0.100, max_mass_kg=0.250,
        min_freq_hz=100.0,
    ),
    "2p": CubeSatFormFactor(
        name="2p PocketQube",
        units=2.0,
        width_mm=50.0, depth_mm=50.0, height_mm=114.0,
        min_mass_kg=0.040, typical_mass_kg=0.200, max_mass_kg=0.500,
        min_freq_hz=100.0,
    ),
    "3p": CubeSatFormFactor(
        name="3p PocketQube",
        units=3.0,
        width_mm=50.0, depth_mm=50.0, height_mm=178.0,
        min_mass_kg=0.060, typical_mass_kg=0.300, max_mass_kg=0.750,
        min_freq_hz=100.0,
    ),
}

# ---------------------------------------------------------------------------
# Combined convenience dict  (PocketQube keys prefixed with 'pq_')
# ---------------------------------------------------------------------------

ALL_FORM_FACTORS: Dict[str, CubeSatFormFactor] = {
    **CUBESAT_FORM_FACTORS,
    **{f"pq_{k}": v for k, v in POCKETQUBE_FORM_FACTORS.items()},
}


def get_form_factor(key: str) -> CubeSatFormFactor:
    """Return a form factor by key, searching both CubeSat and PocketQube dicts.

    Parameters
    ----------
    key:
        Form factor key, e.g. ``'1U'``, ``'3U'``, ``'1p'``, ``'2p'``.

    Returns
    -------
    CubeSatFormFactor

    Raises
    ------
    KeyError
        If *key* is not found in either dictionary.
    """
    if key in CUBESAT_FORM_FACTORS:
        return CUBESAT_FORM_FACTORS[key]
    if key in POCKETQUBE_FORM_FACTORS:
        return POCKETQUBE_FORM_FACTORS[key]
    raise KeyError(
        f"Unknown form factor {key!r}. "
        f"CubeSat keys: {list(CUBESAT_FORM_FACTORS)}. "
        f"PocketQube keys: {list(POCKETQUBE_FORM_FACTORS)}."
    )
