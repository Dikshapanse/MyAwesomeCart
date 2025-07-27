from django.shortcuts import render
from .models import Product, Contact
from math import ceil
from django.http import HttpResponse 

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n / 4)
        grouped_products = [prod[i:i+4] for i in range(0, n, 4)]
        allProds.append([grouped_products, range(nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact_view(request):  # ✅ यहाँ नाम बदला गया
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productview(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productview.html',{'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')
