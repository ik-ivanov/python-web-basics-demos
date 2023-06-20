from django import forms
from .models import Profile, Album


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Age'
            })
        }


class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        exclude = ['profile']

        widgets = {
            'album_name': forms.TextInput(attrs={
                'placeholder': 'Album'
            }),
            'artist': forms.TextInput(attrs={
                'placeholder': 'Artist'
            }),
            'genre': forms.Select(attrs={
                'placeholder': 'Genre'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Image URL'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price'
            })
        }
        labels = {
            "image_url": "Image URL"
        }


class DeleteAlbumModelForm(AlbumModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs = {
                'readonly': 'readonly'
            }
