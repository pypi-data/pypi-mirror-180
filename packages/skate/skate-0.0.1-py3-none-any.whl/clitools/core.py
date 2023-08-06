from __future__ import annotations

from dataclasses import dataclass

from clitools.config.config_loader import ConfigLoader
from clitools.screens.pick_command import CommandPicker
from clitools.screens.pick_group import GroupPicker


@dataclass
class Core:
    def run(self):
        command_group_master = ConfigLoader().load()

        all_command_group_names = command_group_master._get_command_group_names()

        local_or_global, command_group_name = GroupPicker(
            all_command_group_names, "Please choose a command group."
        ).start()

        command_group = command_group_master.get(local_or_global)[command_group_name]
        choice, index = CommandPicker(list(command_group.get_command_names()), "Please choose a command.").start()

        command_group.get_command(choice).run()
