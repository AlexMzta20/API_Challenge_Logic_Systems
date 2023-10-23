# Importa la clase TestCase de Django, que es una clase base para todos los casos de prueba.
from django.test import TestCase
# Importa la función reverse de Django, que permite generar URLs a partir del nombre de las vistas.
from django.urls import reverse
# Importa el módulo status de Django REST Framework, que contiene códigos de estado HTTP.
from rest_framework import status
# Importa las clases APITestCase y APIClient de Django REST Framework.
from rest_framework.test import APITestCase, APIClient
# Importa la clase Programmer desde el módulo models en el mismo directorio.
from .models import Programmer

# Define una clase TestProgrammerModel que hereda de TestCase.


class TestProgrammerModel(TestCase):
    # Define un método setUp que se ejecuta antes de cada caso de prueba.
    def setUp(self):
        self.programmer = Programmer.objects.create(  # Crea una instancia de Programmer y la asigna a self.programmer.
            fullname='Neymar da Silva Santos Júnior',
            nickname='Neymar Jr',
            gender='Male',
            age=31,
            is_active=True
        )
    # Define un caso de prueba para verificar que self.programmer es una instancia de Programmer.

    def test_creacion_programmer(self):
        self.assertTrue(isinstance(self.programmer, Programmer))
    # Define un caso de prueba para verificar que self.programmer.is_active es True.

    def test_programmer_is_active(self):
        self.assertTrue(self.programmer.is_active)
    # Define un caso de prueba para verificar que self.programmer.age es igual a 31.

    def test_programmer_age(self):
        self.assertEqual(self.programmer.age, 31)
    # Define un caso de prueba para verificar que self.programmer.gender es igual a 'Male'.

    def test_programmer_gender(self):
        self.assertEqual(self.programmer.gender, 'Male')

# Define una clase TestProgrammerViewSet que hereda de APITestCase.


class TestProgrammerViewSet(APITestCase):
    # Define un método setUp que se ejecuta antes de cada caso de prueba.
    def setUp(self):
        # Crea una instancia de APIClient y la asigna a self.client. APIClient es una clase que permite hacer solicitudes HTTP en los casos de prueba.
        self.client = APIClient()
        self.programmer = Programmer.objects.create(  # Crea una instancia de Programmer y la asigna a self.programmer.
            fullname='Neymar da Silva Santos Júnior',
            nickname='Neymar Jr',
            gender='Male',
            age=31,
            is_active=True
        )
        # Genera la URL para la vista 'programmer-list' y la asigna a self.url.
        self.url = reverse('programmer-list')

    # Define un caso de prueba para verificar que se puede obtener una lista de todos los programadores.
    def test_get_all_programmers(self):
        # Hace una solicitud GET a self.url y guarda la respuesta en response.
        response = self.client.get(self.url)
        # Verifica que el código de estado HTTP en la respuesta es igual a 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Define un caso de prueba para verificar que se puede obtener un solo programador.
    def test_get_single_programmer(self):
        # Hace una solicitud GET a la URL del programador y guarda la respuesta en response.
        response = self.client.get(f'{self.url}{self.programmer.id}/')
        # Verifica que el código de estado HTTP en la respuesta es igual a 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Define un caso de prueba para verificar que se puede crear un programador.
    def test_create_programmer(self):
        data = {  # Define los datos para crear un programador.
            'fullname': 'Alexia Putellas Segura',
            'nickname': 'La Reina',
            'gender': 'Female',
            'age': 29,
            'is_active': True
        }
        # Hace una solicitud POST a self.url con los datos del programador y guarda la respuesta en response.
        response = self.client.post(self.url, data)
        # Verifica que el código de estado HTTP en la respuesta es igual a 201 Created.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Define un caso de prueba para verificar que se puede eliminar un programador.
    def test_delete_programmer(self):
        # Hace una solicitud DELETE a la URL del programador y guarda la respuesta en response.
        response = self.client.delete(f'{self.url}{self.programmer.id}/')
        # Verifica que el código de estado HTTP en la respuesta es igual a 204 No Content.
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# Define una clase TestProgrammerRoutes que hereda de APITestCase.


class TestProgrammerRoutes(APITestCase):
    # Define un método setUp que se ejecuta antes de cada caso de prueba.
    def setUp(self):
        # Crea una instancia de APIClient y la asigna a self.client.
        self.client = APIClient()
        self.programmer = Programmer.objects.create(  # Crea una instancia de Programmer y la asigna a self.programmer.
            fullname='John Doe',
            nickname='jdoe',
            gender='Male',
            age=30,
            is_active=True
        )
    # Define un caso de prueba para verificar que se puede obtener la ruta de la lista de programadores.

    def test_get_programmer_list_route(self):
        # Genera la URL para la vista 'programmer-list' y la asigna a url.
        url = reverse('programmer-list')
        # Hace una solicitud GET a url y guarda la respuesta en response.
        response = self.client.get(url)
        # Verifica que el código de estado HTTP en la respuesta es igual a 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Define un caso de prueba para verificar que se puede obtener la ruta del detalle de un programador.
    def test_get_programmer_detail_route(self):
        # Genera la URL para la vista 'programmer-detail' con el id del programador y la asigna a url.
        url = reverse('programmer-detail', kwargs={'pk': self.programmer.id})
        # Hace una solicitud GET a url y guarda la respuesta en response.
        response = self.client.get(url)
        # Verifica que el código de estado HTTP en la respuesta es igual a 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
