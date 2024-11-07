from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('add_user',views.addUser),
    path('delete_user/<int:id>',views.delete_user)

]