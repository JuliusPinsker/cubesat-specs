# Changelog

All notable changes to `cubesat-specs` are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.2.0] — 2026-02-28

### Breaking Changes
- **Renamed** `CubeSatFormFactor` → `FormFactor`
- **Removed** `min_freq_hz` — CDS Rev 14.1 does not specify a minimum natural frequency; all vibration test levels are delegated to the Launch Provider (§3.1.1)
- **Removed** `min_mass_kg` and `typical_mass_kg` — not defined in any standard
- `DeployerSpec.deployment_velocity_min_ms`, `deployment_velocity_max_ms`, and
  `tip_off_rate_max_deg_s` are now `Optional[float]` (many specs are proprietary)

### Added
- `FormFactor` — unified model for CubeSat and PocketQube form factors
- `CenterOfGravityLimits` dataclass with `within()` method for CG validation
- CG limits for all CDS form factors from Rev 14.1 Table 2 (1U–12U)
- PocketQube CG limit ±1 cm on all axes (PQ-Mass-04)
- `standards` module with **all** CDS Rev 14.1 quantitative constraints:
  rail dimensions, outgassing, magnetic field, RF/deployable inhibits,
  operational timers, battery guideline, separation spring specs, etc.
- `CDS` singleton (`CDSConstraints`) — every CDS Rev 14.1 constraint in one object
- `PQS` singleton (`PQSConstraints`) — every PocketQube Standard Issue 1 constraint:
  kill switches (≥2), component envelope (7 mm / 10 mm waiver), sliding backplate
  dimensions, recommended materials, hard-anodize requirement, outgassing limits
- Sliding backplate dimensions per form factor (`PQ_BACKPLATE_DIMENSIONS`)
- **JAXA J-SSOD** deployer — ISS Kibo-based deployment with full constraints
  (velocity 1.1–1.7 m/s, ≥3 inhibits, min freq ≥100 Hz, 30-min post-eject delay)
- **D-Orbit ION** Satellite Carrier — OTV with ~48U capacity, custom orbit insertion
- **Maverick Space Systems Mercury-3/6/12** deployers — NASA GEVS-qualified dispensers
- Launch providers: `jaxa`, `dorbit`, `maverick`
- All individual deployer constants exported from top-level package
- Comprehensive test suite for standards, CG limits, form factors, and all providers

### Changed
- PocketQube docstrings corrected: Z-axis heights follow Table 1 "External
  dimensions without backplate" (114 mm for 2p, 178 mm for 3p)

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
