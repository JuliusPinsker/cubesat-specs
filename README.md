# cubesat-specs

[![PyPI version](https://img.shields.io/pypi/v/cubesat-specs.svg)](https://pypi.org/project/cubesat-specs/)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/cubesat-specs.svg)](https://anaconda.org/conda-forge/cubesat-specs)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/JuliusPinsker/cubesat-specs/actions/workflows/test.yml/badge.svg)](https://github.com/JuliusPinsker/cubesat-specs/actions/workflows/test.yml)
[![Docs](https://readthedocs.org/projects/cubesat-specs/badge/?version=latest)](https://cubesat-specs.readthedocs.io)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18827692.svg)](https://doi.org/10.5281/zenodo.18827692)

Standardized **CubeSat** and **PocketQube** form factor specifications, design constraints, and launch provider deployer data — no hardcoding required.

```bash
pip install cubesat-specs     # PyPI
conda install -c conda-forge cubesat-specs  # conda-forge (coming soon)
```

**Non-Python?** All data is also available as [machine-readable JSON files](src/cubesat_specs/data/) — use them from MATLAB, Julia, C++, JavaScript, or any language.

## Quick Start

```python
from cubesat_specs import (
    CUBESAT_FORM_FACTORS,
    POCKETQUBE_FORM_FACTORS,
    get_form_factor,
    get_compatible_providers,
    CDS,   # CubeSat Design Specification Rev 14.1
    PQS,   # PocketQube Standard Issue 1
)

# Look up a 3U CubeSat
ff = get_form_factor("3U")
print(ff.width_mm, ff.depth_mm, ff.height_mm)  # 100.0 100.0 340.5
print(ff.max_mass_kg)                            # 6.0
print(ff.volume_liters)                          # 3.405

# Centre-of-gravity check (CDS Rev 14.1 Table 2)
ff.cg_limits.within(1.0, 1.0, 5.0)  # True — within ±2/±2/±7 cm

# PocketQube 2p
pq = get_form_factor("2p")
print(pq.max_mass_kg)          # 0.5
pq.cg_limits.within(0.5, 0.5, 0.5)  # True — within ±1 cm (PQ-Mass-04)

# CDS constraints
print(CDS.rf_silence_minutes)       # 45
print(CDS.outgassing_tml_max_pct)   # 1.0

# PocketQube Standard constraints
print(PQS.min_kill_switches)        # 2
print(PQS.component_envelope_mm)    # 7.0

# Which launch providers accept a 6U?
for provider in get_compatible_providers("6U"):
    deployer_names = [d.name for d in provider.deployers
                      if "6U" in d.supported_form_factors]
    print(f"{provider.name}: {deployer_names}")
```

## CubeSat Form Factors (CDS Rev 14.1)

| Key   | W × D × H (mm)          | Max mass (kg) | CG limits ±cm (X/Y/Z) |
|-------|--------------------------|---------------|------------------------|
| 0.5U  | 100 × 100 × 56.75        | 1.00          | 2/2/2 *               |
| 1U    | 100 × 100 × 113.5        | 2.00          | 2/2/2                 |
| 1.5U  | 100 × 100 × 170.25       | 3.00          | 2/2/3                 |
| 2U    | 100 × 100 × 227.0        | 4.00          | 2/2/4.5               |
| 3U    | 100 × 100 × 340.5        | 6.00          | 2/2/7                 |
| 3U+   | 100 × 100 × 360.0        | 6.00          | 2/2/7                 |
| 6U    | 226.3 × 100 × 366.0      | 12.00         | 4.5/2/7               |
| 12U   | 226.3 × 226.3 × 366.0    | 24.00         | 4.5/4.5/7             |
| 16U   | 226.3 × 226.3 × 488.0    | 32.00         | —                     |
| 27U   | 300 × 300 × 340.5        | 54.00         | —                     |

\* 0.5U, 3U+, 16U, and 27U are community-derived, not in CDS Rev 14.1.

## PocketQube Form Factors (PocketQube Standard Issue 1)

| Key | W × D × H (mm) | Max mass (g) | CG limit |
|-----|-----------------|--------------|----------|
| 1p  | 50 × 50 × 50   | 250          | ±1 cm    |
| 2p  | 50 × 50 × 114  | 500          | ±1 cm    |
| 3p  | 50 × 50 × 178  | 750          | ±1 cm    |

Dimensions are *without* the 1.6 mm sliding backplate (Y-axis).

## Design Constraints

The `CDS` and `PQS` singletons expose every quantitative constraint from
the respective standards as simple attributes:

### CDS Rev 14.1 highlights

| Attribute                       | Value           | CDS §     |
|---------------------------------|-----------------|-----------|
| `rail_min_width_mm`             | 8.5             | 2.2.5     |
| `max_protrusion_mm`             | 6.5             | 2.2.3     |
| `outgassing_tml_max_pct`        | 1.0 %           | 2.1.7     |
| `outgassing_cvcm_max_pct`       | 0.1 %           | 2.1.7     |
| `rf_silence_minutes`            | 45              | 2.4.5     |
| `deployable_wait_minutes`       | 30              | 2.4.4     |
| `min_deployment_switches`       | 1               | 2.3.2     |
| `battery_faa_guideline_wh`      | 100             | 2.1.5     |

### PocketQube Standard Issue 1 highlights

| Attribute                   | Value         | PQ req.   |
|-----------------------------|---------------|-----------|
| `min_kill_switches`         | 2             | Mech-12   |
| `component_envelope_mm`     | 7.0           | Mech-08   |
| `deployable_envelope_mm`    | 10.0          | Mech-08   |
| `cg_max_offset_cm`          | 1.0           | Mass-04   |
| `mass_per_unit_kg`          | 0.250         | Mass-01   |
| `backplate_thickness_mm`    | 1.6           | Table 1   |
| `pyrotechnics_allowed`      | False         | Gen-02    |

## Launch Providers & Deployers

| Provider key   | Provider              | Deployers                                      |
|----------------|-----------------------|------------------------------------------------|
| `nanoracks`    | NanoRacks             | NRCSD, NRCSD-E, NRCSD DoubleWide              |
| `calpoly`      | Cal Poly              | P-POD Mk III                                   |
| `isis`         | ISIS                  | ISIPOD 3U, ISIPOD 6U                           |
| `exolaunch`    | Exolaunch GmbH        | EXOpod 6U, EXOpod 12U                          |
| `spaceflight`  | SpaceFlight Inc.      | Sherpa-FX                                      |
| `rocketlab`    | Rocket Lab            | Electron Rideshare Deployer                    |
| `alba`         | Alba Orbital          | PocketQube Deployer (4p)                       |
| `jaxa`         | JAXA                  | J-SSOD (10 cm class)                            |
| `dorbit`       | D-Orbit               | ION Satellite Carrier                           |
| `maverick`     | Maverick Space Systems| Mercury-3, Mercury-6, Mercury-12                |

Each `DeployerSpec` carries: `supported_form_factors`, `max_payload_mass_kg`,
optional `deployment_velocity_min/max_ms` and `tip_off_rate_max_deg_s`
(``None`` when proprietary), and optional `inclination_deg` / `altitude_km_min/max`.

## Data Sources

- [CubeSat Design Specification (CDS) Rev 14.1](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf), Cal Poly, 2022
- [PocketQube Standard Issue 1](https://static1.squarespace.com/static/53d7dcdce4b07a1cdbbc08a4/t/53d7e1e0e4b0ce03afb2eaa6/1406698976944/PocketQube+Standard+Issue+1.pdf), TU Delft / Alba Orbital / GAUSS Srl, 2018
- [NanoRacks NRCSD IDD Rev D](https://nanoracks.com/wp-content/uploads/Nanoracks-CubeSat-Deployer-NRCSD-IDD.pdf)
- [NanoRacks NRCSD-E IDD](https://nanoracks.com/wp-content/uploads/Nanoracks-External-Cygnus-Deployer-E-NRCSD-IDD.pdf)
- [Cal Poly P-POD Mk III User Guide](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/5806854d6b8f5b8eb57b83bd/1476822350599/P-POD_MkIIIRevE_UserGuide.pdf)
- [ISIS ISIPOD Datasheet](https://www.isispace.nl)
- [Exolaunch EXOpod Datasheet](https://exolaunch.com)
- [JAXA JEM Payload Accommodation Handbook Vol. 8](https://aerospacebiz.jaxa.jp/solution/satellite/)
- [D-Orbit ION Platform](https://www.dorbit.space)
- [Maverick Space Systems](https://maverickspace.com)

## Machine-Readable Data (JSON)

All data is shipped as JSON files in [`src/cubesat_specs/data/`](src/cubesat_specs/data/) for use from any language:

| File | Contents |
|------|----------|
| `form_factors.json` | CubeSat (0.5U–27U) and PocketQube (1p–3p) dimensions, mass, CG limits |
| `deployers.json` | All deployer specs (velocity, mass, form factors) |
| `launch_providers.json` | Provider names, websites, deployer references |
| `standards_cds.json` | CDS Rev 14.1 constraints |
| `standards_pqs.json` | PocketQube Standard Issue 1 constraints |

Regenerate with `python scripts/export_json.py`.

## Citing

If you use this data in academic work, please cite:

```bibtex
@software{cubesat_specs,
  author  = {Pinsker, Julius},
  title   = {cubesat-specs},
  url     = {https://github.com/JuliusPinsker/cubesat-specs},
  version = {0.2.1},
  year    = {2026},
}
```

A `CITATION.cff` is included — GitHub shows a "Cite this repository" button automatically.

## Contributing

PRs welcome! Priority areas:
- Additional deployers (Tyvak, GomSpace, AAC Clyde Space)
- VEGA/Ariane-6 rideshare specs
- Updated NanoRacks specs post-Voyager acquisition
- SpaceX Transporter mission orbit parameters per flight

## License

[MIT](LICENSE)
