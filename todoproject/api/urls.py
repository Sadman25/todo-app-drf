from django.urls import path,include
from .import views

urlpatterns = [   

    path('',views.taskListView.as_view(),name='tasklist'),
    # path('login',views.userLoginView.as_view(),name='login'),
    # path('registration',views.userRegistrationView.as_view(),name='registration'),
    #path('create',views.taskCreateView.as_view(),name='create'),
    path('details/<str:pk>/',views.taskDetailsView.as_view(),name='details'),
    
]