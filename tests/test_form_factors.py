"""Tests for CubeSat and PocketQube form factor data."""
import pytest
from cubesat_specs import CUBESAT_FORM_FACTORS, POCKETQUBE_FORM_FACTORS, get_form_factor


# --- CubeSat ---

def test_cubesat_keys_present():
    for key in ["0.5U", "1U", "1.5U", "2U", "3U", "3U+", "6U", "12U", "16U", "27U"]:
        assert key in CUBESAT_FORM_FACTORS, f"Missing key: {key}"


def test_1u_dimensions():
    ff = CUBESAT_FORM_FACTORS["1U"]
    assert ff.width_mm == 100.0
    assert ff.depth_mm == 100.0
    assert ff.height_mm == 113.5
    assert ff.max_mass_kg == 1.33
    assert ff.min_freq_hz == 100.0


def test_3u_mass_limit():
    assert CUBESAT_FORM_FACTORS["3U"].max_mass_kg == 4.0


def test_6u_cross_section():
    """6U is 2U wide, so width_mm should be ~226.3 mm."""
    ff = CUBESAT_FORM_FACTORS["6U"]
    assert ff.width_mm == 226.3
    assert ff.depth_mm == 100.0


def test_volume_1u():
    ff = CUBESAT_FORM_FACTORS["1U"]
    # 100 × 100 × 113.5 mm = 1 135 000 mm³ = 1135 cm³ = 1.135 L
    assert abs(ff.volume_liters - 1.135) < 0.01


def test_mass_density_positive():
    for ff in CUBESAT_FORM_FACTORS.values():
        assert ff.mass_density_max_kg_per_liter > 0


def test_min_mass_lt_max_mass():
    for key, ff in CUBESAT_FORM_FACTORS.items():
        assert ff.min_mass_kg < ff.max_mass_kg, f"{key}: min_mass >= max_mass"


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
