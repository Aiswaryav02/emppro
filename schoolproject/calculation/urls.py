from django.urls import path
from .views import Add_view,Sub_view,Strin_view,Home
urlpatterns=[
    path('add/',Add_view.as_view()),
    path('sub/',Sub_view.as_view(),name="subv"),
    path('stri/',Strin_view.as_view(),name="wordcnt"),
    path('chome/',Home.as_view())

]