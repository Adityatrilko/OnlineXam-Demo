from django.urls import include,path
from . import views
urlpatterns=[
    path('Questionpaper/<int:Rid>/<str:qtype>/<int:Qid>',views.Questionpaper),
    path('Result/<int:Rid>',views.Result)
]
