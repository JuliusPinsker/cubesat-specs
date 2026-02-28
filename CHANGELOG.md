# Changelog

All notable changes to `cubesat-specs` are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.1.0] — 2026-02-28

### Added
- `CubeSatFormFactor` dataclass with dimensions, mass limits, and min. freq. properties
- `DeployerSpec` dataclass for launch vehicle deployer constraints
- `LaunchProvider` dataclass grouping deployers by provider
- CubeSat form factors: `0.5U`, `1U`, `1.5U`, `2U`, `3U`, `3U+`, `6U`, `12U`, `16U`, `27U` (Cal Poly CDS Rev 14)
- PocketQube form factors: `1p`, `2p`, `3p` (PocketQube Standard Issue 1.7)
- Launch providers: NanoRacks, Cal Poly, ISIS, Exolaunch, SpaceFlight Inc., Rocket Lab, Alba Orbital
- `get_form_factor(key)` — unified lookup across CubeSat & PocketQube dicts
- `get_compatible_providers(key)` — filter providers by supported form factor
- Volume and mass density computed properties on `CubeSatFormFactor`
- Full test suite (pytest)
- GitHub Actions CI (test matrix Python 3.9–3.12)
- GitHub Actions publish workflow (trusted PyPI publishing via OIDC)
