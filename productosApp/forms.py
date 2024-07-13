from django import forms
from .models import Usuario, ProductosTiendita

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        if len(password) > 12:
            raise forms.ValidationError('La contraseña no puede tener más de 12 caracteres.')
        return password

class ProductosTienditaForm(forms.ModelForm):
    class Meta:
        model = ProductosTiendita
        fields = ['name_prod', 'desc_prod', 'id_categoria', 'activo', 'precio_prod']
