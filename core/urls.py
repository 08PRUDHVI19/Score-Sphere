from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('view_pdf/<str:id>/',views.ViewPDF.as_view(),name="pdf_view"),
]
