"""Dataclass models for CubeSat form factors, deployers, and launch providers."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class CubeSatFormFactor:
    """Standard CubeSat or PocketQube form factor specification.

    Dimensions follow the respective design standards:
    - CubeSat:    Cal Poly CubeSat Design Specification (CDS) Rev 14.1
    - PocketQube: PocketQube Standard Issue 1
    """

    name: str
    """Human-readable name, e.g. '1U CubeSat' or '1p PocketQube'."""
    units: float
    """Number of CubeSat Units (U) or PocketQube units (p)."""
    width_mm: float
    """Outer envelope width [mm] (X-axis)."""
    depth_mm: float
    """Outer envelope depth [mm] (Y-axis)."""
    height_mm: float
    """Outer envelope height [mm] (Z-axis / deployment axis)."""
    min_mass_kg: float
    """Practical minimum populated spacecraft mass [kg]."""
    typical_mass_kg: float
    """Typical populated spacecraft mass [kg]."""
    max_mass_kg: float
    """Maximum allowed mass per the standard [kg]."""
    min_freq_hz: float
    """Minimum required fundamental frequency [Hz] for launch qualification."""

    # ------------------------------------------------------------------
    # Computed properties
    # ------------------------------------------------------------------

    @property
    def volume_cm3(self) -> float:
        """Outer envelope volume [cm³]."""
        return (self.width_mm / 10.0) * (self.depth_mm / 10.0) * (self.height_mm / 10.0)

    @property
    def volume_liters(self) -> float:
        """Outer envelope volume [L]."""
        return self.volume_cm3 / 1000.0

    @property
    def mass_density_max_kg_per_liter(self) -> float:
        """Maximum allowable mass density [kg/L] (max_mass / volume)."""
        return self.max_mass_kg / self.volume_liters if self.volume_liters > 0 else 0.0

    def is_same_cross_section(self, other: CubeSatFormFactor, tol_mm: float = 1.0) -> bool:
        """True if both form factors share the same cross-sectional footprint (±tol_mm)."""
        return (
            abs(self.width_mm - other.width_mm) <= tol_mm
            and abs(self.depth_mm - other.depth_mm) <= tol_mm
        )

    def __repr__(self) -> str:  # noqa: D105
        return (
            f"CubeSatFormFactor({self.name!r}, "
            f"{self.width_mm}×{self.depth_mm}×{self.height_mm} mm, "
            f"max {self.max_mass_kg} kg)"
        )


@dataclass(frozen=True)
class DeployerSpec:
    """Specification for a CubeSat deployment system (P-POD, NRCSD, ISIPOD, …)."""

    name: str
    """Deployer product name."""
    provider: str
    """Company or organisation providing the deployer."""
    max_units: float
    """Maximum total CubeSat units (U) the deployer can accommodate."""
    supported_form_factors: List[str]
    """Form factor keys accepted by this deployer, e.g. ['1U', '2U', '3U']."""
    deployment_velocity_min_ms: float
    """Minimum ejection velocity [m/s]."""
    deployment_velocity_max_ms: float
    """Maximum ejection velocity [m/s]."""
    tip_off_rate_max_deg_s: float
    """Maximum tip-off angular rate [deg/s] per axis at ejection."""
    max_payload_mass_kg: float
    """Maximum total payload mass that can be loaded into the deployer [kg]."""
    mechanism: str = "spring"
    """Ejection mechanism type ('spring', 'pneumatic', 'electromagnetic')."""
    inclination_deg: Optional[float] = None
    """Typical orbital inclination [deg] if this deployer is orbit-specific."""
    altitude_km_min: Optional[float] = None
    """Typical minimum deployment altitude [km] (None = mission-specific)."""
    altitude_km_max: Optional[float] = None
    """Typical maximum deployment altitude [km] (None = mission-specific)."""
    notes: str = ""
    """Additional constraints or remarks."""


@dataclass
class LaunchProvider:
    """A launch service provider offering CubeSat deployment services."""

    name: str
    """Provider name."""
    website: str
    """Official website URL."""
    deployers: List[DeployerSpec] = field(default_factory=list)
    """Deployer systems offered by this provider."""
    notes: str = ""
    """Additional notes."""
