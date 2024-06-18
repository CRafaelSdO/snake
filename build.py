""" Módulo de compilação """

# Imports de pacotes BuiltIn
from os import system
from os.path import join
from typing import Union

# Constantes para a build
## Variáveis do Nuitka
CACHE_DIR = "{CACHE_DIR}"
PROGRAM_BASE = "{PROGRAM_BASE}"

## Programa
PROGRAM_NAME = "Snake"
MAIN_MODULE = "snake.py"

## Recursos
RESOURCES_DIR = "resources"
ICON_FILE = "icon.png"

## Compilação
OUTPUT_DIR = "build"

## Opções de Execução
CONSOLE_MODE = "disable"
STDOUT = "out.txt"
STDERR = "err.txt"

# Srgumentos para build
ARGS: dict[str, Union[list[str], dict[str, str]]] = {
    "flags": ["--onefile", "--remove-output"],
    "options": {
        "--main": MAIN_MODULE,
        "--include-data-dir": f"{RESOURCES_DIR}={RESOURCES_DIR}",
        "--windows-icon-from-ico": join(RESOURCES_DIR, ICON_FILE),
        "--output-dir": OUTPUT_DIR,
        "--onefile-tempdir-spec": join(CACHE_DIR, PROGRAM_NAME),
        "--windows-console-mode": CONSOLE_MODE,
        "--windows-force-stdout-spec": f"{PROGRAM_BASE}-{STDOUT}",
        "--windows-force-stderr-spec": f"{PROGRAM_BASE}-{STDERR}"
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
