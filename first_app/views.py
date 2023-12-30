from django.shortcuts import render
from first_app.api_forms import Contact_form1
from first_app.model_forms import ContactForms2
def api_forms(request):
    if request.method=="POST":
        form=Contact_form1(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'api_forms.html',{"form":form})
    else:
        form=Contact_form1()
    return render(request,'api_forms.html',{"form":form})

def model_forms(request):
    if request.method=="POST":
        form=ContactForms2(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'model_forms.html',{"form":form})
    else:
        form=ContactForms2()
    return render(request,'model_forms.html',{"form":form})