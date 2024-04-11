from django.shortcuts import render,redirect
from .models import Register,customer,Products,Cart,CartDetails
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import sweetify
def index(request): 
          if 'email' in request.session:
                    data=Register.objects.get(Email=request.session['email'])
                    q=data.Uname
                    return render(request,"index.html",{'data':q})
          else:
                     return render(request,"index.html",{'data':None})
def register(request):
          if request.method == "POST":
                    name=request.POST.get('name')
                    number=request.POST.get('number')
                    email=request.POST.get('email')
                    password=request.POST.get('password')
                    obj=Register(Uname=name,No=number,Email=email,password=password)
                    obj.save()
                    return redirect('login')
                              
          return render(request,"register.html")
def login(request):
          if request.method=="POST":
                    email = request.POST.get('email')
                    password = request.POST.get('password')
                    print(email)
                    data=Register.objects.get(Email=email)
                    try:
                              if data.Email ==email:
                               
                                        if data.password ==password:
                                                  request.session['email']=email
                                                  return redirect('index')
                    except:
                              return render(request,"login.html")
          return render(request,"login.html")
def logout(request):
          if 'email' in request.session:
                    del request.session['email']
                    return redirect('index')
def customerdetail(request):
          try:
                    a=Register.objects.get(Email=request.session['email'])
                    q=a.Uname
                    w=Products.objects.all().filter()
                    if request.method=="POST":
                              cname=request.POST.get('name')
                              email=request.POST.get('email')
                              mobile=request.POST.get('mobile')
                              place=request.POST.get('place')
                              date=request.POST.get('date')
                              time=request.POST.get('time')
                             
                              obj=customer(cname=cname,cemail=email,cmobile=mobile,place=place,date=date,time=time)
                              obj.save()
                              return render(request,"cart.html",{'data':q,'cname':cname,'products':w,'email':email,'mobile':mobile,'place':place,'date':date,'time':time})

                              # return redirect('cart')
                    return render(request,"form_basics.html",{'data':q})
          except:
                    return render(request,"404.html",{'data':None})
def addproducts(request):
          try:
                    c=Register.objects.get(Email=request.session['email'])  
                    q=c.Uname
                    print("Excuse Me")
                    if request.method=="POST":
                              pname=request.POST.get('pname')
                              cname=request.POST.get('cname')
                              price=request.POST.get('price')
                              quantity=request.POST.get('quantity')
                              edate=request.POST.get('edate')
                              print(pname,cname,price,quantity,edate)
                              
                              obj1=Products(pname=pname,coname=cname,price=price,quantity=quantity,exp=edate)
                              obj1.save()
                              
                              return redirect('index')
                    return render(request,"addproducts.html",{'data':q})
          
          except:
                     
                    return render(request,"404.html",{'data':None})
        
def viewcustomer(request):
          try:
                    c=Register.objects.get(Email=request.session['email'])  
                    q=c.Uname
                    d=customer.objects.all()
                    return render(request,"viewcustomer.html",{'data':q,'cus':d})
                    

          except:
                     
                    return render(request,"404.html",{'data':None})
def viewproducts(request):
          try:
                    c=Register.objects.get(Email=request.session['email'])  
                    q=c.Uname
                    d=Products.objects.all()
                    return render(request,"viewproducts.html",{'data':q,'pro':d})
                    

          except:
                     
                    return render(request,"404.html",{'data':None})
          
def cart(request):
     
          try:
                    c=Register.objects.get(Email=request.session['email'])  
                    q=c.Uname
                    w=Products.objects.all().filter()
                    if request.method=="POST":
                              pname=request.POST.get('product')
                              cname=request.POST.get('cname')
                              quantity=request.POST.get('quantity')
                              price=request.POST.get('pri')
                              date=request.POST.get('date')
                              time=request.POST.get('time')  
                              email=request.POST.get('email')
                              mobile=request.POST.get('mobile')
                              place=request.POST.get('place')
                              # udate=request.POST.get('date')
                              # utime=request.POST.get('time')     
                              obj=CartDetails(productname= pname,cusname=cname,pquantity=quantity,pprice=price,pdate=date,ptime=time)
                              obj.save()
                              return render(request,"invoice.html",{'cname':cname,'product':pname,'price':price,'email':email,'mobile':mobile,'place':place,'date':date,'time':time,'quantity':quantity})  

                    return render(request,"cart.html",{'data':q,'products':w})
          except:
                     
                    return render(request,"404.html",{'data':None})  
@csrf_exempt  
def optionaj(request):
          selected_option = request.POST.get('selectedOption')
          print(selected_option)
          v=Products.objects.get(pname=selected_option)
          o=v.price
          response_data = {'result': o}
          return JsonResponse(response_data)
@csrf_exempt
def opaj(request):
          quan= request.POST.get('quan')
          pro=request.POST.get('pro')
          v=Products.objects.get(pname=pro)
          o=v.quantity
          q=int(quan)
          print(type(o))
          print(type(q))
          if q > o:
                    response_data = {'result': 'quantity overload'}
                    return JsonResponse(response_data)
          return JsonResponse()
                    
      

          


        