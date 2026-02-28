"""Launch provider and deployer specifications.

Sources
-------
- CubeSat Design Specification (CDS) Rev 14.1, Cal Poly, 2022
  https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/
  t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf
- NanoRacks NRCSD-E IDD
  https://nanoracks.com/wp-content/uploads/Nanoracks-External-Cygnus-Deployer-E-NRCSD-IDD.pdf
- NanoRacks NRCSD IDD Rev D
  https://nanoracks.com/wp-content/uploads/Nanoracks-CubeSat-Deployer-NRCSD-IDD.pdf
- Cal Poly P-POD Mk III Rev E User Guide
  https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/
  t/5806854d6b8f5b8eb57b83bd/1476822350599/P-POD_MkIIIRevE_UserGuide.pdf
- ISIS ISIPOD datasheet  https://www.isispace.nl
- Exolaunch EXOpod datasheet  https://exolaunch.com
- Rocket Lab customer guide  https://www.rocketlabusa.com
- SpaceFlight Inc. Sherpa-FX guide  https://spaceflight.com
"""

from typing import Dict, List

from cubesat_specs._models import DeployerSpec, LaunchProvider

# ---------------------------------------------------------------------------
# Deployer Specifications
# ---------------------------------------------------------------------------

PPOD_MK3 = DeployerSpec(
    name="P-POD Mk III",
    provider="Cal Poly",
    max_units=3.0,
    supported_form_factors=["1U", "2U", "3U"],
    deployment_velocity_min_ms=1.5,
    deployment_velocity_max_ms=2.0,
    tip_off_rate_max_deg_s=5.0,
    max_payload_mass_kg=6.0,
    mechanism="spring",
    notes=(
        "Original CubeSat standard deployer. Internal volume 340 × 100 × 100 mm. "
        "Accepts 1U+1U+1U, 2U+1U, or 3U configurations. "
        "Exit velocity ~2.0 m/s for 4 kg payload (P-POD Mk III Rev E User Guide)."
    ),
)

NRCSD = DeployerSpec(
    name="NanoRacks CubeSat Deployer (NRCSD)",
    provider="NanoRacks / Voyager Space",
    max_units=6.0,
    supported_form_factors=["1U", "2U", "3U", "4U", "5U", "6U"],
    deployment_velocity_min_ms=0.5,
    deployment_velocity_max_ms=2.0,
    tip_off_rate_max_deg_s=5.0,
    max_payload_mass_kg=14.0,
    mechanism="spring",
    inclination_deg=51.6,
    altitude_km_min=400.0,
    altitude_km_max=420.0,
    notes=(
        "ISS-based deployment via JEM airlock. Up to 6U per silo (1U–6U). "
        "Battery: ≤100 Wh total stored chemical energy (FAA requirement). "
        "Deployment velocity 0.5–2.0 m/s; tip-off target < 2 deg/s/axis."
    ),
)

NRCSD_E = DeployerSpec(
    name="NanoRacks External Cygnus Deployer (NRCSD-E)",
    provider="NanoRacks / Voyager Space",
    max_units=6.0,
    supported_form_factors=["1U", "2U", "3U", "4U", "5U", "6U"],
    deployment_velocity_min_ms=0.5,
    deployment_velocity_max_ms=2.0,
    tip_off_rate_max_deg_s=5.0,
    max_payload_mass_kg=14.0,
    mechanism="spring",
    inclination_deg=51.6,
    altitude_km_min=400.0,
    altitude_km_max=450.0,
    notes=(
        "External ISS deployment via Cygnus robotic arm. "
        "Six silos × 6U = 36U total capacity per NRCSD-E unit. "
        "Deployment occurs after Cygnus departs ISS, nominally ~450 km altitude. "
        "Min three deployment switches required on payload."
    ),
)

NRCSD_DOUBLEWIDE = DeployerSpec(
    name="NanoRacks NRCSD DoubleWide",
    provider="NanoRacks / Voyager Space",
    max_units=12.0,
    supported_form_factors=["6U", "12U"],
    deployment_velocity_min_ms=0.5,
    deployment_velocity_max_ms=2.0,
    tip_off_rate_max_deg_s=5.0,
    max_payload_mass_kg=28.0,
    mechanism="spring",
    inclination_deg=51.6,
    altitude_km_min=400.0,
    altitude_km_max=420.0,
    notes="Accommodates 2 × 6U (12U equivalent). ISS-based. Up to 48U per mission cycle.",
)

ISIPOD_3U = DeployerSpec(
    name="ISIS ISIPOD 3U",
    provider="Innovative Solutions In Space (ISIS)",
    max_units=3.0,
    supported_form_factors=["1U", "2U", "3U"],
    deployment_velocity_min_ms=1.5,
    deployment_velocity_max_ms=2.5,
    tip_off_rate_max_deg_s=3.0,
    max_payload_mass_kg=6.0,
    mechanism="spring",
    notes="Standard ISIS deployer. Internal 340.5 × 100 × 100 mm. PC/104 compatible.",
)

ISIPOD_6U = DeployerSpec(
    name="ISIS ISIPOD 6U",
    provider="Innovative Solutions In Space (ISIS)",
    max_units=6.0,
    supported_form_factors=["6U"],
    deployment_velocity_min_ms=1.5,
    deployment_velocity_max_ms=2.5,
    tip_off_rate_max_deg_s=3.0,
    max_payload_mass_kg=12.0,
    mechanism="spring",
    notes="Internal 226.3 × 100 × 366 mm. Widely used on PSLV and Falcon rideshare.",
)

EXOPOD_6U = DeployerSpec(
    name="Exolaunch EXOpod 6U",
    provider="Exolaunch GmbH",
    max_units=6.0,
    supported_form_factors=["6U"],
    deployment_velocity_min_ms=1.2,
    deployment_velocity_max_ms=2.4,
    tip_off_rate_max_deg_s=10.0,
    max_payload_mass_kg=12.0,
    mechanism="spring",
    notes=(
        "Primary deployer on SpaceX Transporter rideshare missions. "
        "Passive tip-off damping; max <10 deg/s all axes (EXOpod User Manual). "
        "Customizable ejection velocity available."
    ),
)

EXOPOD_12U = DeployerSpec(
    name="Exolaunch EXOpod 12U",
    provider="Exolaunch GmbH",
    max_units=12.0,
    supported_form_factors=["12U"],
    deployment_velocity_min_ms=1.2,
    deployment_velocity_max_ms=2.4,
    tip_off_rate_max_deg_s=10.0,
    max_payload_mass_kg=24.0,
    mechanism="spring",
    notes="Used on SpaceX Transporter rideshare missions. Max tip-off <10 deg/s all axes.",
)

SHERPA_FX = DeployerSpec(
    name="SpaceFlight Sherpa-FX OTV Deployer",
    provider="SpaceFlight Inc.",
    max_units=12.0,
    supported_form_factors=["1U", "2U", "3U", "6U", "12U"],
    deployment_velocity_min_ms=1.0,
    deployment_velocity_max_ms=3.0,
    tip_off_rate_max_deg_s=5.0,
    max_payload_mass_kg=300.0,
    mechanism="spring",
    notes=(
        "Orbital transfer vehicle; orbit depends on rideshare primary mission. "
        "Supports multiple deployer rail configurations."
    ),
)

ROCKETLAB_ELECTRON = DeployerSpec(
    name="Rocket Lab Electron Rideshare Deployer",
    provider="Rocket Lab",
    max_units=12.0,
    supported_form_factors=["1U", "2U", "3U", "6U", "12U"],
    deployment_velocity_min_ms=1.0,
    deployment_velocity_max_ms=2.5,
    tip_off_rate_max_deg_s=5.0,
    max_payload_mass_kg=30.0,
    mechanism="spring",
    notes=(
        "Electron launch vehicle. Primarily SSO (97–98°) at 400–1200 km. "
        "Kick Stage enables precise orbit insertion."
    ),
)

POCKETQUBE_DEPLOYER = DeployerSpec(
    name="PocketQube Deployer (4p)",
    provider="Alba Orbital / Various",
    max_units=4.0,
    supported_form_factors=["1p", "2p", "3p"],
    deployment_velocity_min_ms=0.5,
    deployment_velocity_max_ms=2.0,
    tip_off_rate_max_deg_s=5.0,
    max_payload_mass_kg=1.0,
    mechanism="spring",
    notes="Standard PocketQube deployer, 4p capacity per tube. Used on PSLV rideshare.",
)

# ---------------------------------------------------------------------------
# Launch Providers
# ---------------------------------------------------------------------------

LAUNCH_PROVIDERS: Dict[str, LaunchProvider] = {
    "nanoracks": LaunchProvider(
        name="NanoRacks (Voyager Space)",
        website="https://nanoracks.com",
        deployers=[NRCSD, NRCSD_E, NRCSD_DOUBLEWIDE],
        notes=(
            "ISS-based deployment. Orbit: 51.6° inclination, 400–420 km. "
            "No hazardous materials. Battery energy limits apply."
        ),
    ),
    "calpoly": LaunchProvider(
        name="Cal Poly",
        website="https://www.cubesat.org",
        deployers=[PPOD_MK3],
        notes="Originator of the CubeSat standard and P-POD deployer.",
    ),
    "isis": LaunchProvider(
        name="Innovative Solutions In Space (ISIS)",
        website="https://www.isispace.nl",
        deployers=[ISIPOD_3U, ISIPOD_6U],
        notes="Dutch small satellite manufacturer and launch broker. Flight heritage since 2013.",
    ),
    "exolaunch": LaunchProvider(
        name="Exolaunch GmbH",
        website="https://exolaunch.com",
        deployers=[EXOPOD_6U, EXOPOD_12U],
        notes="German rideshare & integration company; SpaceX Transporter partner.",
    ),
    "spaceflight": LaunchProvider(
        name="SpaceFlight Inc.",
        website="https://spaceflight.com",
        deployers=[SHERPA_FX],
        notes="US rideshare aggregator with dedicated orbital transfer vehicles.",
    ),
    "rocketlab": LaunchProvider(
        name="Rocket Lab",
        website="https://www.rocketlabusa.com",
        deployers=[ROCKETLAB_ELECTRON],
        notes="Electron launch vehicle; primarily SSO missions.",
    ),
    "alba": LaunchProvider(
        name="Alba Orbital",
        website="https://www.albaorbital.com",
        deployers=[POCKETQUBE_DEPLOYER],
        notes="Scottish PocketQube specialist; Pale Blue Dot rideshare missions.",
    ),
}


def get_compatible_providers(form_factor_key: str) -> List[LaunchProvider]:
    """Return all launch providers whose deployers support *form_factor_key*.

    Parameters
    ----------
    form_factor_key:
        Form factor key, e.g. ``'1U'``, ``'6U'``, ``'1p'``.

    Returns
    -------
    list[LaunchProvider]
        Providers with at least one deployer accepting the given form factor.
    """
    result: List[LaunchProvider] = []
    for provider in LAUNCH_PROVIDERS.values():
        for deployer in provider.deployers:
            if form_factor_key in deployer.supported_form_factors:
                result.append(provider)
                break
    return result
