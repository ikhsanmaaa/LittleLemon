from django.test import TestCase
from .models import MenuItem
# Create your tests here.

class MenuTestCase(TestCase):
    def test_menu_creation(self):
        menu = MenuItem.objects.create(
            title='macaron', 
            price = 8.4,
            featured = False,
            category = None
            )
        self.assertEqual(menu.title,'macaron')