from django.shortcuts import render
from django.views import View
from .servise import Multiple
from .forms import InputForm

class MultipleAPI(View):

    def get(self,request):
        return render(request,'multiple/index.html',{"form":InputForm()})
    
    def post(self,request):
        form = InputForm(request.POST)
        if form.is_valid():
            values = form.cleaned_data['text']
            result=Multiple()
            text = result.action(values)
        return render(request,'multiple/index.html',{"form":InputForm(),"text":text})
