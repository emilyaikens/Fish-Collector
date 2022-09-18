from django.forms import ModelForm
from .models import Surveys

class SurveyForm(ModelForm):
    class Meta:
        model = Surveys
        fields = ['date', 'age']