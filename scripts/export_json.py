#!/usr/bin/env python3
"""Export all cubesat-specs data to machine-readable JSON files.

Run from the repository root:

    python scripts/export_json.py

Outputs are written to ``src/cubesat_specs/data/``.
"""
from __future__ import annotations

import dataclasses
import json
import pathlib
import sys

# Ensure the local source tree is importable
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import cubesat_specs  # noqa: E402
from cubesat_specs import (  # noqa: E402
    ALL_FORM_FACTORS,
    CUBESAT_FORM_FACTORS,
    LAUNCH_PROVIDERS,
    POCKETQUBE_FORM_FACTORS,
)
from cubesat_specs.standards import (  # noqa: E402
    CDS,
    PQS,
    PQ_BACKPLATE_DIMENSIONS,
    PQ_RECOMMENDED_BASEPLATE_MATERIALS,
    RECOMMENDED_AL_ALLOYS,
    VIBRATION_NOTE,
    SHOCK_NOTE,
)

DATA_DIR = ROOT / "src" / "cubesat_specs" / "data"


def _serializable(obj: object) -> object:
    """Make dataclass / tuple / other types JSON-serializable."""
    if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
        return {k: _serializable(v) for k, v in dataclasses.asdict(obj).items()}
    if isinstance(obj, (list, tuple)):
        return [_serializable(i) for i in obj]
    if isinstance(obj, dict):
        return {k: _serializable(v) for k, v in obj.items()}
    return obj


def export_form_factors() -> None:
    """Export form factors to JSON."""
    data = {
        "$schema": "cubesat-specs/form_factors",
        "version": cubesat_specs.__version__,
        "cubesat": {},
        "pocketqube": {},
    }
    for key, ff in CUBESAT_FORM_FACTORS.items():
        data["cubesat"][key] = _serializable(ff)
    for key, ff in POCKETQUBE_FORM_FACTORS.items():
        data["pocketqube"][key] = _serializable(ff)
    path = DATA_DIR / "form_factors.json"
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"  {path.relative_to(ROOT)}")


def export_deployers() -> None:
    """Export deployer specs to JSON."""
    deployers: dict = {}
    for prov_key, prov in LAUNCH_PROVIDERS.items():
        for d in prov.deployers:
            # Use a slug derived from the variable name convention
            slug = d.name.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
            deployers[slug] = _serializable(d)
    data = {
        "$schema": "cubesat-specs/deployers",
        "version": cubesat_specs.__version__,
        "deployers": deployers,
    }
    path = DATA_DIR / "deployers.json"
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"  {path.relative_to(ROOT)}")


def export_launch_providers() -> None:
    """Export launch providers to JSON."""
    providers: dict = {}
    for key, prov in LAUNCH_PROVIDERS.items():
        providers[key] = {
            "name": prov.name,
            "website": prov.website,
            "notes": prov.notes,
            "deployers": [d.name for d in prov.deployers],
        }
    data = {
        "$schema": "cubesat-specs/launch_providers",
        "version": cubesat_specs.__version__,
        "providers": providers,
    }
    path = DATA_DIR / "launch_providers.json"
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"  {path.relative_to(ROOT)}")


def export_standards() -> None:
    """Export CDS and PQS constraints to JSON."""
    cds_data = {
        "$schema": "cubesat-specs/standards_cds",
        "version": cubesat_specs.__version__,
        "source": "CubeSat Design Specification (CDS) Rev 14.1, Cal Poly, 2022",
        "constraints": _serializable(CDS),
        "recommended_al_alloys": list(RECOMMENDED_AL_ALLOYS),
        "notes": {
            "vibration": VIBRATION_NOTE,
            "shock": SHOCK_NOTE,
        },
    }
    path_cds = DATA_DIR / "standards_cds.json"
    path_cds.write_text(json.dumps(cds_data, indent=2) + "\n")
    print(f"  {path_cds.relative_to(ROOT)}")

    pqs_data = {
        "$schema": "cubesat-specs/standards_pqs",
        "version": cubesat_specs.__version__,
        "source": "PocketQube Standard Issue 1, TU Delft / Alba Orbital / GAUSS Srl, 2018",
        "constraints": _serializable(PQS),
        "backplate_dimensions": {
            k: {"x_mm": v[0], "z_mm": v[1], "thickness_mm": v[2]}
            for k, v in PQ_BACKPLATE_DIMENSIONS.items()
        },
        "recommended_baseplate_materials": list(PQ_RECOMMENDED_BASEPLATE_MATERIALS),
    }
    path_pqs = DATA_DIR / "standards_pqs.json"
    path_pqs.write_text(json.dumps(pqs_data, indent=2) + "\n")
    print(f"  {path_pqs.relative_to(ROOT)}")


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Exporting cubesat-specs v{cubesat_specs.__version__} data →")
    export_form_factors()
    export_deployers()
    export_launch_providers()
    export_standards()
    print("Done.")


if __name__ == "__main__":
    main()
