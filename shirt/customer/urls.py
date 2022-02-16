from django.urls import path
from  customer import views

urlpatterns =[
    path('',views.homepage),
    path('login',views.login),
    path('register',views.register),
    path('dashboard',views.dashboard),
    path('customerview',views.customerview),
    path('customeradd',views.customeradd),
    path('customeredit/<int:id>',views.customeredit),
    path('customerupdate/<int:id>',views.customerupdate),
    path('customerdelete/<int:id>',views.customerdelete)
    

]