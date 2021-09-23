from django.test import TestCase
from model_mommy import mommy

class PerguntaTestcase(TestCase):

    def setUp(self):
        self.pergunta = mommy.make('Pergunta')
    
    def test_str(self):
        self.assertEquals(str(self.pergunta), self.pergunta.enunciado)
    