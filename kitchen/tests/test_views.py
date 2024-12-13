from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType

DISH_TYPE_URL = reverse("kitchen:dish-types")
DISH_TYPE_CREATE_URL = reverse("kitchen:dish-type-create")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_create(self):
        res = self.client.get(DISH_TYPE_CREATE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_delete(self):
        self.dish_type = DishType.objects.create(
            name="test",
        )
        url = reverse("kitchen:dish-type-delete", args=[self.dish_type.id])
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_update(self):
        self.dish_type = DishType.objects.create(
            name="test",
        )
        url = reverse("kitchen:dish-type-update", args=[self.dish_type.id])
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_dish_type_create(self):
        response = self.client.get(DISH_TYPE_CREATE_URL)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_dish_type_update(self):
        self.dish_type = DishType.objects.create(
            name="test",
        )
        url = reverse("kitchen:dish-type-update", args=[self.dish_type.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_dish_type_delete(self):
        self.dish_type = DishType.objects.create(
            name="test",
        )
        url = reverse("kitchen:dish-type-delete", args=[self.dish_type.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
