from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

from customer.forms import CustomerForm
from customer.models import Customer
from shirtsapp.models import Decoration

# Create your views here.
def homepage(request):
    shirts = Decoration.objects.all()
    return render (request,'homepage.html',{'shirts':shirts})
def login(request):
    if request.method == "POST":
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un,password=pw)

        if user is not None:
            auth.login(request,user)
            return redirect('/dashboard')
        else:
            return redirect('/login')

    return render(request,'login.html')



def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname  = request.POST['lastname']
        email = request.POST['email']
        username =request.POST['username']
        password =request.POST['password']

        user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        user.save()
        return redirect('/login')
        
    return render(request,'register.html')
def dashboard(request):
    return render(request,'dashboard.html')
def customerview(request):
    customers=Customer.objects.raw("select * from customer")
    return render(request,'customer/view.html',{'customer':customers})

def customeradd(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/customerview")
            except:
                print("validation failed")
    else:
        form=CustomerForm()
        print("invalid")
    return render(request,'customer/add.html')
def customeredit(request,id):
    try:
       customer=Customer.objects.get(id=id)
       return render(request, "customer/edit.html", {'customer':customer})
    except:
       print("No Data Found")
    return redirect("/customeradd")
def customerupdate(request,id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST, instance=customer)
    if form.is_valid():
        try:
           form. save()
           return redirect("/customerview")
        except:
           print("validation failed")
    return render(request, "customer/edit.html", {'customer':customer})
def customerdelete(request,id):
    try:
       customer=Customer.objects.get(id=id)
       customer.delete()
    except:
        print("No data Found")
    return redirect("/customerview")