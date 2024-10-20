from django.shortcuts import render
from django.views import View
from .servise import Merge
from .forms import InputForm

class MergeAPI(View):

    def get(self,request):
        return render(request,'merge/index.html',{"form":InputForm()})
    
    def post(self,request):
        form = InputForm(request.POST)
        text=''
        if form.is_valid():
            values = form.cleaned_data['json1'],form.cleaned_data['json2']
            result=Merge()
            text = result.action(values)
        return render(request,'multiple/index.html',{"form":InputForm(),"text":text})

# Create your views here.
