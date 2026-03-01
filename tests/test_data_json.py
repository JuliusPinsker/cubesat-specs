"""Tests for JSON data files and data-loading helpers."""
import json
import pathlib

import pytest
from cubesat_specs import data_path, load_json


def test_data_path_exists():
    assert data_path().is_dir()


def test_data_path_has_json_files():
    files = sorted(p.name for p in data_path().glob("*.json"))
    assert "form_factors.json" in files
    assert "deployers.json" in files
    assert "launch_providers.json" in files
    assert "standards_cds.json" in files
    assert "standards_pqs.json" in files


@pytest.mark.parametrize("name", [
    "form_factors.json",
    "deployers.json",
    "launch_providers.json",
    "standards_cds.json",
    "standards_pqs.json",
])
def test_load_json_valid(name):
    data = load_json(name)
    assert isinstance(data, dict)
    assert "version" in data or "$schema" in data


def test_load_json_missing_raises():
    with pytest.raises(FileNotFoundError, match="No data file"):
        load_json("nonexistent.json")


# -- form_factors.json structure ----------------------------------------

def test_form_factors_json_has_cubesat_keys():
    data = load_json("form_factors.json")
    cs = data["cubesat"]
    for key in ["1U", "3U", "6U", "12U"]:
        assert key in cs
        assert cs[key]["max_mass_kg"] > 0


def test_form_factors_json_has_pocketqube_keys():
    data = load_json("form_factors.json")
    pq = data["pocketqube"]
    for key in ["1p", "2p", "3p"]:
        assert key in pq


# -- deployers.json structure -------------------------------------------

def test_deployers_json_non_empty():
    data = load_json("deployers.json")
    deployers = data["deployers"]
    assert len(deployers) >= 10


def test_deployers_json_has_required_fields():
    data = load_json("deployers.json")
    for name, d in data["deployers"].items():
        assert "max_payload_mass_kg" in d, f"{name} missing mass"
        assert "supported_form_factors" in d, f"{name} missing form factors"


# -- launch_providers.json structure ------------------------------------

def test_launch_providers_json_has_all_keys():
    data = load_json("launch_providers.json")
    providers = data["providers"]
    for key in ["nanoracks", "calpoly", "isis", "exolaunch", "jaxa", "dorbit", "maverick"]:
        assert key in providers


# -- standards_cds.json structure ---------------------------------------

def test_standards_cds_json():
    data = load_json("standards_cds.json")
    c = data["constraints"]
    assert c["rf_silence_minutes"] == 45
    assert c["outgassing_tml_max_pct"] == 1.0


# -- standards_pqs.json structure ---------------------------------------

def test_standards_pqs_json():
    data = load_json("standards_pqs.json")
    c = data["constraints"]
    assert c["min_kill_switches"] == 2
    assert c["pyrotechnics_allowed"] is False
