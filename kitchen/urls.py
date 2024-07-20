from django.urls import path

from kitchen.views import index, CookListView, DishTypeListView, DishListView

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types"),
    path("dishes/", DishListView.as_view(), name="dishes"),
]

app_name = "kitchen"
