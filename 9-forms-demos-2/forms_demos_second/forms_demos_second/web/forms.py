from django.core.validators import MinLengthValidator, MaxLengthValidator
from .validators import min_value_validator, max_value_validator, ValueInRangeValidator

from django import forms
from .models import TodoModel, ImageModel, DocumentModel, PetModel, PhotoModel

class TodoForm(forms.Form):
    text = forms.CharField(
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(100),
        ],
        error_messages={
            "required": "Please enter a todo item!!!!",
            "min_length": "Todo item must be at least 5 characters long!!!!!",
        }
    )

    done = forms.BooleanField(required=False)

    priority = forms.IntegerField(
        validators=[
            ValueInRangeValidator(6, 8),
        ],
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     print(cleaned_data)
    #     cleaned_data['text'] = cleaned_data['text'].upper()
    #
    #     return cleaned_data
    #
    # def clean_done(self):
    #     # do something
    #     return self.cleaned_data
    #
    # def clean_text(self):
    #     text = self.cleaned_data["text"]
    #
    #     # additional clean
    #     # WHY:
    #     # 1. The data is valid and cleaned - data related
    #     # 2. Behavior related (ex. if student did the last course)
    #
    #     # if "bad" in text.lower():
    #     #     print('bad word detected')
    #     # #     raise ValidationError("Bad word detected")
    #
    #     self.cleaned_data['text'] = text.upper()
    #
    #     # normalize the text
    #     return self.cleaned_data  # text.lower()  # must return cleaned data


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = "__all__"
        error_messages = {
            "text": {
                "required": "Please enter a todo item??? Pretty please????",
                "min_length": "Todo item must be at least 5 characters long!!!!!",
            }
        }


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = "__all__"


class DocumentModelForm(forms.ModelForm):
    class Meta:
        model = DocumentModel
        fields = "__all__"


class PetModelForm(forms.ModelForm):
    class Meta:
        model = PetModel
        fields = "__all__"


class PhotoModelForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = "__all__"
