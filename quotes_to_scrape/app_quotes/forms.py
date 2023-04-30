from django.forms import ModelForm, CharField, TextInput, ModelChoiceField, ModelMultipleChoiceField, Select, \
    SelectMultiple

from .models import Author, Tag, Quote


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control'}))
    born_date = CharField(max_length=20, widget=TextInput(attrs={'class': 'form-control'}))
    born_location = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(max_length=5000, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class TagForm(ModelForm):
    tag = CharField(max_length=25, required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Tag
        fields = ['tag']


class QuoteForm(ModelForm):
    quote = CharField(max_length=1000, widget=TextInput(attrs={'class': 'form-control'}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'),  # noqa
                              widget=Select(attrs={"class": "form-select"}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('tag'),  # noqa
                                    widget=SelectMultiple(attrs={"class": "form-select", "size": "7"}))

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
        # exclude = ['tags']
