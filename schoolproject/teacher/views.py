from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.
# function based view
# class based view

def index(request):
    name="ajith"
    li=["apple","orange","kiwi"]
    tbl=[{"name":"arun","age":20,"class":"10c"},{"name":"akhil","age":20,"class":"10a"},{"name":"ajith","age":20,"class":"10c"}]
    c=False
    return render(request,"index.html",{"data":name,"d1":li,"table":tbl,"condition":c})
def home(request):
    return render(request,"home.html")

    
# def log(request):
#     if request.method=="POST":
#         user=request.POST.get('un')
#         psw=request.POST.get('ps')
#         return HttpResponse("post:<br>Username:"+user+"<br>Password:"+psw)
#     elif request.method=="GET":
#          return render(request,"login.html")


class Log_view(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        user=request.POST.get('un')
        psw=request.POST.get('ps')
        return HttpResponse("post:<br>Username:"+user+"<br>Password:"+psw)

def reg(request):
    if request.method=="POST":
       fn=request.POST.get('fn')
       lan=request.POST.get('lan')
       un=request.POST.get('un')
       ps=request.POST.get('ps')
       cp=request.POST.get('cp')
       return HttpResponse("post:<br>First name:"+fn+"<br>Last name:"+lan+"<br>Username:"+un+"<br>Password:"+ps+"<br>Confirm password:"+cp)
    elif request.method=="GET":
       return render(request,"registration.html")


def menu(request):
    m=[{"item":"cb","category":"nonveg","price":120},
      {"item":"vb","category":"veg","price":100},
      {"item":"sadya ","category":"veg","price":100},]
    return render(request,"menu.html",{"menu":m})


class Teachhome(View):
    def get(self,request):
        return render(request,"teachhome.html")