import os
import json
from typing import Any
from pydantic_settings import (
    BaseSettings,
    EnvSettingsSource,
    DotEnvSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)
from pydantic.fields import FieldInfo

class TupleParseMixin:
    def prepare_field_value(self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool) -> Any:
        
        if field_name == 'LISTA' and value is not None:
            return tuple(s.strip() for s in value.split(','))
            
        return value       


class MyEnvSettingsSource(TupleParseMixin, EnvSettingsSource):
    ...

class MyDotEnvSettingsSource(TupleParseMixin, DotEnvSettingsSource):
    ...   


class Settings(BaseSettings):
    SCALAR: int
    LISTA: tuple[str, ...] = ('default',)

    model_config = SettingsConfigDict(
        env_file='.env', 
        env_file_encoding='utf-8'
    )


    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """
        Define the sources and their order for loading the settings values.

        Args:
            settings_cls: The Settings class.
            init_settings: The `InitSettingsSource` instance.
            env_settings: The `EnvSettingsSource` instance.
            dotenv_settings: The `DotEnvSettingsSource` instance.
            file_secret_settings: The `SecretsSettingsSource` instance.

        Returns:
            A tuple containing the sources and their order for loading the settings values.
        """
        return (
            MyEnvSettingsSource(settings_cls),
            MyDotEnvSettingsSource(settings_cls),  
        )