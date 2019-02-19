from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login

def home_page(request):
    context = {}
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if not user==None:
            login(request,user)
            return redirect(home_page)
        else:
            print("Login Failed")
            return render(request,"index.html",{"invalid":True})

    return render(request,"index.html",context)

def menu_page(request):
    context = {}
    return render(request,"menu.html",context)

def bill_page(request):
    context = {}
    return render(request,"bill.html",context)
