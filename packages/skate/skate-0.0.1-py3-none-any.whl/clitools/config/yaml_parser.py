from pathlib import Path

import yaml
from yaml.loader import SafeLoader

from clitools.command import Command
from clitools.command_group import CommandGroup


class YamlParser:
    def __init__(self):
        pass

    def parse(self, file: Path) -> dict[str, CommandGroup]:
        """
        Read command groups from a yaml file.
        """

        with open(file, "rb") as f:
            command_groups_raw = yaml.load(f, Loader=SafeLoader)

        command_groups = {}
        for group_name, group_commands in command_groups_raw.items():
            command_groups[group_name] = CommandGroup(
                commands={name: Command(name, **command_dict) for name, command_dict in group_commands.items()}
            )

        return command_groups
