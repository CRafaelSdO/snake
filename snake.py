""" Módulo de lançamento """

# Imports de pacotes BuiltIn
from os.path import dirname

# Imports de pacotes externos
from arcade import run

# Imports de pacotes locais
from game import *

def main() -> None:
    """ Função Principal """

    # Cria e configura a janela
    window = GameWindow(dirname(__file__))
    window.setup()

    # inicia o loop principal
    run()

# Inicia a função principal caso este modulo esteja sendo executado
if __name__ == "__main__":
    main()
