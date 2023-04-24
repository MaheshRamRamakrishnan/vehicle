import hashlib

from .models import *
from seller.models import *
from analysis.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError


def mhome(request):
    return render(request, 'management/management_home.html')

def management_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        gender = request.POST['gender']
        address = request.POST['address']
        password = request.POST['password']
        try:
            managementregistration(name=name, email=email, password=password, phonenumber=phonenumber, gender=gender,
                                   address=address).save()

            return redirect('/manage_login/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/manage_register/')
    return render(request, 'management/management_registration.html')

def management_login_1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            managementregistration.objects.get(email=email, password=password)
            messages.info(request, "login successfully")
            return redirect('/managehome/')
        except:
            pass
    return render(request, 'management/management_login.html')


def sellerdetails_2(request):
    datas = seller_details.objects.filter(approve=False)
    return render(request, "management/sellerdetails.html", {"datas": datas})

def send_Admin(request, id):
    datas = seller_details.objects.get(id=id)
    datas.approve = True
    datas.save()
    print('hi')
    messages.info(request, "successfully sent")
    return redirect('/seller_details_3/')


def comment_1(request, id):
    if request.method == "POST":
        comment = request.POST['comment']
        print(comment, "1")
        print(id)
        datas = seller_details.objects.get(id=id)
        datas.comment = comment
        datas.save()
    return render(request, 'management/sellerdetails.html')


def vehicle_details_1(request):
    datas = vehicle_details.objects.filter(approve=False)
    return render(request, "management/vehicle details.html", {"datas": datas})


def send_Analysis(request, id):
    datas = vehicle_details.objects.get(id=id)
    datas.approve = True
    datas.save()
    print('hi')
    messages.info(request, "successfully sent")
    return redirect('/seller_vehicle_2/')


def after_seller_accept(request):
    datas = mechanical_analysis.objects.filter(accept=True)
    return render(request, "management/approved.html", {"datas": datas})


def after_seller_reject(request):
    datas = mechanical_analysis.objects.filter(deny=True)
    return render(request, "management/approved.html", {"datas": datas})


import random


def smart_contract(request, id):
    data = mechanical_analysis.objects.get(id=id)
    k = random.randint(100000000000000, 1000000000000000)
    # data.km = k
    a_string = str(data.km)
    hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
    print(hashed_string)
    mah = mechanical_analysis.objects.filter(id=id).update(hash_id=hashed_string)
    datas = mechanical_analysis.objects.get(id=id)
    datas.smart_contract = True
    datas.save()
    messages.info(request, "data hashed successfully transaction is secured!! Smart Contract Created Succesfully")
    return redirect('/accepted_seller/')


def get_view(request):
    datas = mechanical_analysis.objects.all()
    return render(request, "management/view_key.html", {"datas": datas})


import rsa


def get_input2(request, id):
    get = mechanical_analysis.objects.get(id=id)
    publicKey, privateKey = rsa.newkeys(512)
    print("hello")
    r = get.id
    print(r)
    inputvar = []
    get.save()

    a = get.car_name
    b = get.km
    c = get.year
    d = get.condition
    e = get.gear_condition
    print(a)
    print(b)
    xx = [a, b, c, d, e]
    x = []
    for i in xx:
        encMessage = rsa.encrypt(i.encode(), publicKey)
        x.append(encMessage)
        print(x)

    print(x)
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    e = x[4]
    st = mechanical_analysis.objects.filter(id=r).update(car_encrypt=a, km_encrypt=b, year_encrypt=c,
                                                         condition_encrypt=d, gear_condition_encrypt=e)
    print(a, b, c, d, e)
    return redirect('/managehome/')


