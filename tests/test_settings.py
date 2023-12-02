import os

import pytest
from pydantic_core import ValidationError

from src.config import Settings


def test_positive_env_scalar_required():

    os.environ['SCALAR'] = "1"

    settings = Settings()

    assert settings.SCALAR == 1

    del os.environ['SCALAR']
    

def test_negative_env_with_scalar_must_return_error():

    with pytest.raises(ValidationError):
        settings = Settings()


def test_positive_env_scalar_and_tuple():

    os.environ['SCALAR'] = "2"
    os.environ['LISTA'] = "abc,def,ghi"

    settings = Settings()

    assert settings.SCALAR == 2
    assert settings.LISTA == ("abc","def","ghi",)

    del os.environ['SCALAR']
    del os.environ['LISTA']


def test_positive_dotenv_scalar():
    Settings.model_config['env_file']="tests/env_files/env_only_scalar"
    settings = Settings()

    assert settings.SCALAR == 3


def test_positive_dotenv_scalar_and_tuple():
    Settings.model_config['env_file']="tests/env_files/env_scalar_tuple"
    settings = Settings()

    assert settings.SCALAR == 3
    assert settings.LISTA == ("abc", "def", "ghi",)


def test_positive_env_precedes_dotenv():
    
    os.environ['SCALAR'] = "44"

    Settings.model_config['env_file'] = "tests/env_files/env_scalar_tuple"
    settings = Settings()

    assert settings.SCALAR == 44
    assert settings.LISTA == ("abc", "def", "ghi",)

    del os.environ['SCALAR']
