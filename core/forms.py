from django import forms
from .models import Folder, File


class CreateFolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']
