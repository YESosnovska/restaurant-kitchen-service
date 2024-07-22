from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Dish, Cook, DishType


class ModelTests(TestCase):
    def test_dish_str(self):
        dish_type = DishType.objects.create(name="dish_type")
        dish = Dish.objects.create(
            name="test",
            description="test description",
            price=10,
            dish_type=dish_type,
        )
        self.assertEqual(
            str(dish),
            f"{dish.name} ({dish.description}), price: {dish.price}"
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
            years_of_experience=10,
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name}), "
            f"years of experience: {cook.years_of_experience}"
        )

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="test",
        )
        self.assertEqual(str(dish_type), dish_type.name)

