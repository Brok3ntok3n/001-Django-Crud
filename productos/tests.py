from django.test import TestCase
from django.urls import reverse


class ListaProductosViewTests(TestCase):
    def test_lista_productos_renderiza(self):
        response = self.client.get(reverse('productos:lista'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productos/lista.html')
