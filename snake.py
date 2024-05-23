""" Módulo de lançamento """

# Imports de pacotes externos
from arcade import run

# Imports de pacotes locais
from game import *
from game import Properties # Adição para teste - Retirar

def main() -> None:
    """ Função Principal """

    # Cria e configura a janela
    window = GameWindow(properties = Properties(fullscreen = True)) # Alterar após testes
    window.setup()

    # inicia o loop principal
    run()

# Inicia a função principal caso este modulo esteja sendo chamado
if __name__ == "__main__":
    main()
