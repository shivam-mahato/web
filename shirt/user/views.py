from django.shortcuts import render , redirect
from django.contrib.auth.models import User

from user.forms import UserForm
# Create your views here.
def viewuser(request):
    users=User.objects.raw("select * from 	auth_user  ")
    return render(request,'user/viewuser.html',{'users':users})
def useradd(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname  = request.POST['lastname']
        email = request.POST['email']
        username =request.POST['username']
        password =request.POST['password']

        user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        user.save()
        return redirect('/user/userview')
    return render(request,'user/add.html')
def useredit(request, id):
    try:
        user = User.objects.get(id=id)
        
        return render(request,'user/edit.html',{'user':user})
    except:
        print("invalid")
    return redirect('/user/userview')
def userupdate(request,id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST,instance=user)
    if form.is_valid():
        try:
            form.save()
            return redirect('/user/userview') 
        except:
            print('cannot update')
    return render(request,'user/edit.html',{'user':user})

def userdelete(request,id):
    try:
        user  = User.objects.get(id=id)
        user.delete()
    except:
        print('cannot delete')
    return redirect("/user/userview")