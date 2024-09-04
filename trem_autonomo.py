class TremAutonomo:
    def __init__(self):
        self.posicao = 0
        self.movimentos = 0
        self.movimentos_consecutivos = 0
        self.direcao_atual = None

    def mover(self, direcao):
        if direcao == 'DIREITA':
            self.posicao += 1
        elif direcao == 'ESQUERDA':
            self.posicao -= 1
        else:
            raise ValueError(f"Comando inválido: {direcao}")
        
        self.movimentos += 1
        self.movimentos_consecutivos += 1

    def validar_movimento(self, direcao):
        if self.movimentos >= 50:
            raise Exception("O trem já percorreu 50 posições, a viagem terminou.")
        
        if self.direcao_atual != direcao:
            self.movimentos_consecutivos = 0
        
        if self.movimentos_consecutivos >= 20:
            raise Exception(f"Movimento inválido: mais de 20 movimentos consecutivos na direção {direcao}.")
        
        self.direcao_atual = direcao

    def executar_comandos(self, comandos):
        if not comandos:
            raise ValueError("A lista de comandos não pode ser vazia.")
        
        for comando in comandos:
            self.validar_movimento(comando)
            self.mover(comando)

        return self.posicao
