#cuentas/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPers

class FormCreacionUsuario(UserCreationForm):
    class Meta(UserCreationForm):
        model = UsuarioPers
        fields = (
                'username',
                'email',
                'edad'
        )

        
class FormCambiarUsuario(UserChangeForm):
    class Meta:
        model= UsuarioPers
        fields = (
            'username',
            'email',
            'edad'
        )

