from django.shortcuts import render,redirect
from .models import product,Signup
from math import ceil
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout





# Create your views here.
def index(request):
  
    allProds = []
    catprods = product.objects.values('catagory', 'prod_id')
    cats = {item['catagory'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(catagory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds }
    return render(request, 'home.html', params)


def search(request):
    Query=request.GET['query']
    if len(Query)>78:
        Product=product.objects.none()

    else:
        product_cat=product.objects.filter(catagory__icontains=Query)
        product_name=product.objects.filter(prod_name__icontains=Query)
        allProds=product_cat.union(product_name)

    params={'allprods':allProds,'query':Query}
    return render(request,'search.html',params)

def signin(request):
    if request.method=="POST":
        username=request.POST.get("uname",'')
        email=request.POST.get("email",'')
        Fname=request.POST.get("Fname",'')
        Lname=request.POST.get("Lname",'')
        phone=request.POST.get("phone",'')
        password=request.POST.get("password1",'')
        password1=request.POST.get("password2",'')


        var=Signup(Username=username,Email=email,Fname=Fname,Lname=Lname,phone=phone,password=password)
        var.save()
        if not username.isalnum() and password==password1:
            messages.error(request,"please check all the details you have put is correct or not ")
            
            return redirect('/')
    return render(request,"signin.html")        

def logIn(request):
    
    if request.method=="POST":
        name=request.POST["Uname"]
        pass2=request.POST["password5"]

        user=authenticate(Username=name,password=pass2)
      
        
        if user is None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,"please fill the form correctly")
    return render(request,"login.html")
   