"""Tests for CDS Rev 14.1 and PocketQube Standard Issue 1 constraints."""
from cubesat_specs import CDS, PQS
from cubesat_specs.standards import (
    CDSConstraints,
    PQSConstraints,
    # CDS module-level constants
    RAIL_MIN_WIDTH_MM,
    OUTGASSING_TML_MAX_PCT,
    RF_SILENCE_MINUTES,
    DEPLOYABLE_WAIT_MINUTES,
    # PQS module-level constants
    PQ_MIN_KILL_SWITCHES,
    PQ_CG_MAX_OFFSET_CM,
    PQ_COMPONENT_ENVELOPE_MM,
    PQ_BACKPLATE_DIMENSIONS,
)


# --- CDS singleton ---

def test_cds_is_singleton_instance():
    assert isinstance(CDS, CDSConstraints)


def test_cds_rail_width():
    assert CDS.rail_min_width_mm == 8.5


def test_cds_outgassing():
    assert CDS.outgassing_tml_max_pct == 1.0
    assert CDS.outgassing_cvcm_max_pct == 0.1


def test_cds_rf_silence():
    assert CDS.rf_silence_minutes == 45


def test_cds_deployable_wait():
    assert CDS.deployable_wait_minutes == 30


def test_cds_deployment_switches():
    assert CDS.min_deployment_switches >= 1


def test_cds_module_constants_match():
    """Module-level constants should equal CDS singleton fields."""
    assert RAIL_MIN_WIDTH_MM == CDS.rail_min_width_mm
    assert OUTGASSING_TML_MAX_PCT == CDS.outgassing_tml_max_pct
    assert RF_SILENCE_MINUTES == CDS.rf_silence_minutes
    assert DEPLOYABLE_WAIT_MINUTES == CDS.deployable_wait_minutes


# --- PQS singleton ---

def test_pqs_is_singleton_instance():
    assert isinstance(PQS, PQSConstraints)


def test_pqs_no_pyrotechnics():
    assert PQS.pyrotechnics_allowed is False


def test_pqs_outgassing():
    assert PQS.outgassing_tml_max_pct == 1.0
    assert PQS.outgassing_cvcm_max_pct == 0.1


def test_pqs_kill_switches():
    assert PQS.min_kill_switches == 2


def test_pqs_cg_offset():
    assert PQS.cg_max_offset_cm == 1.0


def test_pqs_component_envelope():
    assert PQS.component_envelope_mm == 7.0
    assert PQS.deployable_envelope_mm == 10.0


def test_pqs_backplate_thickness():
    assert PQS.backplate_thickness_mm == 1.6


def test_pqs_mass_per_unit():
    assert PQS.mass_per_unit_kg == 0.250


def test_pqs_module_constants_match():
    """Module-level constants should equal PQS singleton fields."""
    assert PQ_MIN_KILL_SWITCHES == PQS.min_kill_switches
    assert PQ_CG_MAX_OFFSET_CM == PQS.cg_max_offset_cm
    assert PQ_COMPONENT_ENVELOPE_MM == PQS.component_envelope_mm


def test_pqs_backplate_dimensions():
    """Sliding backplate X × Z × thickness from PQ Standard Table 1."""
    assert PQ_BACKPLATE_DIMENSIONS["1p"] == (58.0, 64.0, 1.6)
    assert PQ_BACKPLATE_DIMENSIONS["2p"] == (58.0, 128.0, 1.6)
    assert PQ_BACKPLATE_DIMENSIONS["3p"] == (58.0, 192.0, 1.6)


def test_pqs_hard_anodize():
    assert PQS.hard_anodize_required is True
