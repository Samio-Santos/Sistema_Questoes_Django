from django.test import TestCase
from django.core.exceptions import ValidationError
from perguntas.models import Pergunta
from categorias.models import Materia, Banca

class TestPerguntaModel(TestCase):
    def setUp(self):
        """Configura o ambiente de teste"""
        self.materia = Materia.objects.create(materia='Informática')
        self.banca = Banca.objects.create(banca='CESPE')
        
        # Dados padrão para criar perguntas
        self.dados_pergunta = {
            'enunciado': 'Teste de pergunta?',
            'alternativas_Multiplasescolhas': {
                'A': 'Alternativa A',
                'B': 'Alternativa B',
                'C': 'Alternativa C',
                'D': 'Alternativa D',
                'E': 'Alternativa E'
            },
            'alternativas_correta': 'A',
            'materia': self.materia,
            'banca': self.banca,
            'disponivel': True
        }

    def test_criar_pergunta(self):
        """Testa a criação básica de uma pergunta"""
        pergunta = Pergunta.objects.create(**self.dados_pergunta)
        self.assertEqual(pergunta.enunciado, self.dados_pergunta['enunciado'])
        self.assertEqual(pergunta.alternativas_correta, self.dados_pergunta['alternativas_correta'])
        self.assertTrue(pergunta.disponivel)

    def test_pergunta_str(self):
        """Testa a representação string da pergunta"""
        pergunta = Pergunta.objects.create(**self.dados_pergunta)
        self.assertEqual(str(pergunta), pergunta.enunciado)

    def test_pergunta_alternativas(self):
        """Testa se as alternativas estão corretas"""
        pergunta = Pergunta.objects.create(**self.dados_pergunta)
        alternativas = pergunta.alternativas_Multiplasescolhas
        self.assertEqual(alternativas['A'], 'Alternativa A')
        self.assertEqual(alternativas['B'], 'Alternativa B')
        self.assertEqual(alternativas['C'], 'Alternativa C')
        self.assertEqual(alternativas['D'], 'Alternativa D')
        self.assertEqual(alternativas['E'], 'Alternativa E')

    def test_pergunta_disponivel(self):
        """Testa se a pergunta pode ser marcada como indisponível"""
        pergunta = Pergunta.objects.create(**self.dados_pergunta)
        pergunta.disponivel = False
        pergunta.save()
        self.assertFalse(pergunta.disponivel)

    def test_pergunta_materia(self):
        """Testa a relação com a matéria"""
        pergunta = Pergunta.objects.create(**self.dados_pergunta)
        self.assertEqual(pergunta.materia, self.materia)
        self.assertEqual(pergunta.materia.materia, 'Informática')

    def test_pergunta_banca(self):
        """Testa a relação com a banca"""
        pergunta = Pergunta.objects.create(**self.dados_pergunta)
        self.assertEqual(pergunta.banca, self.banca)
        self.assertEqual(pergunta.banca.banca, 'CESPE')
    