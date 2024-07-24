from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    DishTypeListView,
    DishListView,
    CookCreateView,
    CookDetailView,
    CookDeleteView,
    CookExperienceUpdateView,
    DishTypeDeleteView,
    DishTypeUpdateView,
    DishTypeCreateView,
    DishCreateView,
    DishDetailView,
    DishDeleteView,
    DishUpdateView,
    ToggleAssignToDishView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/delete/",
         CookDeleteView.as_view(),
         name="cook-delete"),
    path(
        "cooks/<int:pk>/update/",
        CookExperienceUpdateView.as_view(),
        name="cook-experience-update",
    ),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types"),
    path(
        "dish-types/<int:pk>/delele/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path("dishes/", DishListView.as_view(), name="dishes"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path(
        "dishes/<int:pk>/toggle-assign/",
        ToggleAssignToDishView.as_view(),
        name="toggle-dish-assign",
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
]

app_name = "kitchen"
