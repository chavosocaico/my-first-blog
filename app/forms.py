from django import forms
from .models import Sala
from .models import Material
from .models import horarios
from .models import ReservarSala
from .models import ReservarMaterial


class SalaForm(forms.ModelForm):
	
	class Meta:
		model = Sala
		fields = ( 'nome', 'bloco', 'numero', 
				   'h1_Matutino', 'h2_Matutino', 'h3_Matutino', 'h4_Matutino', 'h5_Matutino', 'h6_Matutino',
				   'h1_Vespertino', 'h2_Vespertino', 'h3_Vespertino', 'h4_Vespertino', 'h5_Vespertino', 'h6_Vespertino',
				   'h1_Noturno', 'h2_Noturno', 'h3_Noturno', 'h4_Noturno',)

class MaterialForm(forms.ModelForm):
	class Meta:
		model = Material
		fields = ('nome','numero','localizacao',
				  'h1_Matutino', 'h2_Matutino', 'h3_Matutino', 'h4_Matutino', 'h5_Matutino', 'h6_Matutino',
				  'h1_Vespertino', 'h2_Vespertino', 'h3_Vespertino', 'h4_Vespertino', 'h5_Vespertino', 'h6_Vespertino',
				  'h1_Noturno', 'h2_Noturno', 'h3_Noturno', 'h4_Noturno',)

class RSalaForm(forms.ModelForm):
	class Meta:
		model = ReservarSala
		fields = ('data_da_reserva', 'horario_de_Entrada','horario_de_Saida','justificativa',)

class RMaterialForm(forms.ModelForm):
	class Meta:
		model = ReservarMaterial
		fields = ('data_da_reserva', 'horario_de_Entrada','horario_de_Saida','justificativa',)
		
