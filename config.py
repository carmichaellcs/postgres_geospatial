
from dynaconf import Dynaconf

settings = Dynaconf(
  envvar_prefix="DYNACONF",
  settings_files=['settings.toml', '.secrets.toml'],
  environments=["development", "production"],
  env_switcher="DYNACONF_MODE"
)
