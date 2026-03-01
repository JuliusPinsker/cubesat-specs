"""cubesat_specs — Standardized CubeSat and PocketQube form factor data.

Provides
--------
Data models
  FormFactor, CenterOfGravityLimits, DeployerSpec, LaunchProvider

Form-factor registries
  CUBESAT_FORM_FACTORS        dict[str, FormFactor]   (0.5U … 27U)
  POCKETQUBE_FORM_FACTORS     dict[str, FormFactor]   (1p … 3p)
  ALL_FORM_FACTORS            combined dict (cubesat + ``pq_``-prefixed PocketQube)

Launch providers
  LAUNCH_PROVIDERS            dict[str, LaunchProvider]

Standards
  CDS                         CDS Rev 14.1 constraints  (``cubesat_specs.standards``)
  PQS                         PocketQube Std Issue 1 constraints

Lookup helpers
  get_form_factor(key)        unified lookup
  get_compatible_providers(key)  providers whose deployers support the form factor
"""

from cubesat_specs._models import (
    CenterOfGravityLimits,
    DeployerSpec,
    FormFactor,
    LaunchProvider,
)
from cubesat_specs.form_factors import (
    ALL_FORM_FACTORS,
    CUBESAT_FORM_FACTORS,
    POCKETQUBE_FORM_FACTORS,
    get_form_factor,
)
from cubesat_specs.launch_providers import (
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
from cubesat_specs.standards import CDS, CDSConstraints, PQS, PQSConstraints

__version__ = "0.2.1"

__all__ = [
    # data models
    "FormFactor",
    "CenterOfGravityLimits",
    "DeployerSpec",
    "LaunchProvider",
    # registries
    "CUBESAT_FORM_FACTORS",
    "POCKETQUBE_FORM_FACTORS",
    "ALL_FORM_FACTORS",
    "LAUNCH_PROVIDERS",
    # deployers
    "PPOD_MK3",
    "NRCSD",
    "NRCSD_E",
    "NRCSD_DOUBLEWIDE",
    "ISIPOD_3U",
    "ISIPOD_6U",
    "EXOPOD_6U",
    "EXOPOD_12U",
    "SHERPA_FX",
    "ROCKETLAB_ELECTRON",
    "POCKETQUBE_DEPLOYER",
    "JSSOD",
    "DORBIT_ION",
    "MAVERICK_MERCURY_3",
    "MAVERICK_MERCURY_6",
    "MAVERICK_MERCURY_12",
    # standards
    "CDS",
    "CDSConstraints",
    "PQS",
    "PQSConstraints",
    # helpers
    "get_form_factor",
    "get_compatible_providers",
    "data_path",
    "load_json",
    "__version__",
]


import json as _json
import pathlib as _pathlib


def data_path() -> _pathlib.Path:
    """Return the directory containing the machine-readable JSON data files.

    Useful for non-Python consumers that want the path to the installed
    JSON files, or for programmatic loading.

    >>> from cubesat_specs import data_path
    >>> sorted(p.name for p in data_path().glob("*.json"))  # doctest: +SKIP
    ['deployers.json', 'form_factors.json', ...]
    """
    return _pathlib.Path(__file__).parent / "data"


def load_json(name: str) -> dict:
    """Load one of the bundled JSON data files and return it as a dict.

    Parameters
    ----------
    name:
        Filename without directory, e.g. ``'form_factors.json'`` or
        ``'standards_cds.json'``.

    Returns
    -------
    dict
        Parsed JSON data.

    Raises
    ------
    FileNotFoundError
        If *name* does not exist in the data directory.
    """
    path = data_path() / name
    if not path.exists():
        available = [p.name for p in data_path().glob("*.json")]
        raise FileNotFoundError(
            f"No data file {name!r}. Available: {available}"
        )
    return _json.loads(path.read_text(encoding="utf-8"))
