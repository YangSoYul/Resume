from django.contrib.auth.forms import UserCreationForm
from .models import Applicant


class ApplicantForm(UserCreationForm):
    class Meta:
        model = Applicant
        fields = ['username', 'age', 'school', 'major', 'grade', 'like']
