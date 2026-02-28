"""Constants and constraints from the CubeSat Design Specification (CDS) Rev 14.1.

Every value in this module is directly traceable to the CDS Rev 14.1
(CP-CDS-R14.1, Cal Poly SLO, February 2022).  Section references are
given as ``§X.Y.Z``.

Source
------
https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/
t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

# ── Rail & Mechanical Interface (§2.2) ─────────────────────────────────────

RAIL_MIN_WIDTH_MM: float = 8.5
"""Minimum rail width measured from edge of rail to first protrusion [mm] (§2.2.5)."""

RAIL_SURFACE_ROUGHNESS_MAX_UM: float = 1.6
"""Recommended maximum rail surface roughness Ra [µm] (§2.2.6)."""

RAIL_EDGE_RADIUS_MIN_MM: float = 1.0
"""Minimum radius on rail edges [mm] (§2.2.7)."""

RAIL_END_CONTACT_AREA_MIN_MM: Tuple[float, float] = (6.5, 6.5)
"""Minimum rail end contact area on ±Z faces [mm × mm] (§2.2.8)."""

RAIL_CONTACT_PCT_MIN: float = 75.0
"""Minimum percentage of rail length in contact with dispenser rails [%] (§2.2.9).
Up to 25 % may be recessed."""

MAX_PROTRUSION_MM: float = 6.5
"""Maximum protrusion of any component from the rail plane [mm] (§2.2.3)."""

RBF_MAX_PROTRUSION_MM: float = 6.5
"""Maximum RBF-pin protrusion from rail surface when inserted [mm] (§2.3.5.2)."""

RECOMMENDED_AL_ALLOYS: Tuple[str, ...] = (
    "7075", "6061", "6082", "5005", "5052",
)
"""Aluminium alloys recommended for CubeSat structure and rails (§2.2.12.1)."""

HARD_ANODIZE_REQUIRED: bool = True
"""All aluminium surfaces in contact with dispenser rails shall be hard
anodized to prevent cold welding (§2.2.13)."""

# ── Separation Mechanism (§2.2.14) ─────────────────────────────────────────

SEPARATION_SPRING_MAX_FORCE_N: float = 6.7
"""Maximum recommended separation spring force [N] (1.5 lbf) (§2.2.14.1)."""

SEPARATION_SPRING_MIN_STROKE_MM: float = 2.5
"""Minimum recommended separation spring stroke [mm] (0.1 in) (§2.2.14.1)."""

# ── Outgassing (§2.1.7) ───────────────────────────────────────────────────

OUTGASSING_TML_MAX_PCT: float = 1.0
"""Maximum Total Mass Loss [%] (§2.1.7.1)."""

OUTGASSING_CVCM_MAX_PCT: float = 0.1
"""Maximum Collected Volatile Condensable Material [%] (§2.1.7.2)."""

# ── Magnetic Field (§2.1.8) ────────────────────────────────────────────────

MAGNETIC_FIELD_MAX_GAUSS_ABOVE_EARTH: float = 0.5
"""Maximum residual magnetic field above Earth's ambient [Gauss] (§2.1.8)."""

# ── Venting (§2.1.9) ──────────────────────────────────────────────────────

ASCENT_VENT_RATIO_MAX_M: float = 50.8
"""Maximum ventable-volume / vent-area ratio [m] (2 000 in) (§2.1.9)."""

# ── Electrical Safety (§2.3) ──────────────────────────────────────────────

MIN_DEPLOYMENT_SWITCHES: int = 1
"""Minimum number of deployment switches (§2.3.2)."""

RF_INHIBIT_COUNT: int = 3
"""Minimum independent RF-transmission inhibits (§2.3.7)."""

DEPLOYABLE_INHIBIT_COUNT: int = 3
"""Minimum independent inhibits for deployable structures (§2.3.8)."""

PROPULSION_INHIBIT_COUNT: int = 3
"""Minimum independent inhibits for propulsion activation (§2.1.4)."""

# ── Real-Time Clock (§2.3.3) ──────────────────────────────────────────────

RTC_MAX_FREQ_KHZ: float = 320.0
"""Maximum RTC oscillator frequency [kHz] (§2.3.3.2)."""

RTC_MAX_CURRENT_MA: float = 10.0
"""Maximum RTC circuit current draw [mA] (§2.3.3.3)."""

# ── Operational Timers (§2.4) ─────────────────────────────────────────────

DEPLOYABLE_WAIT_MINUTES: int = 30
"""Minimum wait time before deploying booms/antennas/panels after
deployment-switch activation [minutes] (§2.4.4)."""

RF_SILENCE_MINUTES: int = 45
"""Minimum wait time before first RF transmission after on-orbit
deployment [minutes] (§2.4.5)."""

# ── Battery Guideline (§2.1.5) ────────────────────────────────────────────

BATTERY_FAA_GUIDELINE_WH: float = 100.0
"""FAA carry-on lithium-ion battery limit used as guideline [Wh] (§2.1.5).
This is a *recommendation*, not a hard CDS requirement."""

# ── Orbital Debris (§2.4.3) ───────────────────────────────────────────────

REENTRY_ENERGY_MAX_J: float = 15.0
"""Maximum re-entry kinetic energy per component [J] (§2.4.3.1)."""

# ── Pyrotechnics (§2.1.2 / §2.1.3) ───────────────────────────────────────

PYROTECHNICS_STANDARD: str = "AFSPCMAN 91-710 Vol. 3"
"""Pyrotechnics and propulsion systems shall conform to this standard."""

# ── Testing Philosophy (§3) ───────────────────────────────────────────────
# CDS Rev 14.1 does NOT specify vibration levels, shock levels, thermal-
# vacuum profiles, or a minimum natural frequency.  All test levels and
# durations are delegated to the Launch Provider (§3.1.1, §3.2.2, §3.3.1).
# When the LV environment is unknown, GSFC-STD-7000A (GEVS) and
# SMC-S-016 may be used as *guides* — but their levels are "not guaranteed
# to encompass or satisfy all LV testing environments" (§3, para 2).

VIBRATION_NOTE: str = (
    "CDS Rev 14.1 §3.1.1: random vibration levels are defined by the "
    "Launch Provider.  No default levels are specified in the CDS.  "
    "GSFC-STD-7000A (GEVS) and SMC-S-016 may be used as guides."
)

SHOCK_NOTE: str = (
    "CDS Rev 14.1 §3.3.1.1: shock testing is typically not required "
    "for CubeSats."
)


# ── Convenience aggregate ─────────────────────────────────────────────────

@dataclass(frozen=True)
class CDSConstraints:
    """All CDS Rev 14.1 constraints collected in a single object.

    This is a convenience wrapper that mirrors the module-level constants.
    """

    # Mechanical
    rail_min_width_mm: float = RAIL_MIN_WIDTH_MM
    rail_surface_roughness_max_um: float = RAIL_SURFACE_ROUGHNESS_MAX_UM
    rail_edge_radius_min_mm: float = RAIL_EDGE_RADIUS_MIN_MM
    rail_end_contact_area_min_mm: Tuple[float, float] = RAIL_END_CONTACT_AREA_MIN_MM
    rail_contact_pct_min: float = RAIL_CONTACT_PCT_MIN
    max_protrusion_mm: float = MAX_PROTRUSION_MM
    rbf_max_protrusion_mm: float = RBF_MAX_PROTRUSION_MM
    separation_spring_max_force_n: float = SEPARATION_SPRING_MAX_FORCE_N
    separation_spring_min_stroke_mm: float = SEPARATION_SPRING_MIN_STROKE_MM

    # Outgassing
    outgassing_tml_max_pct: float = OUTGASSING_TML_MAX_PCT
    outgassing_cvcm_max_pct: float = OUTGASSING_CVCM_MAX_PCT

    # Magnetic
    magnetic_field_max_gauss: float = MAGNETIC_FIELD_MAX_GAUSS_ABOVE_EARTH

    # Electrical
    min_deployment_switches: int = MIN_DEPLOYMENT_SWITCHES
    rf_inhibit_count: int = RF_INHIBIT_COUNT
    deployable_inhibit_count: int = DEPLOYABLE_INHIBIT_COUNT
    propulsion_inhibit_count: int = PROPULSION_INHIBIT_COUNT
    rtc_max_freq_khz: float = RTC_MAX_FREQ_KHZ
    rtc_max_current_ma: float = RTC_MAX_CURRENT_MA

    # Operational timers
    deployable_wait_minutes: int = DEPLOYABLE_WAIT_MINUTES
    rf_silence_minutes: int = RF_SILENCE_MINUTES

    # Battery
    battery_faa_guideline_wh: float = BATTERY_FAA_GUIDELINE_WH

    # Debris
    reentry_energy_max_j: float = REENTRY_ENERGY_MAX_J


CDS = CDSConstraints()
"""Singleton instance of all CDS Rev 14.1 constraints."""


# ═══════════════════════════════════════════════════════════════════════════
# PocketQube Standard Issue 1  (7 June 2018)
# ═══════════════════════════════════════════════════════════════════════════
# Contributors: TU Delft, Alba Orbital, GAUSS Srl
# Source: https://static1.squarespace.com/static/53d7dcdce4b07a1cdbbc08a4/
# t/5b34c395352f5303fcec6f45/1530184648111/PocketQube+Standard+issue+1+-+Published.pdf

# ── General (§2.1) ────────────────────────────────────────────────────────

PQ_PYROTECHNICS_ALLOWED: bool = False
"""PQ-Gen-02: Pyrotechnics shall not be allowed on board."""

PQ_OUTGASSING_TML_MAX_PCT: float = 1.0
"""PQ-Gen-04: Maximum Total Mass Loss [%] (per ECSS-Q-70-02C)."""

PQ_OUTGASSING_CVCM_MAX_PCT: float = 0.1
"""PQ-Gen-04: Maximum Collected Volatile Condensable Material [%]."""

# ── Mechanical (§2.2) ─────────────────────────────────────────────────────

PQ_COMPONENT_ENVELOPE_MM: float = 7.0
"""PQ-Mech-08: Maximum protrusion for components [mm]."""

PQ_DEPLOYABLE_ENVELOPE_MM: float = 10.0
"""PQ-Mech-08: Maximum protrusion for deployables (requires waiver) [mm]."""

PQ_RAIL_CLAMP_WIDTH_MM: float = 2.0
"""PQ-Mech-07: Rail clamping width on each side of sliding backplate [mm]."""

PQ_MIN_CONTACT_SURFACE_MM: float = 21.5
"""PQ-Mech-10: Minimum contact surface from both sides on Z+ axis [mm]."""

PQ_MIN_KILL_SWITCHES: int = 2
"""PQ-Mech-12: Minimum number of kill switches."""

PQ_BACKPLATE_THICKNESS_MM: float = 1.6
"""Sliding backplate thickness [mm] (Table 1, all sizes)."""

PQ_BACKPLATE_DIMENSIONS: Dict[str, Tuple[float, float, float]] = {
    "1p": (58.0, 64.0, 1.6),
    "2p": (58.0, 128.0, 1.6),
    "3p": (58.0, 192.0, 1.6),
}
"""Sliding backplate (X × Z × thickness) per form factor [mm] (Table 1)."""

# ── Mass (§2.2.2) ─────────────────────────────────────────────────────────

PQ_MASS_PER_UNIT_KG: float = 0.250
"""PQ-Mass-01: Maximum mass per 1P unit [kg]."""

PQ_CG_MAX_OFFSET_CM: float = 1.0
"""PQ-Mass-04: Max CG offset from geometric centre [cm] (all axes)."""

# ── Materials (§2.2.3) ────────────────────────────────────────────────────

PQ_RECOMMENDED_BASEPLATE_MATERIALS: Tuple[str, ...] = (
    "FR4", "Al-7075", "Al-6061", "Al-6065", "Al-6082",
)
"""PQ-Mat-02: Recommended baseplate materials."""

PQ_HARD_ANODIZE_REQUIRED: bool = True
"""PQ-Mat-03: Metallic deployer-contact surfaces shall be hard anodized."""


# ── Convenience aggregate ─────────────────────────────────────────────────

@dataclass(frozen=True)
class PQSConstraints:
    """All PocketQube Standard Issue 1 constraints collected in a single object."""

    # General
    pyrotechnics_allowed: bool = PQ_PYROTECHNICS_ALLOWED
    outgassing_tml_max_pct: float = PQ_OUTGASSING_TML_MAX_PCT
    outgassing_cvcm_max_pct: float = PQ_OUTGASSING_CVCM_MAX_PCT

    # Mechanical
    component_envelope_mm: float = PQ_COMPONENT_ENVELOPE_MM
    deployable_envelope_mm: float = PQ_DEPLOYABLE_ENVELOPE_MM
    rail_clamp_width_mm: float = PQ_RAIL_CLAMP_WIDTH_MM
    min_contact_surface_mm: float = PQ_MIN_CONTACT_SURFACE_MM
    min_kill_switches: int = PQ_MIN_KILL_SWITCHES
    backplate_thickness_mm: float = PQ_BACKPLATE_THICKNESS_MM

    # Mass
    mass_per_unit_kg: float = PQ_MASS_PER_UNIT_KG
    cg_max_offset_cm: float = PQ_CG_MAX_OFFSET_CM

    # Materials
    hard_anodize_required: bool = PQ_HARD_ANODIZE_REQUIRED


PQS = PQSConstraints()
"""Singleton instance of all PocketQube Standard Issue 1 constraints."""
