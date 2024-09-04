from trem_autonomo import TremAutonomo

def main():
    comandos = ['DIREITA', 'DIREITA', 'ESQUERDA', 'DIREITA', 'DIREITA', 'DIREITA']

    trem = TremAutonomo()

    try:
        posicao_final = trem.executar_comandos(comandos)
        print(f"Posição final do trem: {posicao_final}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
