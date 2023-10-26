from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('login',views.SugaView.as_view(), name="yuki")

]