# cubesat-specs

[![PyPI version](https://badge.fury.io/py/cubesat-specs.svg)](https://pypi.org/project/cubesat-specs/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/JuliusPinsker/cubesat-specs/actions/workflows/test.yml/badge.svg)](https://github.com/JuliusPinsker/cubesat-specs/actions/workflows/test.yml)

Standardized **CubeSat** and **PocketQube** form factor specifications plus launch provider and deployer constraints — no hardcoding required.

```bash
pip install cubesat-specs
```

## Quick Start

```python
from cubesat_specs import (
    CUBESAT_FORM_FACTORS,
    POCKETQUBE_FORM_FACTORS,
    get_form_factor,
    get_compatible_providers,
)

# Look up a 3U CubeSat
ff = CUBESAT_FORM_FACTORS["3U"]
print(ff.width_mm, ff.depth_mm, ff.height_mm)  # 100.0 100.0 340.5
print(ff.max_mass_kg)                            # 6.0
print(ff.volume_liters)                          # 3.405

# PocketQube 1p
pq = POCKETQUBE_FORM_FACTORS["1p"]
print(pq.max_mass_kg)  # 0.25

# Unified lookup (CubeSat + PocketQube)
get_form_factor("6U")   # returns CubeSatFormFactor for 6U
get_form_factor("2p")   # returns CubeSatFormFactor for 2p PocketQube

# Which launch providers accept a 6U?
for provider in get_compatible_providers("6U"):
    deployer_names = [d.name for d in provider.deployers
                      if "6U" in d.supported_form_factors]
    print(f"{provider.name}: {deployer_names}")
```

## CubeSat Form Factors (Cal Poly CDS Rev 14.1)

| Key   | W × D × H (mm)          | Max mass (kg) | Min freq (Hz) |
|-------|--------------------------|---------------|---------------|
| 0.5U  | 100 × 100 × 56.75        | 1.00          | 100           |
| 1U    | 100 × 100 × 113.5        | 2.00          | 100           |
| 1.5U  | 100 × 100 × 170.25       | 3.00          | 100           |
| 2U    | 100 × 100 × 227.0        | 4.00          | 100           |
| 3U    | 100 × 100 × 340.5        | 6.00          | 100           |
| 3U+   | 100 × 100 × 360.0        | 6.00          | 100           |
| 6U    | 226.3 × 100 × 366.0      | 12.00         | 100           |
| 12U   | 226.3 × 226.3 × 366.0    | 24.00         | 100           |
| 16U   | 226.3 × 226.3 × 488.0    | 32.00         | 100           |
| 27U   | 300 × 300 × 340.5        | 54.00         | 100           |

## PocketQube Form Factors (PocketQube Standard Issue 1)

| Key | W × D × H (mm) | Max mass (g) |
|-----|-----------------|--------------|
| 1p  | 50 × 50 × 50  | 250          |
| 2p  | 50 × 50 × 114 | 500          |
| 3p  | 50 × 50 × 178 | 750          |

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

Each `DeployerSpec` carries: `supported_form_factors`, `deployment_velocity_min/max_ms`, `tip_off_rate_max_deg_s`, `max_payload_mass_kg`, and optional `inclination_deg` / `altitude_km_min/max`.

## Data Sources

- [CubeSat Design Specification (CDS) Rev 14.1](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf), Cal Poly, 2022
- [PocketQube Standard Issue 1](https://static1.squarespace.com/static/53d7dcdce4b07a1cdbbc08a4/t/5b34c395352f5303fcec6f45/1530184648111/PocketQube+Standard+issue+1+-+Published.pdf), 2018
- [NanoRacks NRCSD IDD Rev D](https://nanoracks.com/wp-content/uploads/Nanoracks-CubeSat-Deployer-NRCSD-IDD.pdf)
- [NanoRacks NRCSD-E IDD](https://nanoracks.com/wp-content/uploads/Nanoracks-External-Cygnus-Deployer-E-NRCSD-IDD.pdf)
- [Cal Poly P-POD Mk III User Guide](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/5806854d6b8f5b8eb57b83bd/1476822350599/P-POD_MkIIIRevE_UserGuide.pdf)
- [ISIS ISIPOD Datasheet](https://www.isispace.nl)
- [Exolaunch EXOpod Datasheet](https://exolaunch.com)

## Contributing

PRs welcome! Priority areas:
- Additional deployers (Tyvak, GomSpace, AAC Clyde Space, D-Orbit ION)
- VEGA/Ariane-6 rideshare specs
- Updated NanoRacks specs post-Voyager acquisition
- SpaceX Transporter mission orbit parameters per flight

## License

[MIT](LICENSE)
