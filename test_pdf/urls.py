from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    # path('pdf_view/', views.render_html, name="pdf_view"),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
]