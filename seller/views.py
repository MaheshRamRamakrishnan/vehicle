from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from analysis.models import *

# Create your views here.

def shome(request):
    return render(request, 'seller/seller_home.html')


def s_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        gender = request.POST['gender']
        address = request.POST['address']
        password = request.POST['password']
        try:
            sellerregistration(name=name, email=email, password=password, phonenumber=phonenumber, gender=gender,
                               address=address).save()

            return redirect('/seller_login/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/seller_login/')
    return render(request, 'seller/seller_registration.html')


def seller_login_1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            sellerregistration.objects.get(email=email, password=password)
            messages.info(request, "login successfully")
            return redirect('/sellerhome/')
        except:
            pass
    return render(request, 'seller/seller_login.html')


#
# def vehicle_details(request):
#     return render(request, 'seller/vehicle.html')


def seller_details_2(request):
    if request.method == 'POST':
        print('1')
        title = request.POST['title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        employment = request.POST['employment']
        company = request.POST['company']
        Gender = request.POST['Gender']
        street = request.POST['street']
        zip = request.POST['zip']
        place = request.POST['place']
        country = request.POST['country']
        code = request.POST['code']
        phone = request.POST['phone']
        email = request.POST['email']

        seller_details(title=title, first_name=first_name, last_name=last_name, employment=employment,
                       company=company,
                       Gender=Gender, street=street, zip=zip, place=place, country=country, code=code, phone=phone,
                       email=email).save()
        messages.info(request, "submitted successfully")
        return redirect('/sellerhome/')
    return render(request, 'seller/seller_details.html')


def vehicledetails(request):
    if request.method == 'POST':
        print('1')
        brand = request.POST['brand']
        year = request.POST['year']
        km_driven = request.POST['km_driven']
        fuel = request.POST['fuel']
        transmission = request.POST['transmission']
        No_of_Owners = request.POST['No_of_Owners']
        Registration_City = request.POST['Registration_City']
        car_type = request.POST['car_type']
        insurance = request.POST['insurance']
        rc = request.POST['rc']
        warranty = request.POST['warranty']
        price = request.POST['price']

        vehicle_details(brand=brand, year=year, km_driven=km_driven, fuel=fuel,
                        transmission=transmission,
                        No_of_Owners=No_of_Owners, Registration_City=Registration_City, car_type=car_type,
                        insurance=insurance, rc=rc, warranty=warranty, price=price,
                        ).save()
        messages.info(request, "submitted successfully")
        return redirect('/sellerhome/')
    return render(request, 'seller/vehicle.html')


def valuation_4(request):
    datas = mechanical_analysis.objects.filter(to_seller=True)
    return render(request, "seller/valuation3.html", {"datas": datas})

def after_accept(request):
    datas = mechanical_analysis.objects.filter(accept=False)
    return render(request, "seller/acceptance.html", {"datas": datas})

def send_approve(request, id):
    datas = mechanical_analysis.objects.get(id=id)
    datas.accept = True
    datas.save()
    print('hi')
    messages.info(request, "successfully sent")
    return redirect('/after_accepet/')

def after_reject(request):
    datas = mechanical_analysis.objects.filter(deny=False)
    return render(request, "seller/reject.html", {"datas": datas})

def send_deny(request, id):
    datas = mechanical_analysis.objects.get(id=id)
    datas.deny = True
    datas.save()
    print('hi')
    messages.info(request, "successfully sent")
    return redirect('/after_deny/')

def seller_bid(request):
    datas = mechanical_analysis.objects.all()
    return render(request, "seller/bidding.html", {"datas": datas})
