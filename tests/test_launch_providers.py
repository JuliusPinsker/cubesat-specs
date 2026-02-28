"""Tests for launch provider and deployer data."""
import pytest
from cubesat_specs import (
    DORBIT_ION,
    EXOPOD_6U,
    EXOPOD_12U,
    ISIPOD_3U,
    ISIPOD_6U,
    JSSOD,
    LAUNCH_PROVIDERS,
    MAVERICK_MERCURY_3,
    MAVERICK_MERCURY_6,
    MAVERICK_MERCURY_12,
    NRCSD,
    NRCSD_DOUBLEWIDE,
    NRCSD_E,
    POCKETQUBE_DEPLOYER,
    PPOD_MK3,
    ROCKETLAB_ELECTRON,
    SHERPA_FX,
    get_compatible_providers,
)
from cubesat_specs._models import DeployerSpec, LaunchProvider

# ---------------------------------------------------------------------------
# Registry completeness
# ---------------------------------------------------------------------------

ALL_PROVIDER_KEYS = [
    "nanoracks", "calpoly", "isis", "exolaunch", "spaceflight",
    "rocketlab", "alba", "jaxa", "dorbit", "maverick",
]


@pytest.mark.parametrize("key", ALL_PROVIDER_KEYS)
def test_provider_keys_present(key):
    assert key in LAUNCH_PROVIDERS, f"Missing provider: {key}"


def test_provider_count():
    assert len(LAUNCH_PROVIDERS) == len(ALL_PROVIDER_KEYS)


def test_all_providers_are_launch_provider_instances():
    for key, prov in LAUNCH_PROVIDERS.items():
        assert isinstance(prov, LaunchProvider), f"{key} is not a LaunchProvider"


def test_all_deployers_are_deployer_spec_instances():
    for key, prov in LAUNCH_PROVIDERS.items():
        for d in prov.deployers:
            assert isinstance(d, DeployerSpec), f"{key}: {d.name} bad type"


# ---------------------------------------------------------------------------
# Every deployer must have coherent data
# ---------------------------------------------------------------------------

def _all_deployers():
    """Yield (provider_key, DeployerSpec) for every deployer."""
    for key, prov in LAUNCH_PROVIDERS.items():
        for d in prov.deployers:
            yield key, d


@pytest.mark.parametrize("key,d", list(_all_deployers()), ids=lambda x: x if isinstance(x, str) else x.name)
def test_deployer_positive_mass(key, d):
    assert d.max_payload_mass_kg > 0, f"{d.name}: mass must be positive"


@pytest.mark.parametrize("key,d", list(_all_deployers()), ids=lambda x: x if isinstance(x, str) else x.name)
def test_deployer_positive_units(key, d):
    assert d.max_units > 0, f"{d.name}: max_units must be positive"


@pytest.mark.parametrize("key,d", list(_all_deployers()), ids=lambda x: x if isinstance(x, str) else x.name)
def test_deployer_has_supported_form_factors(key, d):
    assert len(d.supported_form_factors) > 0, f"{d.name}: no supported form factors"


@pytest.mark.parametrize("key,d", list(_all_deployers()), ids=lambda x: x if isinstance(x, str) else x.name)
def test_deployer_velocity_ordering(key, d):
    """If both velocity bounds are given, min ≤ max."""
    if d.deployment_velocity_min_ms is not None and d.deployment_velocity_max_ms is not None:
        assert d.deployment_velocity_min_ms <= d.deployment_velocity_max_ms, f"{d.name}: vel min > max"


# ---------------------------------------------------------------------------
# NanoRacks
# ---------------------------------------------------------------------------

def test_nanoracks_has_three_deployers():
    assert len(LAUNCH_PROVIDERS["nanoracks"].deployers) == 3


def test_nrcsd_orbit():
    assert NRCSD.inclination_deg == 51.6
    assert NRCSD.altitude_km_min == 400.0
    assert NRCSD.altitude_km_max == 420.0


def test_nrcsd_supports_1u_to_6u():
    for key in ["1U", "2U", "3U", "4U", "5U", "6U"]:
        assert key in NRCSD.supported_form_factors


# ---------------------------------------------------------------------------
# Cal Poly P-POD
# ---------------------------------------------------------------------------

def test_ppod_max_3u():
    assert PPOD_MK3.max_units == 3.0


def test_ppod_velocity():
    assert PPOD_MK3.deployment_velocity_min_ms == 1.5
    assert PPOD_MK3.deployment_velocity_max_ms == 2.0


# ---------------------------------------------------------------------------
# JAXA J-SSOD (new)
# ---------------------------------------------------------------------------

def test_jssod_orbit():
    assert JSSOD.inclination_deg == 51.6
    assert JSSOD.altitude_km_min == 380.0
    assert JSSOD.altitude_km_max == 420.0


def test_jssod_velocity():
    assert JSSOD.deployment_velocity_min_ms == 1.1
    assert JSSOD.deployment_velocity_max_ms == 1.7


def test_jssod_supports_up_to_3u():
    assert "3U" in JSSOD.supported_form_factors
    assert "6U" not in JSSOD.supported_form_factors


def test_jssod_mass():
    assert JSSOD.max_payload_mass_kg == 4.0


def test_jssod_in_jaxa_provider():
    assert JSSOD in LAUNCH_PROVIDERS["jaxa"].deployers


# ---------------------------------------------------------------------------
# D-Orbit ION (new)
# ---------------------------------------------------------------------------

def test_dorbit_ion_supports_up_to_16u():
    assert "16U" in DORBIT_ION.supported_form_factors
    assert "1U" in DORBIT_ION.supported_form_factors


def test_dorbit_ion_velocity_proprietary():
    """D-Orbit does not publish ejection velocity publicly."""
    assert DORBIT_ION.deployment_velocity_min_ms is None
    assert DORBIT_ION.deployment_velocity_max_ms is None
    assert DORBIT_ION.tip_off_rate_max_deg_s is None


def test_dorbit_ion_capacity():
    assert DORBIT_ION.max_units == 48.0
    assert DORBIT_ION.max_payload_mass_kg == 160.0


# ---------------------------------------------------------------------------
# Maverick Space Systems (new)
# ---------------------------------------------------------------------------

def test_maverick_has_three_deployers():
    assert len(LAUNCH_PROVIDERS["maverick"].deployers) == 3


def test_maverick_mercury_3_supports_3u():
    assert "3U" in MAVERICK_MERCURY_3.supported_form_factors
    assert MAVERICK_MERCURY_3.max_payload_mass_kg == 6.0


def test_maverick_mercury_6_supports_6u():
    assert "6U" in MAVERICK_MERCURY_6.supported_form_factors
    assert MAVERICK_MERCURY_6.max_payload_mass_kg == 12.0


def test_maverick_mercury_12_supports_12u():
    assert "12U" in MAVERICK_MERCURY_12.supported_form_factors
    assert MAVERICK_MERCURY_12.max_payload_mass_kg == 24.0


def test_maverick_mercury_velocity_not_public():
    """Maverick does not publish ejection velocities."""
    for d in [MAVERICK_MERCURY_3, MAVERICK_MERCURY_6, MAVERICK_MERCURY_12]:
        assert d.deployment_velocity_min_ms is None
        assert d.deployment_velocity_max_ms is None


# ---------------------------------------------------------------------------
# get_compatible_providers
# ---------------------------------------------------------------------------

def test_compatible_providers_1u():
    providers = get_compatible_providers("1U")
    names = [p.name for p in providers]
    assert any("NanoRacks" in n for n in names)
    assert any("Cal Poly" in n for n in names)
    assert any("JAXA" in n for n in names)
    assert any("D-Orbit" in n for n in names)
    assert any("Maverick" in n for n in names)


def test_compatible_providers_6u():
    providers = get_compatible_providers("6U")
    assert len(providers) >= 5


def test_compatible_providers_16u():
    providers = get_compatible_providers("16U")
    names = [p.name for p in providers]
    assert any("D-Orbit" in n for n in names)


def test_compatible_providers_pocketqube():
    providers = get_compatible_providers("1p")
    names = [p.name for p in providers]
    assert any("Alba" in n for n in names)


def test_no_provider_for_unknown():
    assert get_compatible_providers("99U") == []
