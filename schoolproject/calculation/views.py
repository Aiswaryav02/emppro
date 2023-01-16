from django.shortcuts import render,HttpResponse
from django.views.generic import View
from .forms import Subform,Strcnts
# Create your views here.


class Add_view(View):
    def get(self,request):
        frm=Subform()
        return render(request,"addval.html",{"form":frm})
    def post(self,request):
        form_data=Subform(request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            num1=form_data.cleaned_data.get('fnum')
            num2=form_data.cleaned_data.get('snum')
            res=num1+num2
            return render(request,"addval.html",{"form":form_data,"res":res})
        return render(request,"addval.html",{"form":form_data})

class Sub_view(View):
    def get(self,request):
        form=Subform()
        return render(request,"sub.html",{'form':form})
    def post(self,request):
        form_data=Subform(request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            num1=form_data.cleaned_data.get('fnum')
            num2=form_data.cleaned_data.get('snum')
            res=num1-num2
            return render(request,"sub.html",{"form":form_data,"res":res})
        return render(request,"sub.html",{"form":form_data}) 

class Strin_view(View):
     def get(self,request):
        sent=Strcnts()
        return render(request,"stringcount.html",{"sent":sent})
     def post(self,request):
        sent=Strcnts(request.POST)
        print(request.POST)
        if sent.is_valid():
            data=sent.cleaned_data.get('sen')
            li=data.split()
            dict={}
            for i in li:
                if i not in dict:
                    dict[i]=1
                else:
                    dict[i]+=1
            data=dict.items()
            return render(request,"stringcount.html",{"res":data})
        return HttpResponse (request,"stringcount.html")

        
        
        
class Home(View):
     def get(self,request):
        return render(request,"calchome.html")
        


   

       
