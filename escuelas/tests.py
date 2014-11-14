from django.test import TestCase
from petc.settings import CICLO_ACTUAL


class EscuelaTestCase(TestCase):

    def es_ciclo_actual(self):
        self.assertEqual(2011, CICLO_ACTUAL)
