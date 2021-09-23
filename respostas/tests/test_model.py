from django.test import TestCase
from model_mommy import mommy

class RespostaTestcase(TestCase):

    def setUp(self):
        self.resposta = mommy.make('Resposta')
    
    def test_str(self):
        self.assertEquals(str(self.resposta), self.resposta.usuario.username)
    