# FILEPATH: /home/jjailbird/developments/projects/templates/fastapi_production_template/tests/test_config.py

import pytest
from unittest import mock
from src.config import Config, settings, app_configs
from src.constants import Environment

def test_config_values():
    assert isinstance(settings.DATABASE_URL, str)
    assert isinstance(settings.REDIS_URL, str)
    assert settings.SITE_DOMAIN == "myapp.com"
    assert isinstance(settings.ENVIRONMENT, Environment)
    assert isinstance(settings.CORS_ORIGINS, list)
    assert isinstance(settings.CORS_HEADERS, list)
    assert settings.APP_VERSION == "1"

def test_app_configs():
    assert isinstance(app_configs, dict)
    assert app_configs["title"] == "App API"

    if settings.ENVIRONMENT.is_deployed:
        assert app_configs["root_path"] == f"/v{settings.APP_VERSION}"
    else:
        assert "root_path" not in app_configs

    if not settings.ENVIRONMENT.is_debug:
        assert app_configs["openapi_url"] is None
    else:
        assert "openapi_url" not in app_configs

@mock.patch.object(Config, 'SENTRY_DSN', None)
def test_validate_sentry_non_local():
    with pytest.raises(ValueError):
        Config.validate_sentry_non_local(settings)