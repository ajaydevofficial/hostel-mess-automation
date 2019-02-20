from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login
from django.contrib.auth import logout
from userdata.models import userdata

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
    qs = userdata.objects.all()
    context = {"object":qs}
    try:
        newq = userdata.objects.filter(evening = 'idiyapam').count()
        context.update({'idiyapam':newq})
    except:
        pass
    try:
        newq = userdata.objects.filter(evening = 'meals').count()
        context.update({'meals':newq})
    except:
        pass
    try:
        newq = userdata.objects.filter(lunch = 'meals').count()
        context.update({'meal':newq})
    except:
        pass
    try:
        newq = userdata.objects.filter(evening = 'chappathy').count()
        context.update({'chappathy':newq})
    except:
        pass
    try:
        newq = userdata.objects.filter(lunch = 'biriyani').count()
        context.update({'biriyani':newq})
    except:
        pass
    try:
        newq = userdata.objects.filter(lunch = 'friedrice').count()
        context.update({'friedrice':newq})
    except:
        pass
    try:
        newq = userdata.objects.filter(morning = 'poori').count()
        context.update({'poori':newq})
    except:
        pass
    try:
        newq = userdata.objects.filter(evening = 'idli').count()
        context.update({'idli':newq})
    except:
        pass
    try:
        newq = userdata.objects.filter(evening = 'dosa').count()
        context.update({'dosa':newq})
    except:
        pass
    return render(request,"index.html",context)

def menu_page(request):
    context = {}
    price = {
    'idli' :10,
    'dosa' : 20,
    'poori' : 40,
    'friedrice' : 100,
    'biriyani' : 200,
    'meals' : 50,
    'idiyapam' : 30,
    'chappathy' : 35
    }
    try:
        if request.method=='POST':
            user = userdata.objects.get(name = request.user.username)
            return render(request,"menu.html",{"already":True})
    except:
        if request.method=='POST':
            morning = request.POST['item1']
            lunch = request.POST['item2']
            evening = request.POST['item3']
            bill = price[morning]+price[lunch]+price[evening]
            userdata.objects.create(morning = morning,lunch=lunch,evening=evening,name=request.user.username,bill=bill)
            return redirect(bill_page)
    return render(request,"menu.html",context)

def bill_page(request):
    try:
        user = userdata.objects.get(name=request.user.username)
        context = {'user':user,'submit':True}
        print('yay')
    except:
        context = {'submit':False}
        print('blah')
    return render(request,"bill.html",context)

def logout_page(request):
    logout(request)
    return redirect(home_page)
