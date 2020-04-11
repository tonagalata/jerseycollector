from django.forms import ModelForm
from .models import Championship

class ChampionshipForm(ModelForm):
    class Meta:
      model = Championship
      fields = ['name', 'date']
