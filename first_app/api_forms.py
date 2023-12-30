from django import forms
import datetime
class Contact_form1(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField(required=True)
    comment=forms.CharField(required=False,widget=forms.Textarea(attrs={"rows":2}))
    agree=forms.BooleanField()
    enter_Date=forms.DateField(label="Enter date",widget=forms.DateInput(attrs={"type":"date"}))
    birth_year_choices=['1980', '1981', '1982']
    birthday=forms.DateField(widget=forms.SelectDateWidget(years=birth_year_choices))
    value=forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    favorite_colors_choices = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_colors=forms.ChoiceField(choices=favorite_colors_choices)
    favorite_colors1=forms.ChoiceField(choices=favorite_colors_choices ,widget=forms.RadioSelect(attrs={"class":"text-primary"}))
    favorite_colors2=forms.MultipleChoiceField(choices=favorite_colors_choices)
    favorite_colors3=forms.MultipleChoiceField(choices=favorite_colors_choices ,widget=forms.CheckboxSelectMultiple())