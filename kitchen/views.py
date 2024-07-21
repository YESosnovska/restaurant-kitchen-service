from django.shortcuts import render
from django.views import generic

from kitchen.models import Cook, DishType, Dish


def index(request):
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "kitchen/cooks_list.html"
    paginate_by = 5


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_types_list"
    template_name = "kitchen/dish_types_list.html"
    paginate_by = 5


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "kitchen/dish_list.html"
    paginate_by = 5
