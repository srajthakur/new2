from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from  math import  ceil
from .resource import PersonResource
from tablib import Dataset
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
import csv
from django.utils.encoding import smart_str
from django.contrib import messages
import xlwt




def login(request):

    if request.method == "POST":


        phone = request.POST.get('phone', '')
        print(type(phone))
        password = request.POST.get('password', '')
        log = Login.objects.filter(loginid=phone)
        if len(log)==0:
            messages.info(request,'User not registered')
            return render(request, 'shop/login.html')
        if log[0].password==password:

            return redirect('Home',phone)

        else:
           messages.info(request, 'Incorrect password')
           return render(request, 'shop/login.html')



    return render(request, 'shop/login.html')



def index(request):
    print(uid,'index')
    p = product.objects.all()
    c = Cart.objects.filter(uid=uid)

    ni = len(p)
    ns = ni // 4 + ceil((ni / 4) - (ni // 4))
    n = len(c)


    params = {'ns': ns, 'range': range(1,ns), 'xv': p,'n':n,'myid':uid}

    return render(request,'shop/index.html',params)



def info(request):
    return render(request, 'shop/info.html')

def Home(request,myid):

    global uid
    uid = myid
    c = Cart.objects.filter(uid=uid)
    n = len(c)
    pa = {'n': n}
    return render(request, 'shop/Home.html',pa)

def Home1(request):
    c = Cart.objects.filter(uid=uid)
    n = len(c)
    pa = {'n': n}
    return render(request, 'shop/Home1.html',pa)


def track(request):
    return render(request,'shop/index.html')
def Contact(request):
    if request.method=="POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        Contact=contact(cname=name,email=email,phone=phone,desc=desc)
        Contact.save()
    return render(request,'shop/Contact.html')
def quickview(request,myid):
    p = product.objects.filter(id=myid)
    c = Cart.objects.filter(uid=uid)
    n = len(c)
    pa={'xv':p[0],'n':n}

    if request.method=="POST":
       desc = request.POST.get('id', '')
       k = Cart.objects.filter(cartid=myid)

       if len(k)==0:
         l = Cart.objects.all()
         l=Cart(uid=uid,cartid=myid,cartname=p[0].pname,cartdecs=p[0].decs,cartimage=p[0].image,cartprice=p[0].price)
         l.save()


    return render( request,'shop/quickview.html',pa )

def search(request):
    return render(request,'shop/index.html')
def checkout(request):
    return render(request,'shop/index.html')
def cart(request,):
    print(uid,'cart')

    if request.method == "POST":
        o= request.POST.get('cartid','')
        Cart.objects.get(uid=uid,cartid=o).delete()


    c = Cart.objects.filter(uid=uid)

    n = len(c)
    if n==0:
        return render(request, 'shop/ecart.html' )

    price=0
    for i in range(0,n):
        price=price+c[i].cartprice
    pa = {'xv': c, 'n': n,'price':price}



    return render(request,'shop/cart.html',pa)


def adress(request):
    c = Cart.objects.filter(uid=uid)
    n = len(c)

    a = Adress.objects.filter(uid=uid)
    pa = {'xv': a[0],'n':n}

    if request.method=='POST':

        name = request.POST.get('name', '')
        hno = request.POST.get('hno', '')
        street = request.POST.get('street', '')
        pin = request.POST.get('pin', '')
        city = request.POST.get('city', '')
        distric = request.POST.get('distric', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')
        adress=Adress(uid=uid,name=name,houseno=hno,streetadress=street,pincode=pin,city=city,distric=distric,state=state,phone=phone)
        adress.save()


        return render(request, 'shop/adress.html',pa)

    if len(a)==0:
        return render(request, 'shop/addadress.html')
    return render(request,'shop/adress.html',pa)

def about(request):
    return render(request,'shop/adress.html')

def payment(request):
    return render(request,'shop/payment.html')


def data(request):
    labelid = request.GET("id", False)
    print(labelid)
    return render(request,'shop/payment.html')


def review(request):
    c = Cart.objects.filter(uid=uid)
    n = Adress.objects.filter(uid=uid)
    pa = {'xv': c, 'n': n[0]}

    return render(request,'shop/review.html',pa)







def createacc(request):

    if request.method == "POST":
        username = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        log = Login.objects.filter(loginid=username)
        if len(log)==1:
            messages.info(request,'User already registered')
            return render(request, 'shop/createacc.html')

        if password!=password2:
            messages.info(request, 'password not match')
            return render(request, 'shop/createacc.html')
        log=Login(loginid=username,loginname=username,password=password)
        log.save()
        messages.success(request, " sucessfully ")
        return redirect('Home',username)
    else:
       return render(request,'shop/createacc.html')



def su(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['login']

        imported_data = dataset.load(new_persons.read(), format='xls')
        # print(imported_data)
        for data in imported_data:
            print(data)

            value = Login(
                id=int(data[0]),
                loginid=int(data[1]),
                loginname=data[2],
                password=int(data[3]),

            )
            value.save()
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['product']

        imported_data = dataset.load(new_persons.read(), format='xls')
        # print(imported_data)
        for data in imported_data:
            print(data)

            value = product(

            id=int(data[0]),
            pname = data[1],
            decs = data[2],
            date = data[3],
            ca = data[4],
            sca = data[5],
            price = int(data[6]),
            image = data[7]

            )
            value.save()


    return render(request, 'shop/su.html')
def loginfo(request):
    response = HttpResponse(content_type='login/csv')
    w = csv.writer(response)
    print('updated')
    w.writerow(['id','loginid','loginname','password'])
    for l in Login.objects.all().values_list('id','loginid','loginname','password'):
        w.writerow(l)
        print(l)
    response['Content-Disposition'] = 'attachment;filename="login.csv'
    return response


def productinfo(request):
    response = HttpResponse(content_type='product/csv')
    w = csv.writer(response)
    print('updated')
    w.writerow(['id','pname','decs','date','ca','sca','price','image'])
    for l in product.objects.all().values_list('id','pname','decs','date','ca','sca','price','image'):
        w.writerow(l)
        print(l)
    response['Content-Disposition'] = 'attachment;filename="product.csv'
    return response