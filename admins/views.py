from django.shortcuts import render,redirect
from django.contrib import messages
from seller.models import *
from analysis.models import *
from django.core.mail import send_mail

# Create your views here.

def adminhome(request):
    return render(request, 'admin/admin_home.html')

def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # print(email)
        if email == "admin@gmail.com" and password == "admin":
            # print(email)
            # request.session['admin'] = "admin@gmail.com"
            messages.info(request, "login successfully")
            return render(request, 'admin/admin_home.html')
        elif email != "admin@gmail.com":
            messages.error(request, "Wrong Mail id")
            return render(request, 'admin/admin_login.html')
        elif password != "admin":
            messages.error(request, "wrong password")
            return render(request, 'admin/admin_login.html')
        else:
            return render(request, 'admin/admin_login.html')
    return render(request, 'admin/admin_login.html')


def seller_approve(request):
    datas = seller_details.objects.filter(approve=True)
    return render(request, "admin/seller_a_details.html", {"datas": datas})

def approve_project(request, id):
    datas = seller_details.objects.get(id=id)
    print(datas.email)
    # print(datas.refer)
    send_mail(
        'Subject here',
        'Congrats! ,  You  have been Approved ',
        'maheshraamsurya@gmail.com',
        [datas.email],
        fail_silently=False,
    )
    datas.approve = True

    datas.save()
    return redirect('/admin_home/')

def reject_project(request, id):
    datas = seller_details.objects.get(id=id)
    print(datas.email)
    # print(datas.refer)
    send_mail(
        'Subject here',
        'Sorry! ,  Your application have been rejected ',
        'maheshraamsurya@gmail.com',
        [datas.email],
        fail_silently=False,
    )
    datas.approve = True

    datas.save()

    return redirect('/admin_home/')

def analysis_t2(request):
    datas = team_details.objects.all()
    return render(request, "admin/analysis_team_2.html", {"datas": datas})

def valuation_2(request):
    datas = mechanical_analysis.objects.filter(to_seller=False)
    return render(request, "admin/quotation2.html", {"datas": datas})

def send_Analysis(request, id):
    datas = mechanical_analysis.objects.get(id=id)
    datas.to_seller = True
    datas.save()
    print('hi')
    messages.info(request, "successfully sent")
    return redirect('/Quotation2/')
