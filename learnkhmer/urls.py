from django.urls import path, include
from learnkhmer import views


app_name = 'learnkhmer'

urlpatterns = [
    path('khmer/', views.index, name='index'),    
    
]