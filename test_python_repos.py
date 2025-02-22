import unittest
import requests

class TestPythonRepos(unittest.TestCase):

    def setUp(self):
        """Configura la solicitud a la API de GitHub."""
        url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
        headers = {"Accept": "application/vnd.github.v3+json"}
        self.response = requests.get(url, headers=headers)
        self.response_dict = self.response.json()

    def test_status_code(self):
        """Verifica que la solicitud a la API fue exitosa (código 200)."""
        self.assertEqual(self.response.status_code, 200, "La API no respondió con 200.")

    def test_response_contains_items(self):
        """Verifica que la respuesta contiene la clave 'items'."""
        self.assertIn("items", self.response_dict, "No se encontró la clave 'items' en la respuesta.")

    def test_number_of_repositories(self):
        """Verifica que la API devuelve al menos 30 repositorios (GitHub suele mostrar 30 por defecto)."""
        self.assertGreaterEqual(len(self.response_dict["items"]), 30, "Menos de 30 repositorios devueltos.")

    def test_total_count_positive(self):
        """Verifica que el total de repositorios en GitHub sea mayor que 10,000 (según el filtro de la consulta)."""
        self.assertGreater(self.response_dict["total_count"], 10000, "Menos de 10,000 repositorios encontrados.")

if __name__ == '__main__':
    unittest.main()
