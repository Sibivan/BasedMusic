from django.test import TestCase
from django.urls import reverse

from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Instrument

class GetTests(TestCase):
    def test_index_url(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basedapp/index.html')

    def test_database_url(self):
        response = self.client.get(reverse('database'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basedapp/database.html')

class PostTests(TestCase):
    def test_database_view_post(self):
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

        response = self.client.post(reverse('database'), {
            'instrument_type': 'Гитара',
            'instrument_manufacturer': 'Fender',
            'cover': image,
            'instock': 'yes',
            'strings': 'on',
            'mediator': 'on',
            'capidaster': 'on'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('database'))

        new_instrument = Instrument.objects.get(types='Гитара')
        self.assertEqual(new_instrument.manufacturer, 'Fender')
        self.assertTrue(new_instrument.isonbase)
        self.assertTrue(new_instrument.stronbox)
        self.assertTrue(new_instrument.medonbox)
        self.assertTrue(new_instrument.caponbox)

    def test_delete_instrument(self):
        """
        Тест проверяет удаление записи: сначала считает количество, удаляет и проверяет уменьшение.
        """
        # Добавляем тестовый объект, если в базе нет записей
        Instrument.objects.create(
            types='Бас-гитара',
            manufacturer='Gibson',
            isonbase=True,
            stronbox=False,
            medonbox=True,
            caponbox=False
        )

        # Фиксируем текущее количество объектов
        initial_count = Instrument.objects.count()
        self.assertGreaterEqual(initial_count, 1)

        # Удаляем запись
        instrument_to_delete = Instrument.objects.first()
        response = self.client.post(reverse('delete', kwargs={'pk': instrument_to_delete.pk}))

        # Проверяем редирект после удаления
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/database_view')

        # Проверяем, что количество записей уменьшилось на 1
        self.assertEqual(Instrument.objects.count(), initial_count - 1)
