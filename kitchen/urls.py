from django.urls import path

from kitchen.views import index, CookListView, DishTypeListView

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types"),
]

app_name = "kitchen"
