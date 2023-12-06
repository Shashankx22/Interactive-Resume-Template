from django.contrib import admin
from django.urls import include, path

from . import views
from app.views import form_view
from app.views import form_view2
from app.views import form_view3
from app.views import form_view4

urlpatterns = [
    path('', views.index, name="index"),
    path('team/', views.team, name="team"),
    path("login/",views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("form1/", form_view, name="form1"),
    path("form2/", form_view2, name="form2"),
    path("form3/", form_view3, name="form3"),
    path("form4/", form_view4, name="form4"),
]