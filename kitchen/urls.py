from django.urls import path

from kitchen.views import index, CookListView, DishTypeListView, DishListView, CookCreateView, CookDetailView, \
    CookDeleteView, CookExperienceUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("cooks/<int:pk>/update/", CookExperienceUpdateView.as_view(), name="cook-experience-update"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types"),
    path("dishes/", DishListView.as_view(), name="dishes"),
]

app_name = "kitchen"
