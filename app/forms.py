from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, Button
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions

from core.models import Proveedor, MarcaComercial


class ProveedorCrearForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProveedorCrearForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'

        self.helper.layout = Layout(
            Fieldset('Nueva marca comercial',
                'nombre', 'proveedor', 'categoria_servicio', 'localidad', 'modalidad_pago', 'direccion', 'telefono_fijo', 'telefono_movil', 'email', 'sitio_web', 'observaciones'
            ),
            FormActions(
                Submit('submit', u'Guardar proveedor'),
                css_class='text-right'
            ),
        )

    class Meta:
        model = MarcaComercial
        exclude = ('estado_obj',)