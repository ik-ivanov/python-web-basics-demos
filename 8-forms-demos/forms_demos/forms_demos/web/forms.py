# Create your forms here.
from django import forms
from .models import Person

class PersonForm(forms.Form):
    name = forms.CharField(
        label="Your custom nice name",
        max_length=5,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your placeholder name",
                "class": "form-control",
                "custom-attribute": "custom-value",
            }
        ),
    )
    age = forms.IntegerField(
        help_text="Please fill your age",
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    # HOBBY_CHOICES = [
    #     (1, "Football"),
    #     (2, "Basketball"),
    #     (3, "Tennis"),
    # ]

    # hobby = forms.CharField(widget=forms.CheckboxSelectMultiple(
    #     choices=HOBBY_CHOICES,
    #
    # ))
    # hobby3 = forms.CharField(widget=forms.Select(
    #     choices=HOBBY_CHOICES
    # ))
    # is_happy = forms.BooleanField(required=False)


class PersonModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Person
        fields = "__all__"  # ["name", "age"]
        exclude = ["password"]
        widgets = {
            "name": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your name",
                    "length": 5,
                }
            ),
        }
        labels = {
            "name": "Your custom name",
        }
        help_texts = {
            "age": "Please fill your age",
        }
        error_messages = {
            "name": {
                "required": "This is super important",
                "max_length": "This is too long",
            },
        }





