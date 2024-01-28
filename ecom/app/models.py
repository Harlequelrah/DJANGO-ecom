from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return f"{self.title}"

    class Categories(models.TextChoices):
        CURD = 'CR'
        MILK = 'ML'
        LASSI = 'LS'
        MILKSHAKE = 'MS'
        PANEER = 'PN'
        GHEE = 'GH'
        CHEESE = 'CZ'
        ICE_CREAMS = 'IC'

    @classmethod
    def get_category_name(cls, category_name):
        CATEGORY_MAPPING = {
            'CR': 'Crud',
            'ML': 'Milk',
            'LS': 'Lassi',
            'MS': 'Milkshake',
            'PN': 'Paneer',
            'GH': 'Ghee',
            'CZ': 'Cheese',
            'IC': 'Ice-Creams',
        }
        return CATEGORY_MAPPING.get(category_name, '')

    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=Categories.choices, max_length=10)
    product_image=models.ImageField(upload_to='product')

