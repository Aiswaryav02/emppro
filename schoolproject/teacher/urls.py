from django.urls import path
from .views import index,home,reg,menu,Log_view,Teachhome

urlpatterns=[
    path('index/',index,name="in"),
    path('home/',home,name="hme"),
    # path('login/',log),
    path('log/',Log_view.as_view(),name="lg"),
    path('reg/',reg,name="rg"),
    path('menu/',menu,name="mn"),
    path('tchhme/',Teachhome.as_view())

]