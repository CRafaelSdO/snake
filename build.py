""" Módulo de compilação """

# Imports de pacotes BuiltIn
from os import system
from os.path import join
from typing import Union

# Constantes para a build
MAIN_MODULE = "snake.py"
RESOURCES_DIR = "resources"
ICON_FILE = "icon.png"
STDOUT = "{PROGRAM_BASE}-output.txt"
STDERR = "{PROGRAM_BASE}-logs.txt"
CONSOLE_MODE = "disable"
TEMP_DIR = join("{TEMP}", "snake")
OUTPUT_DIR = "build"

# Srgumentos para build
ARGS: dict[str, Union[list[str], dict[str, str]]] = {
    "flags": [MAIN_MODULE, "--onefile", "--remove-output"],
    "options": {
        "--windows-icon-from-ico": join(RESOURCES_DIR, ICON_FILE),
        "--include-data-dir": f"{RESOURCES_DIR}={RESOURCES_DIR}",
        "--output-dir": OUTPUT_DIR,
        "--onefile-tempdir-spec": TEMP_DIR,
        "--windows-console-mode": CONSOLE_MODE,
        "--windows-force-stdout-spec": STDOUT,
        "--windows-force-stderr-spec": STDERR
    }
}

def main() -> None:
    """ Função Principal """

    comand = "python -m nuitka"

    for flag in ARGS["flags"]:
        comand += f" {flag}"

    for option in ARGS["options"]:
        comand += f" {option}={ARGS['options'][option]}"

    system(comand)

# Inicia a função principal caso este modulo esteja sendo executado
if __name__ == "__main__":
    main()
