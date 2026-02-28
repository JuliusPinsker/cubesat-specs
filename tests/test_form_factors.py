"""Tests for CubeSat and PocketQube form factor data."""
import pytest
from cubesat_specs import (
    CUBESAT_FORM_FACTORS,
    POCKETQUBE_FORM_FACTORS,
    FormFactor,
    CenterOfGravityLimits,
    get_form_factor,
)


# --- CubeSat registry ---

def test_cubesat_keys_present():
    for key in ["0.5U", "1U", "1.5U", "2U", "3U", "3U+", "6U", "12U", "16U", "27U"]:
        assert key in CUBESAT_FORM_FACTORS, f"Missing key: {key}"


def test_1u_dimensions():
    ff = CUBESAT_FORM_FACTORS["1U"]
    assert ff.width_mm == 100.0
    assert ff.depth_mm == 100.0
    assert ff.height_mm == 113.5
    assert ff.max_mass_kg == 2.0


def test_3u_mass_limit():
    assert CUBESAT_FORM_FACTORS["3U"].max_mass_kg == 6.0


def test_6u_cross_section():
    """6U is 2U wide, so width_mm should be ~226.3 mm."""
    ff = CUBESAT_FORM_FACTORS["6U"]
    assert ff.width_mm == 226.3
    assert ff.depth_mm == 100.0


def test_volume_1u():
    ff = CUBESAT_FORM_FACTORS["1U"]
    assert abs(ff.volume_liters - 1.135) < 0.01


def test_mass_density_positive():
    for ff in CUBESAT_FORM_FACTORS.values():
        assert ff.mass_density_max_kg_per_liter > 0


# --- CG limits (CDS Rev 14.1 Table 2) ---

def test_1u_cg_limits():
    cg = CUBESAT_FORM_FACTORS["1U"].cg_limits
    assert cg.x_pm_cm == 2.0
    assert cg.y_pm_cm == 2.0
    assert cg.z_pm_cm == 2.0


def test_6u_cg_limits():
    cg = CUBESAT_FORM_FACTORS["6U"].cg_limits
    assert cg.x_pm_cm == 4.5
    assert cg.y_pm_cm == 2.0
    assert cg.z_pm_cm == 7.0


def test_12u_cg_limits():
    cg = CUBESAT_FORM_FACTORS["12U"].cg_limits
    assert cg.x_pm_cm == 4.5
    assert cg.y_pm_cm == 4.5
    assert cg.z_pm_cm == 7.0


def test_cg_within():
    cg = CenterOfGravityLimits(x_pm_cm=2.0, y_pm_cm=2.0, z_pm_cm=2.0)
    assert cg.within(1.0, 1.0, 1.0)
    assert cg.within(2.0, 2.0, 2.0)
    assert not cg.within(2.1, 0.0, 0.0)


def test_cg_none_means_no_limit():
    """None axes are always within limit."""
    cg = CenterOfGravityLimits()
    assert cg.within(999.0, 999.0, 999.0)


def test_16u_27u_no_cds_cg():
    """16U/27U are not in CDS — CG limits default to None."""
    for key in ("16U", "27U"):
        cg = CUBESAT_FORM_FACTORS[key].cg_limits
        assert cg.x_pm_cm is None
        assert cg.y_pm_cm is None
        assert cg.z_pm_cm is None


# --- PocketQube ---

def test_pocketqube_keys_present():
    for key in ["1p", "2p", "3p"]:
        assert key in POCKETQUBE_FORM_FACTORS


def test_1p_dimensions():
    ff = POCKETQUBE_FORM_FACTORS["1p"]
    assert ff.width_mm == 50.0
    assert ff.depth_mm == 50.0
    assert ff.height_mm == 50.0
    assert ff.max_mass_kg == 0.250


def test_pocketqube_cg_limits():
    """PQ-Mass-04: CG shall not exceed 1 cm from geometric centre."""
    for key in ("1p", "2p", "3p"):
        cg = POCKETQUBE_FORM_FACTORS[key].cg_limits
        assert cg.x_pm_cm == 1.0
        assert cg.y_pm_cm == 1.0
        assert cg.z_pm_cm == 1.0


def test_pocketqube_2p_height():
    """PocketQube Standard Table 1: 2P = 114 mm Z."""
    assert POCKETQUBE_FORM_FACTORS["2p"].height_mm == 114.0


def test_pocketqube_3p_height():
    """PocketQube Standard Table 1: 3P = 178 mm Z."""
    assert POCKETQUBE_FORM_FACTORS["3p"].height_mm == 178.0


# --- get_form_factor() ---

def test_get_cubesat():
    ff = get_form_factor("6U")
    assert ff.units == 6.0


def test_get_pocketqube():
    ff = get_form_factor("2p")
    assert ff.units == 2.0


def test_get_invalid_raises():
    with pytest.raises(KeyError, match="99U"):
        get_form_factor("99U")


def test_is_same_cross_section():
    ff_1u = CUBESAT_FORM_FACTORS["1U"]
    ff_2u = CUBESAT_FORM_FACTORS["2U"]
    ff_6u = CUBESAT_FORM_FACTORS["6U"]
    assert ff_1u.is_same_cross_section(ff_2u)
    assert not ff_1u.is_same_cross_section(ff_6u)


def test_repr_uses_formfactor():
    ff = CUBESAT_FORM_FACTORS["1U"]
    assert repr(ff).startswith("FormFactor(")
