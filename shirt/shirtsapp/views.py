from django.shortcuts import render,redirect
from shirtsapp.models import Decoration

from shirtsapp.forms import ShirtForm

# Create your views here.
def shirtview(request):
    shirt = Decoration.objects.all()


    return render (request,'shirt/view.html',{'decorations':shirt})
def shirtadd(request):
    if request.method=="POST":
        form=ShirtForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/shirt/shirtview")
            except:
                print("validation failed")
    else:
        form=ShirtForm()
        print("invalid")
    return render(request,'shirt/add.html',{'form':form})

def shirtedit(request,id):
    try:
       shirt=Decoration.objects.get(id=id)
       return render(request,'shirt/edit.html',{'shirt':shirt})
    except:
       print("No Data Found")
    return redirect("/shirt/shirtview")
def shirtupdate(request,id):
    decoration = Decoration.objects.get(id=id)
    form = ShirtForm(request.POST, instance=decoration)
    if form.is_valid():
        try:
           form. save()
           return redirect("/shirt/shirtview")
        except:
           print("validation failed")
    return render(request, "shirt/edit.html", {'decoration':decoration})
def shirtdelete(request,id):
    try:
       decoration=Decoration.objects.get(id=id)
       decoration.delete()
    except:
        print("No data Found")
    return redirect("/shirt/shirtview")


    