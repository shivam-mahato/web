from django.urls import path
from user import views

urlpatterns = [
    path('userview',views.viewuser),
    path('useradd',views.useradd),
    path('useredit/<int:id>',views.useredit),
    path('userupdate/<int:id>',views.userupdate),
    path('userdelete/<int:id>',views.userdelete)
]
