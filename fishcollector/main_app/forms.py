from django.forms import ModelForm
from .models import Surveys

#create a form that represents the feeding model
class SurveyForm(ModelForm):
    class Meta:
        model = Surveys
        fields = ['date', 'age']