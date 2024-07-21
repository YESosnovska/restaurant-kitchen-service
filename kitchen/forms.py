from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook, Dish


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"
