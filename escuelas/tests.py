from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from petc.settings import CICLO_ACTUAL


class EscuelaTestCase(TestCase):

    setup_test_environment()
    client = Client()

    def es_ciclo_actual(self):
        self.assertEqual(2011, CICLO_ACTUAL)

    def acceso_restringido_sin_loguearse(self):
        self.assertEqual(client.get('/').status_code,200)
        self.assertEqual(client.get('/escuelas/').status_code, 302)

    def pagina_no_encontrada(self):
        self.assertEqual(client.get('/otro/').status_code, 404)