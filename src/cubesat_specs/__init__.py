"""cubesat_specs — Standardized CubeSat and PocketQube form factor data.

Provides:
  CUBESAT_FORM_FACTORS        dict[str, CubeSatFormFactor]   (0.5U … 27U)
  POCKETQUBE_FORM_FACTORS     dict[str, CubeSatFormFactor]   (1p … 3p)
  ALL_FORM_FACTORS            combined dict (cubesat + pq_ prefixed PocketQube)
  LAUNCH_PROVIDERS            dict[str, LaunchProvider]
  get_form_factor(key)        unified lookup
  get_compatible_providers(key)  providers whose deployers support the form factor
"""

from cubesat_specs._models import CubeSatFormFactor, DeployerSpec, LaunchProvider
from cubesat_specs.form_factors import (
    CUBESAT_FORM_FACTORS,
    POCKETQUBE_FORM_FACTORS,
    ALL_FORM_FACTORS,
    get_form_factor,
)
from cubesat_specs.launch_providers import LAUNCH_PROVIDERS, get_compatible_providers

__version__ = "0.1.1"

__all__ = [
    "CubeSatFormFactor",
    "DeployerSpec",
    "LaunchProvider",
    "CUBESAT_FORM_FACTORS",
    "POCKETQUBE_FORM_FACTORS",
    "ALL_FORM_FACTORS",
    "LAUNCH_PROVIDERS",
    "get_form_factor",
    "get_compatible_providers",
    "__version__",
]
