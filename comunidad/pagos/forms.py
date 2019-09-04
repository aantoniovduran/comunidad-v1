from django import forms
from .models import Pagos

class PagosForm(forms.ModelForm):

    class Meta:
        model = Pagos
        fields = ('__all__')

    def __init__(self, user, *args, **kwargs):
        super(PagosForm, self).__init__(*args, **kwargs)
        self.fields['cuota'].queryset = Pagos.objects.filter(socio=user)
        self.fields['fechapago'].widget.attrs['readonly'] = True
        #self.fields['estadocuota'].widget.attrs['disabled'] = 'disabled'
        

