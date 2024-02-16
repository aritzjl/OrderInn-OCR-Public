from django.urls import path
from . import views

urlpatterns = [
    path('subir-imagen/', views.ocr, name = "ocr" ),
    path('',views.ocr,name = "ocr"),
    path('',views.ocr,name = "home"),
]
