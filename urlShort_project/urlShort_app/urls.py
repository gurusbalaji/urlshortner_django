from django.urls import path
from urlShort_app import views

urlpatterns = [
  path('',views.home),
  path('result',views.shorturl),
  path('<str:shortened_url>',views.redirectionurl)
]