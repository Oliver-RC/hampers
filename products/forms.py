from django import forms
from .models import Product, Category, Occasion


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        occasions = Occasion.objects.all()
        category_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        occasion_friendly_names = [(o.id, o.get_friendly_name()) for o in occasions]

        self.fields['category'].choices = category_friendly_names
        self.fields['occasion'].choices = occasion_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-secondary'
