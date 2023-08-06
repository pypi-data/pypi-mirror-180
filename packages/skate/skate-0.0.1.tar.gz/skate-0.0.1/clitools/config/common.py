import os
from pathlib import Path


def get_global_commands_file_path() -> Path:
    home = Path(os.environ["CLITOOLS_HOME"]) if "CLITOOLS_HOME" in os.environ else Path.home()
    return home / "clitools" / "commands.yaml"
