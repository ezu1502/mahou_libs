import os
from .bocca_setup import master_log
from .bocca_main import add_level, BoccaFiglia


__version__ = "0.1.0"

BOCCA_HIDE_GREETING = os.getenv("BOCCA_HIDE_GREETING", "0")

if BOCCA_HIDE_GREETING == "0":
    print(f"Welcome to Bocca {__version__}, the True Logger -- Powered by Mahou Libs")