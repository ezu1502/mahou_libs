import os
from .bocca_setup import _master_log
from .bocca_main import add_level, BoccaFiglia


__version__ = "0.1.0"

BOCCA_HIDE_GREETING = os.getenv("BOCCA_HIDE_GREETING", "0")

if BOCCA_HIDE_GREETING == "0":
    print(f"\nWelcome to Bocca {__version__}, the True Logger -- Powered by Mahou Libs\n")

    
def configure_default_settings():
    _master_log.configure()

def set_core_level(level):
    _master_log.set_root_level(level)