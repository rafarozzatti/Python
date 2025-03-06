import unittest
from atividades import comer

class AtividadesTestes(unittest.TestCase):
    
    def teste_comer_saudavel(self):
        self.assetEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma'
        )

    def teste_comer_gostosa(self):
        self.assetEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez'
        )

if __name__ == '__main__':
    unittest.main()
