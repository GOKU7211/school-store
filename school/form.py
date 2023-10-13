from django import forms

from .models import Department, Course

class Location(forms.Form):
    department= forms.ModelChoiceField(queryset=Department.objects.all(),
        widget=forms.Select(attrs={"hx-get": "load/", "hx-target": "#id_course"}))
    course = forms.ModelChoiceField(queryset=Course.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "department" in self.data:
            department_id = int(self.data.get("department"))
            self.fields["course"].queryset = Course.objects.filter(department_id=department_id)