from django.test import TestCase

from app.calc import add, substract


class CalcTests(TestCase):
    def test_add_numbers(self):
        '''test that 2 numbers are added'''
        self.assertEqual(add(3, 8), 11)

    def test_add_numbers(self):
        '''test that 2 numbers are substract'''
        self.assertEqual(substract(5, 11), 6)