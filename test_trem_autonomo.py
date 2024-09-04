import unittest

from trem_autonomo import TremAutonomo

class TestTremAutonomo(unittest.TestCase):

    def test_movimento_direita(self):
        trem = TremAutonomo()
        posicao_final = trem.executar_comandos(['DIREITA', 'DIREITA'])
        self.assertEqual(posicao_final, 2)

    def test_movimento_esquerda(self):
        trem = TremAutonomo()
        posicao_final = trem.executar_comandos(['ESQUERDA'])
        self.assertEqual(posicao_final, -1)

    def test_movimento_misto(self):
        trem = TremAutonomo()
        posicao_final = trem.executar_comandos(['ESQUERDA', 'DIREITA', 'DIREITA'])
        self.assertEqual(posicao_final, 1)

    def test_lista_comandos_vazia(self):
        trem = TremAutonomo()
        with self.assertRaises(ValueError):
            trem.executar_comandos([])

    def test_comando_invalido(self):
        trem = TremAutonomo()
        with self.assertRaises(ValueError):
            trem.executar_comandos(['INVALIDO'])

    def test_limite_50_movimentos(self):
        trem = TremAutonomo()
        comandos = ['DIREITA'] * 50
        posicao_final = trem.executar_comandos(comandos)
        self.assertEqual(posicao_final, 50)
        with self.assertRaises(Exception):
            trem.mover('DIREITA')

    def test_limite_20_movimentos_consecutivos(self):
        trem = TremAutonomo()
        comandos = ['DIREITA'] * 20 + ['ESQUERDA']
        posicao_final = trem.executar_comandos(comandos)
        self.assertEqual(posicao_final, 19)
        with self.assertRaises(Exception):
            trem.executar_comandos(['DIREITA'] * 21)

if __name__ == '__main__':
    unittest.main()
