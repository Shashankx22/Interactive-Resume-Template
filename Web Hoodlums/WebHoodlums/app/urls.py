from django.urls import path
from . import views

app_name = 'app'  # This is the namespace for your app

urlpatterns = [
    path('resume1/', views.resume_view1, name='resume_view1'),
    path('submit1/', views.submit_form1, name='submit_form1'),
    path('resume2/', views.resume_view2, name='resume_view2'),
    path('submit2/', views.submit_form2, name='submit_form2'),
    path('resume3/', views.resume_view3, name='resume_view3'),
    path('submit3/', views.submit_form3, name='submit_form3'),
    path('resume4/', views.resume_view4, name='resume_view4'),
    path('submit4/', views.submit_form4, name='submit_form4'),

]
