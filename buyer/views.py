from .models import *
from analysis.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError



# Create your views here.

def bhome(request):
    return render(request, 'buyer/buyer_home.html')


def buyer_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        gender = request.POST['gender']
        address = request.POST['address']
        password = request.POST['password']
        try:
            buyerregistration(name=name, email=email, password=password, phonenumber=phonenumber, gender=gender,
                              address=address).save()

            return redirect('/buyer_login/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/buyer_register/')
    return render(request, 'buyer/buyer_registration.html')


def buyer_login_1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            buyerregistration.objects.get(email=email, password=password)
            messages.info(request, "login successfully")
            return redirect('/buyer_home/')
        except:
            pass
    return render(request, 'buyer/buyer_login.html')


def buyer_details(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        employment = request.POST['employment']
        number = request.POST['number']
        gender = request.POST['gender']
        city = request.POST['city']
        car_type = request.POST['car_type']
        fuel = request.POST['fuel']
        transmission = request.POST['transmission']
        No_of_Owners = request.POST['No_of_Owners']
        price = request.POST['price']
        state = request.POST['state']
        buyer_data(first_name=first_name, last_name=last_name, email=email, employment=employment, number=number, city=city,
                      car_type=car_type, gender=gender,
                      transmission=transmission, fuel=fuel,No_of_Owners=No_of_Owners,price=price,state=state).save()
        messages.info(request, "submitted successfully")
        return redirect('/buyer_home/')
    return render(request, 'buyer/buyer_details.html')

def after_smart_contract(request):
    datas = mechanical_analysis.objects.filter(smart_contract=True)
    return render(request, "buyer/smart_contract_car.html", {"datas": datas})

def Bid_buyer(request, id):
    if request.method == "POST":
        bid = request.POST['bid']
        print(bid, "1")
        print(id)
        datas = mechanical_analysis.objects.get(id=id)
        datas.bid = bid
        datas.save()
    return render(request, 'buyer/smart_contract_car.html')
