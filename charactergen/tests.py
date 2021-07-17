from django.test import TestCase
from django.urls import reverse

from charactergen.models import Character, Genre

description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget " \
              "nulla ipsum. Cras odio tortor, commodo imperdiet facilisis eu, vulputate sed " \
              "elit. Curabitur pulvinar congue lectus vitae facilisis. In et quam tempor, imperdiet " \
              "risus ac, finibus ipsum. Phasellus sodales maximus ante, eu bibendum ipsum tincidunt et. " \
              "Ut id mauris malesuada, rutrum odio nec, varius nisi. Nunc ut tincidunt lorem. Integer " \
              "quis bibendum lorem. Nam et consectetur felis, vel eleifend velit."


def create_test_character(character_type):
    genre = Genre.objects.create(name="Fantasy", description=description)
    return Character.objects.create(type=character_type, description=description, genre=genre)


class CharactergenTests(TestCase):

    def test_random_character_shows_character(self):
        create_test_character("Meep")
        url = reverse('get_random_character')
        response = self.client.post(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Meep")
        self.assertContains(response, "Lorem ipsum dolor sit amet")

    def test_index(self):

        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "?")

