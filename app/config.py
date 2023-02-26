from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["configs/settings.toml"],
    secrets=["configs/.secrets.toml"],
    environments=True,
)
