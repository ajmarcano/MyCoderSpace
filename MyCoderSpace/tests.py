from django.test import TestCase
from MyCoderSpace.models import *
from django.urls import reverse

class BlogTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Alvaro2", email="email@email.com", password="12345678a")
        self.blog = BlogModel(autor=self.user, titulo="dalksjdnaslkjdnaskljdnaskljdnaskdjnasldnasldnaslkdnaslkdnaslkdnaslkdnalskdnalskjdnalsdnaljskdnaljksdnaljksdnlakjsndalkjsdnalkjsdnlajksdnlajsdnalsdnalsdnlajksdnlakjsdnlakjsndlasndlasdnald", sub_titulo="Sub titulo", cuerpo="cuerpo")
        self.blog.save()

    def test_longitud_titulo(self):
        '''
        Se prueba si el titulo tiene menos de 100 caracteres
        '''
        titulo = self.blog.titulo
        self.assertTrue(len(titulo) < 100)

    def test_borrar_blog__sin_loggear(self):
        '''
        Se prueba si es posible borrar un blog sin haberse loggeado a la pagina
        '''
        response = self.client.get(reverse("delete", kwargs={"pk":"1"}))
        self.assertRedirects(response, "/blogger/accounts/login/?next=/delete/1/", status_code=302, target_status_code=200)

    def test_borrar_blog__usuario_loggeado(self):
        '''
        Se prueba si es posible borrar un blog estando loggeado como el autor
        '''
        self.client.login(username="Alvaro2", password="12345678a")
        response = self.client.get(reverse("delete", kwargs={"pk":1}))
        self.assertEqual(200, response.status_code)

    def test_borrar_blog__usuario_no_dueño(self):
        '''
        Se prueba si un usuario loggeado pero que no es dueño del post, puede borrarlo
        '''
        self.client.login(username="Alvaro3", password="12345678a")
        response = self.client.get(reverse("delete", kwargs={"pk":10}))
        self.assertEqual(403, response.status_code)

