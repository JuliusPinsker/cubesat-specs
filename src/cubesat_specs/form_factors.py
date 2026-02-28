"""Standardized CubeSat and PocketQube form factor data.

Sources
-------
- CubeSat Design Specification (CDS) Rev 14.1, Cal Poly, 2022
  https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/
  t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf
- PocketQube Standard Issue 1, 2018
  https://static1.squarespace.com/static/53d7dcdce4b07a1cdbbc08a4/
  t/5b34c395352f5303fcec6f45/1530184648111/PocketQube+Standard+issue+1+-+Published.pdf
- Alba Orbital 1P Structure Brochure (PocketQube thermal / load data)

Height values for CubeSat use the *maximum structural envelope* along the
deployment (Z) axis as defined in CDS Rev 14.1 Appendix B drawings.

PocketQube Z-axis heights for 2p and 3p follow PocketQube Standard Issue 1
Table 1 ("External dimensions without backplate"): 114 mm for 2p, 178 mm
for 3p.  The 1.6 mm sliding backplate adds to the Y-axis only (51.6 mm total).

.. versionchanged:: 0.2.0
   * ``min_freq_hz`` removed — CDS Rev 14.1 does **not** specify a minimum
     natural frequency; all vibration test levels are delegated to the
     Launch Provider (§3.1.1).
   * ``min_mass_kg`` and ``typical_mass_kg`` removed — not in CDS.
   * ``cg_limits`` added from CDS Rev 14.1 Table 2.
"""

from typing import Dict

from cubesat_specs._models import CenterOfGravityLimits, FormFactor

# ---------------------------------------------------------------------------
# CubeSat Centre-of-Gravity Limits  (CDS Rev 14.1 Table 2)
# Values are ±cm from the geometric centre on each axis.
# ---------------------------------------------------------------------------

_CG_1U = CenterOfGravityLimits(x_pm_cm=2.0, y_pm_cm=2.0, z_pm_cm=2.0)
_CG_1_5U = CenterOfGravityLimits(x_pm_cm=2.0, y_pm_cm=2.0, z_pm_cm=3.0)
_CG_2U = CenterOfGravityLimits(x_pm_cm=2.0, y_pm_cm=2.0, z_pm_cm=4.5)
_CG_3U = CenterOfGravityLimits(x_pm_cm=2.0, y_pm_cm=2.0, z_pm_cm=7.0)
_CG_6U = CenterOfGravityLimits(x_pm_cm=4.5, y_pm_cm=2.0, z_pm_cm=7.0)
_CG_12U = CenterOfGravityLimits(x_pm_cm=4.5, y_pm_cm=4.5, z_pm_cm=7.0)

# ---------------------------------------------------------------------------
# CubeSat Form Factors  (CDS Rev 14.1)
# ---------------------------------------------------------------------------
# Dimensions: Appendix B specification drawings
# Mass limits: Table 1 (§2.2.10)
# CG limits:   Table 2 (§2.2.11)
#
# Note: CDS Rev 14.1 covers 1U through 12U.  The 0.5U, 3U+, 16U and 27U
# entries are *derived from community practice* and are not in the CDS.
# ---------------------------------------------------------------------------

CUBESAT_FORM_FACTORS: Dict[str, FormFactor] = {
    "0.5U": FormFactor(
        name="0.5U CubeSat",
        units=0.5,
        width_mm=100.0, depth_mm=100.0, height_mm=56.75,
        max_mass_kg=1.0,
        cg_limits=_CG_1U,       # use 1U CG limits (conservative)
    ),
    "1U": FormFactor(
        name="1U CubeSat",
        units=1.0,
        width_mm=100.0, depth_mm=100.0, height_mm=113.5,
        max_mass_kg=2.0,
        cg_limits=_CG_1U,
    ),
    "1.5U": FormFactor(
        name="1.5U CubeSat",
        units=1.5,
        width_mm=100.0, depth_mm=100.0, height_mm=170.25,
        max_mass_kg=3.0,
        cg_limits=_CG_1_5U,
    ),
    "2U": FormFactor(
        name="2U CubeSat",
        units=2.0,
        width_mm=100.0, depth_mm=100.0, height_mm=227.0,
        max_mass_kg=4.0,
        cg_limits=_CG_2U,
    ),
    "3U": FormFactor(
        name="3U CubeSat",
        units=3.0,
        width_mm=100.0, depth_mm=100.0, height_mm=340.5,
        max_mass_kg=6.0,
        cg_limits=_CG_3U,
    ),
    "3U+": FormFactor(
        name="3U+ CubeSat",
        units=3.0,
        width_mm=100.0, depth_mm=100.0, height_mm=360.0,
        max_mass_kg=6.0,
        cg_limits=_CG_3U,       # same XY/Z envelope as 3U
    ),
    "6U": FormFactor(
        name="6U CubeSat",
        units=6.0,
        width_mm=226.3, depth_mm=100.0, height_mm=366.0,
        max_mass_kg=12.0,
        cg_limits=_CG_6U,
    ),
    "12U": FormFactor(
        name="12U CubeSat",
        units=12.0,
        width_mm=226.3, depth_mm=226.3, height_mm=366.0,
        max_mass_kg=24.0,
        cg_limits=_CG_12U,
    ),
    "16U": FormFactor(
        name="16U CubeSat",
        units=16.0,
        width_mm=226.3, depth_mm=226.3, height_mm=488.0,
        max_mass_kg=32.0,
        # 16U not in CDS Rev 14.1 — no official CG limits
    ),
    "27U": FormFactor(
        name="27U CubeSat",
        units=27.0,
        width_mm=300.0, depth_mm=300.0, height_mm=340.5,
        max_mass_kg=54.0,
        # 27U not in CDS Rev 14.1 — no official CG limits
    ),
}

# ---------------------------------------------------------------------------
# PocketQube Centre-of-Gravity Limit  (PQ-Mass-04)
# "shall not exceed 1 cm from its geometric centre" — all axes.
# ---------------------------------------------------------------------------

_CG_PQ = CenterOfGravityLimits(x_pm_cm=1.0, y_pm_cm=1.0, z_pm_cm=1.0)

# ---------------------------------------------------------------------------
# PocketQube Form Factors  (PocketQube Standard Issue 1)
# 1p = 50 × 50 × 50 mm base unit; mass ≤ 250 g per unit
# Dimensions from Table 1 ("External dimensions without backplate").
# Sliding backplate adds 1.6 mm to Y-axis (PQ-Mech-02).
#
# Thermal data from Alba Orbital 1P Structure Brochure:
#   Operational range 223–363 K  (−50 °C to +90 °C)
#   Static load capability >±40 g (three axes)
#   Sine vibration: 4 g, 5–100 Hz
# ---------------------------------------------------------------------------

POCKETQUBE_FORM_FACTORS: Dict[str, FormFactor] = {
    "1p": FormFactor(
        name="1p PocketQube",
        units=1.0,
        width_mm=50.0, depth_mm=50.0, height_mm=50.0,
        max_mass_kg=0.250,
        cg_limits=_CG_PQ,
    ),
    "2p": FormFactor(
        name="2p PocketQube",
        units=2.0,
        width_mm=50.0, depth_mm=50.0, height_mm=114.0,
        max_mass_kg=0.500,
        cg_limits=_CG_PQ,
    ),
    "3p": FormFactor(
        name="3p PocketQube",
        units=3.0,
        width_mm=50.0, depth_mm=50.0, height_mm=178.0,
        max_mass_kg=0.750,
        cg_limits=_CG_PQ,
    ),
}

# ---------------------------------------------------------------------------
# Combined convenience dict  (PocketQube keys prefixed with 'pq_')
# ---------------------------------------------------------------------------

ALL_FORM_FACTORS: Dict[str, FormFactor] = {
    **CUBESAT_FORM_FACTORS,
    **{f"pq_{k}": v for k, v in POCKETQUBE_FORM_FACTORS.items()},
}


def get_form_factor(key: str) -> FormFactor:
    """Return a form factor by key, searching both CubeSat and PocketQube dicts.

    Parameters
    ----------
    key:
        Form factor key, e.g. ``'1U'``, ``'3U'``, ``'1p'``, ``'2p'``.

    Returns
    -------
    FormFactor

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
