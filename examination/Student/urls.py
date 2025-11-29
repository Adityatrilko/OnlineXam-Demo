


from django.urls import include,path
from . import views

urlpatterns = [
     path('register',views.Register),
     path('login',views.Login),
     path('logout',views.logout),
     path('about',views.About),
     path('contact',views.Contact),
     path('Studenthome/<int:Rid>',views.Studenthome)
    ] 
