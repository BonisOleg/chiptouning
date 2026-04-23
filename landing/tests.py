from django.test import TestCase

from landing.templatetags.format import tellinks


class TellinksFilterTest(TestCase):

    def test_plain_number_wrapped(self):
        result = tellinks('+380950734118')
        self.assertIn('href="tel:+380950734118"', result)
        self.assertIn('class="tel-link"', result)

    def test_number_with_spaces_and_dashes(self):
        result = tellinks('+380 95 073-41-18')
        self.assertIn('href="tel:+38095073', result)

    def test_two_numbers_in_text(self):
        text = 'Іван +380507887284 або +380972770400 м. Запоріжжя'
        result = tellinks(text)
        self.assertEqual(result.count('tel-link'), 2)
        self.assertIn('href="tel:+380507887284"', result)
        self.assertIn('href="tel:+380972770400"', result)
        self.assertIn('м. Запоріжжя', result)

    def test_cyrillic_text_escaped(self):
        text = 'Тест <script>alert(1)</script> +380971234567'
        result = tellinks(text)
        self.assertNotIn('<script>', result)
        self.assertIn('&lt;script&gt;', result)
        self.assertIn('href="tel:+380971234567"', result)

    def test_no_number_unchanged(self):
        text = 'Просто текст без номера'
        result = tellinks(text)
        self.assertEqual(result, 'Просто текст без номера')
