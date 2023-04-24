from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from seller.models import *


# Create your views here.

def ahome(request):
    return render(request, 'analysis/analysis_home.html')


def analysis_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        gender = request.POST['gender']
        address = request.POST['address']
        password = request.POST['password']
        try:
            analysisregistration(name=name, email=email, password=password, phonenumber=phonenumber, gender=gender,
                                 address=address).save()

            return redirect('/analysis_login/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/analysis_register/')
    return render(request, 'analysis/analysis_registration.html')


def analysis_login_1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            analysisregistration.objects.get(email=email, password=password)
            messages.info(request, "login successfully")
            return redirect('/analysishome/')
        except:
            pass
    return render(request, 'analysis/analysis_login.html')


def vehicle_details_2(request):
    datas = vehicle_details.objects.filter(approve=True)
    return render(request, "analysis/vehicle__details.html", {"datas": datas})


# def mechanical_team(request):
#     return render(request, 'analysis/mechanical2.html')


def analysis_team_1(request):
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        eid = request.POST['eid']
        city = request.POST['city']
        pin = request.POST['pin']
        email = request.POST['email']
        team_no = request.POST['team_no']
        gender = request.POST['gender']
        address = request.POST['address']


        designation = request.POST['designation']
        team_details(name=name, last_name=last_name, email=email, eid=eid, city=city, pin=pin,
                     team_no=team_no, gender=gender,
                     address=address, designation=designation).save()
        messages.info(request, "submitted successfully")
        return redirect('/analysishome/')
    return render(request, 'analysis/analysisteam.html')


def mechanical_verify(request):
    if request.method == 'POST':
        car_name = request.POST['car_name']
        brand = request.POST['brand']
        km = request.POST['km']
        year = request.POST['year']
        engine = request.POST['engine']
        condition = request.POST['condition']
        gear = request.POST['gear']
        gear_condition = request.POST['gear_condition']
        air_bag = request.POST['air_bag']
        airbag_condition = request.POST['airbag_condition']
        tyre_condition = request.POST['tyre_condition']
        light_condition = request.POST['light_condition']
        comment = request.POST['comment']
        mechanical_analysis(car_name=car_name, brand=brand, km=km, year=year, engine=engine, condition=condition,
                     gear=gear, gear_condition=gear_condition,
                     air_bag=air_bag, airbag_condition=airbag_condition,tyre_condition=tyre_condition,light_condition=light_condition,comment=comment).save()
        messages.info(request, "submitted successfully")
        return redirect('/analysishome/')
    return render(request, 'analysis/mechanical2.html')

def valuation_1(request):
    datas = mechanical_analysis.objects.all()
    return render(request, "analysis/valuation.html", {"datas": datas})

def quotation(request, id):
    if request.method == "POST":
        quotation = request.POST['quotation']
        print(quotation, "1")
        print(id)
        datas = mechanical_analysis.objects.get(id=id)
        datas.quotation = quotation
        datas.save()
    return render(request, 'analysis/valuation.html')
