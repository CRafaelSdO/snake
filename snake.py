""" Módulo de lançamento do jogo """

# Importação externa
from arcade import run

# Importação local
from game import *

def main():
    """ Função Principal """

    # Cria e configura a janela
    window = GameWindow(Properties())

    # inicia o loop principal
    run()

# Inicia a função principal caso este modulo esteja sendo chamado
if __name__ == "__main__":
    main()
