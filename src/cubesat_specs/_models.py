"""Dataclass models for satellite form factors, deployers, and launch providers."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass(frozen=True)
class CenterOfGravityLimits:
    """Acceptable centre-of-gravity offset from the geometric centre.

    Values are expressed as *±cm* on each axis.

    - CubeSat: per-form-factor limits from CDS Rev 14.1 Table 2.
    - PocketQube: ±1 cm on all axes (PQ-Mass-04).
    - ``None`` means no specified limit for that axis.
    """

    x_pm_cm: Optional[float] = None
    """Max CG offset from geometric centre on X-axis [±cm]."""
    y_pm_cm: Optional[float] = None
    """Max CG offset from geometric centre on Y-axis [±cm]."""
    z_pm_cm: Optional[float] = None
    """Max CG offset from geometric centre on Z-axis [±cm]."""

    def within(self, x_cm: float, y_cm: float, z_cm: float) -> bool:
        """Return True if the given CG offset is within all limits."""
        if self.x_pm_cm is not None and abs(x_cm) > self.x_pm_cm:
            return False
        if self.y_pm_cm is not None and abs(y_cm) > self.y_pm_cm:
            return False
        if self.z_pm_cm is not None and abs(z_cm) > self.z_pm_cm:
            return False
        return True


@dataclass(frozen=True)
class FormFactor:
    """Standard satellite form factor specification.

    Covers both CubeSat (Cal Poly CDS Rev 14.1) and PocketQube
    (PocketQube Standard Issue 1) with a unified interface.

    .. versionadded:: 0.2.0
       Renamed from ``CubeSatFormFactor``.
    .. versionchanged:: 0.2.0
       ``min_freq_hz`` removed — the CDS does **not** specify a minimum
       natural frequency (§3.1.1).  Added ``cg_limits``.
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
    max_mass_kg: float
    """Maximum allowed mass per the standard [kg] (CDS Rev 14.1 Table 1)."""
    cg_limits: CenterOfGravityLimits = CenterOfGravityLimits()
    """Centre-of-gravity limits (CDS Table 2 for CubeSats, PQ-Mass-04 for PocketQubes)."""

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

    def is_same_cross_section(self, other: FormFactor, tol_mm: float = 1.0) -> bool:
        """True if both form factors share the same cross-sectional footprint (±tol_mm)."""
        return (
            abs(self.width_mm - other.width_mm) <= tol_mm
            and abs(self.depth_mm - other.depth_mm) <= tol_mm
        )

    def __repr__(self) -> str:  # noqa: D105
        return (
            f"FormFactor({self.name!r}, "
            f"{self.width_mm}×{self.depth_mm}×{self.height_mm} mm, "
            f"max {self.max_mass_kg} kg)"
        )


@dataclass(frozen=True)
class DeployerSpec:
    """Specification for a CubeSat deployment system (P-POD, NRCSD, ISIPOD, …).

    .. versionchanged:: 0.2.0
       ``deployment_velocity_min_ms``, ``deployment_velocity_max_ms``, and
       ``tip_off_rate_max_deg_s`` are now ``Optional[float]``; many commercial
       deployer specs are proprietary and these fields may be ``None``.
    """

    name: str
    """Deployer product name."""
    provider: str
    """Company or organisation providing the deployer."""
    max_units: float
    """Maximum total CubeSat units (U) the deployer can accommodate."""
    supported_form_factors: List[str]
    """Form factor keys accepted by this deployer, e.g. ['1U', '2U', '3U']."""
    max_payload_mass_kg: float
    """Maximum total payload mass that can be loaded into the deployer [kg]."""
    deployment_velocity_min_ms: Optional[float] = None
    """Minimum ejection velocity [m/s] (None = not publicly specified)."""
    deployment_velocity_max_ms: Optional[float] = None
    """Maximum ejection velocity [m/s] (None = not publicly specified)."""
    tip_off_rate_max_deg_s: Optional[float] = None
    """Maximum tip-off angular rate [deg/s] per axis (None = not publicly specified)."""
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
