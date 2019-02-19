from django.shortcuts import render,redirect

def home_page(request):
    context = {}
    return render(request,"index.html",context)

def menu_page(request):
    context = {}
    return render(request,"menu.html",context)

def bill_page(request):
    context = {}
    return render(request,"bill.html",context)
