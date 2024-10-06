from .models import Instrument
from django.forms import ModelForm, TextInput, CheckboxInput, Select, ClearableFileInput
from django import forms
class InstrumentForm(ModelForm):
	class Meta:
		Types=(
		('Акустическая гитара','Акустическая гитара'),
		('Бас-гитара','Бас-гитара'),
		('Электрогитара','Электрогитара')
		)
		model=Instrument
		fields=['types', 'manufacturer', 'isonbase', 'medonbox', 'caponbox', 'stronbox', 'cover']
		widgets={
			"types": Select(choices=Types),
			"manufacturer": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Производитель инструмента'
				}),
			"isonbase": CheckboxInput(),
            "medonbox": CheckboxInput(),
            "caponbox": CheckboxInput(),
            "stronbox": CheckboxInput(),
            "cover": ClearableFileInput(attrs={
                'class': 'form-control'
            })
			
		}
