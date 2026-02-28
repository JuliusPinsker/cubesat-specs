# Changelog

All notable changes to `cubesat-specs` are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.1.1] — 2026-02-28

### Changed
- Removed internal publishing instructions from README

## [0.1.0] — 2026-02-28

### Added
- `CubeSatFormFactor` dataclass with dimensions, mass limits, and min. freq. properties
- `DeployerSpec` dataclass for launch vehicle deployer constraints
- `LaunchProvider` dataclass grouping deployers by provider
- CubeSat form factors: `0.5U`, `1U`, `1.5U`, `2U`, `3U`, `3U+`, `6U`, `12U`, `16U`, `27U` (Cal Poly CDS Rev 14.1)
- PocketQube form factors: `1p`, `2p`, `3p` (PocketQube Standard Issue 1)
- Launch providers: NanoRacks, Cal Poly, ISIS, Exolaunch, SpaceFlight Inc., Rocket Lab, Alba Orbital
- `get_form_factor(key)` — unified lookup across CubeSat & PocketQube dicts
- `get_compatible_providers(key)` — filter providers by supported form factor
- Volume and mass density computed properties on `CubeSatFormFactor`
- Full test suite (pytest)
- GitHub Actions CI (test matrix Python 3.9–3.12)
- GitHub Actions publish workflow (trusted PyPI publishing via OIDC)

### Data Sources
- CubeSat mass limits updated to CDS Rev 14.1 (2022): 2.0 kg/U (was 1.33 kg/U)
- PocketQube 2p/3p Z-heights corrected to 114/178 mm per standard (incl. backplate)
- P-POD deployment velocity corrected to 1.5–2.0 m/s per User Guide Rev E
- NRCSD-E velocity corrected to 0.5–2.0 m/s; altitude to ~450 km post-ISS
- NRCSD battery limit corrected to 100 Wh (FAA requirement)
- ISIPOD 3U max payload corrected to 6 kg per ISIS brochure
- EXOpod tip-off corrected to <10 deg/s per EXOpod User Manual
