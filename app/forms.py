from django.db.models import fields
from app.models import TODO
from django.forms import ModelForm
class TODOForm(ModelForm):
    class Meta:
        model=TODO
        fields = ['title','status','priority']
