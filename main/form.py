from django import forms

from main.models import Newsletter, Customer


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewsletterForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('customer', 'status', 'interval')

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.filter(owner=user)


class CustomerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['owner']



