from django.db import models
from PIL import Image
from io import BytesIO
from multiselectfield import MultiSelectField

class Strain(models.Model):

    STOCK_CHOICES = (
        ("in_stock", "In stock"),
        ("limited_stock", "Limited stock"),
        ("out_of_stock", "Out of stock"),
        ("gone_forever", "Gone forever"),
        ("coming_soon", "Coming soon"),

    )

    TYPE_CHOICES = (
        ("indica", "Indica"),
        ("sativa", "Sativa"),
        ("hybrid", "Hybrid"),
        ("indica_hybrid", "Indica Hybrid"),
        ("sativa_hybrid", "Sativa Hybrid"),
    )

    EFFECT_CHOICES = (
        ("aroused", "Aroused"),
        ("creative", "Creative"),
        ("energetic", "Energetic"),
        ("euphoric", "Euphoric"),
        ("focused", "Focused"),
        ("giggly", "Giggly"),
        ("happy", "Happy"),
        ("hungry", "Hungry"),
        ("relaxed", "Relaxed"),
        ("sleepy", "Sleepy"),
        ("talkative", "Talkative"),
        ("tingly", "Tingly"),
        ("uplifted", "Uplifted"),
    )

    AROMA_CHOICES = (
        ('ammonia', 'Ammonia'),
        ('apple', 'Apple'),
        ('apricot', 'Apricot'),
        ('berry', 'Berry'),
        ('blueberry', 'Blueberry'),
        ('blue_cheese', 'Blue Cheese'),
        ('butter', 'Butter'),
        ('cheese', 'Cheese'),
        ('chemical', 'Chemical'),
        ('chestnut', 'Chestnut'),
        ('citrus', 'Citrus'),
        ('coffee', 'Coffee'),
        ('cream', 'Cream'),
        ('diesel', 'Diesel'),
        ('earthy', 'Earthy'),
        ('flowery', 'Flowery'),
        ('gassy', 'Gassy'),
        ('grape', 'Grape'),
        ('grapefruit', 'Grapefruit'),
        ('honey', 'Honey'),
        ('lavender', 'Lavender'),
        ('lemon', 'Lemon'),
        ('lime', 'Lime'),
        ('mango', 'Mango'),
        ('menthol', 'Menthol'),
        ('mint', 'Mint'),
        ('nutty', 'Nutty'),
        ('orange', 'Orange'),
        ('peach', 'Peach'),
        ('pear', 'Pear'),
        ('pepper', 'Pepper'),
        ('pine', 'Pine'),
        ('pineapple', 'Pineapple'),
        ('plum', 'Plum'),
        ('pungent', 'Pungent'),
        ('rose', 'Rose'),
        ('sage', 'Sage'),
        ('skunk', 'Skunk'),
        ('spicy_herbal', 'Spicy/Herbal'),
        ('strawberry', 'Strawberry'),
        ('sweet', 'Sweet'),
        ('tar', 'Tar'),
        ('tea', 'Tea'),
        ('tobacco', 'Tobacco'),
        ('tree_fruit', 'Tree fruit'),
        ('tropical', 'Tropical'),
        ('vanilla', 'Vanilla'),
        ('violet', 'Violet'),
        ('woody', 'Woody'),
    )

    name = models.CharField(max_length=50)
    stock = models.CharField(max_length=20, choices=STOCK_CHOICES, default="gone_forever")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="hybrid")
    effect = MultiSelectField(choices=EFFECT_CHOICES, max_choices=3, max_length=50)
    thc = models.IntegerField()
    breeder = models.CharField(max_length=30, null=True)
    lineage = models.CharField(max_length=75, null=True)
    aroma = MultiSelectField(choices=AROMA_CHOICES, max_choices=3, max_length=50)
    description = models.TextField()
    grow_info = models.TextField()
    image = models.ImageField(upload_to='strains/img')


    def __str__(self):
        return self.name
