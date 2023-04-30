import os
import yaml
import pytest
from pathlib import Path
from ..config import load_config, setup_environment_variables

def test_load_config_valid_file():
    config = load_config()
    assert isinstance(config, dict), "Configuration should be a dictionary"
    assert "OpenAI" in config, "OpenAI settings should be present in the configuration"
    assert "chatbot" in config, "Chatbot settings should be present in the configuration"

def test_load_config():
    config = load_config()

    assert isinstance(config, dict), "Loaded configuration should be a dictionary"
    assert "Key_File" in config, "Key_File should be present in the configuration"
    assert "chatbot" in config, "chatbot should be present in the configuration"
    assert "name" in config["chatbot"], "name should be present in the chatbot configuration"

def test_setup_environment_variables(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "dummy_openai_key")
    monkeypatch.setenv("SERPAPI_API_KEY", "dummy_serpapi_key")

    config = load_config()
    setup_environment_variables(config)

    assert 'OPENAI_API_KEY' in os.environ, "OPENAI_API_KEY should be in environment variables"
    assert 'SERPAPI_API_KEY' in os.environ, "SERPAPI_API_KEY should be in environment variables"

