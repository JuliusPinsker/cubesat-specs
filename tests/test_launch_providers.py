"""Tests for launch provider and deployer data."""
import pytest
from cubesat_specs import LAUNCH_PROVIDERS, get_compatible_providers


def test_provider_keys_present():
    for key in ["nanoracks", "calpoly", "isis", "exolaunch", "spaceflight", "rocketlab", "alba"]:
        assert key in LAUNCH_PROVIDERS, f"Missing provider: {key}"


def test_nanoracks_has_three_deployers():
    assert len(LAUNCH_PROVIDERS["nanoracks"].deployers) == 3


def test_nrcsd_orbit():
    nrcsd = next(
        d for d in LAUNCH_PROVIDERS["nanoracks"].deployers
        if d.name == "NanoRacks CubeSat Deployer (NRCSD)"
    )
    assert nrcsd.inclination_deg == 51.6
    assert nrcsd.altitude_km_min == 400.0
    assert nrcsd.altitude_km_max == 420.0


def test_nrcsd_supports_1u_to_6u():
    nrcsd = next(
        d for d in LAUNCH_PROVIDERS["nanoracks"].deployers
        if d.name == "NanoRacks CubeSat Deployer (NRCSD)"
    )
    for key in ["1U", "2U", "3U", "4U", "5U", "6U"]:
        assert key in nrcsd.supported_form_factors


def test_ppod_max_3u():
    ppod = LAUNCH_PROVIDERS["calpoly"].deployers[0]
    assert ppod.max_units == 3.0


def test_compatible_providers_1u():
    providers = get_compatible_providers("1U")
    names = [p.name for p in providers]
    assert any("NanoRacks" in n for n in names)
    assert any("Cal Poly" in n for n in names)


def test_compatible_providers_6u_multiple():
    providers = get_compatible_providers("6U")
    assert len(providers) >= 3


def test_compatible_providers_pocketqube():
    providers = get_compatible_providers("1p")
    names = [p.name for p in providers]
    assert any("Alba" in n for n in names)


def test_no_provider_for_unknown():
    providers = get_compatible_providers("99U")
    assert providers == []
