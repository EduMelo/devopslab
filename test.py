# -*- coding: utf-8 -*-
from app import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')
        self.errorResult =  self.app.get('/bug')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        self.assertEqual(self.result.data.decode('utf-8'), "Arquitetura de Tecnologia")

    def test_bug(self):
        #verifica bug
        self.assertNotEqual(self.result.status_code, 200)