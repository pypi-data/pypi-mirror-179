import platform
import sys

import aiohttp

import ciberedev

commands = []


class Command:
    def __init__(self, *, name: str, description: str, full_name: str):
        self.name = name
        self.full_name = full_name
        self.description = description

    def callback(self):
        pass


class GetVersionCmd(Command):
    def __init__(self):
        super().__init__(
            name="v",
            full_name="version",
            description="gives you the version of ciberedev.py you are running",
        )

    def callback(self):
        print(f"ciberedev.py version: {ciberedev.__version__}")


class GetSystemInfoCmd(Command):
    def __init__(self):
        super().__init__(
            name="s",
            full_name="system-info",
            description="gives you info about your system",
        )

    def callback(self):
        info = {}

        info["ciberedev.py"] = ciberedev.__version__
        info["aiohttp"] = aiohttp.__version__
        info["python"] = sys.version.split(" ")[0]
        info["OS"] = platform.platform()

        nl = "\n"
        print(nl.join([f"{item}: {info[item]}" for item in info]))


class HelpCmd(Command):
    def __init__(self):
        super().__init__(name="h", description="the help menu", full_name="help")

    def callback(self):
        nl = "\n"
        print(
            f"""
ciberedev.py arguments

{nl.join(
    [
        f"-{cmd.name} | {cmd.full_name}: {cmd.description}"
        for cmd in commands
    ]
)}
"""
        )


commands.append(GetSystemInfoCmd())
commands.append(GetVersionCmd())
commands.append(HelpCmd())


def main():
    args = sys.argv

    if len(args) == 1:
        given_cmd = "h"
    elif len(args) > 2:
        return print("Too many arguments passed")
    elif not args[1].startswith("-"):
        return print("All Arguments must start with '-'")
    else:
        given_cmd = args[1].split("-")
        given_cmd.pop(0)
        given_cmd = "".join(given_cmd)

    found_cmds = [cmd for cmd in commands if cmd.name == given_cmd]
    if len(found_cmds) == 0:
        return print(f"Unknown command {given_cmd}'")
    else:
        cmd = found_cmds[0]

    cmd.callback()


if __name__ == "__main__":
    main()
