from django import forms
from busapp.models import Busbooking,Welcome_Form
class Bus_booking(forms.ModelForm):
	class Meta:
		model=Busbooking
		fields=('NAME','EMAIL','PH_NO')

class Welcome_F(forms.ModelForm):
    class Meta:
        model=Welcome_Form
        fields = ('FROM','TO')
