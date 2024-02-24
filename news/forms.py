from django.forms import ModelForm
from .models import Category


class CreateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {"name": "Nome"}
