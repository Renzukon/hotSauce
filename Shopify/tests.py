import os
import django
import unittest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ShopifyInternChallenge.settings")
django.setup()
from Shopify.models import fruits


class TestModels(unittest.TestCase):
    # Simple unit test to determine if the models being used is the correct one
    def testModel(self):
        fruit = fruits.objects.get(id=1)
        self.assertEqual(fruit.title, 'Apple')
    # Unit test to add more fruits into the database
    def testAddModel(self):
        fruit = fruits.objects.create(title="Mango", price="10", inventory_count="15")
        self.assertIsInstance(fruit, fruits)


if __name__ == '__main__':
        unittest.main()