from django.urls import path
from . import views
from mockerproject.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('contact/',views.contact,name="contact")

] + static(MEDIA_URL,document_root=MEDIA_ROOT)