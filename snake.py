""" Módulo de lançamento """

# Imports de pacotes externos
from arcade import run

# Imports de pacotes locais
from game import *

def main() -> None:
    """ Função Principal """

    # Cria e configura a janela
    window = GameWindow()

    # inicia o loop principal
    run()

# Inicia a função principal caso este modulo esteja sendo chamado
if __name__ == "__main__":
    main()
