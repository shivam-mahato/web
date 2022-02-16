from django.urls import path

from shirtsapp import views

urlpatterns = [
    path('shirtview',views.shirtview),
    path('shirtadd',views.shirtadd),
    path('shirtedit/<int:id>',views.shirtedit),
    path('shirtupdate/<int:id>',views.shirtupdate),
    path('shirtdelete/<int:id>',views.shirtdelete)



]