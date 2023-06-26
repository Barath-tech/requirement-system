from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate,login
from .models import PurchaseRequisition,Requisition,PurchaseRequisitionLine


def index(request):
    return render(request,"index.html") 

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_manager:
                login(request, user)
                return redirect('manager')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def create_requisition(request):
    n=''
    if request.method == 'POST':
        requested_by = request.POST.get('requestedBy')
        requested_date = request.POST.get('requestedDate')
        expected_date = request.POST.get('expectedDate')
        manager_name = request.POST.get('managerName')
        vendor_name = request.POST.get('vendorName')
        #requisition_Id= request.POST.get('requsitionid')
        status = 'Draft'  # Assuming you want to set the status as 'Draft' by default

        requisition = PurchaseRequisition(
            requested_by=requested_by,
            requested_date=requested_date,
            expected_date=expected_date,
            manager_name=manager_name,
            vendor_name=vendor_name,
            status=status,
            #requisition_Id=requisition_Id
        )
        requisition.save()
        n='Data Inserted'
        # Optionally, you can redirect the user to a success page or perform other actions
        return render(request, 'success.html')

    return render(request, 'home.html')

def customer(request):
    return render(request,"home.html")

def nextpage(request):
    return render(request,"purchaseorder.html")

def manager(request):
    return render(request,"orders.html")

def save_requisition(request):
    if request.method == 'POST':
        requisition_number = request.POST.get('requisitionNumber')
        requested_by = request.POST.get('requestedBy')
        requested_date = request.POST.get('requestedDate')
        comments = request.POST.get('comments')

        requisition = Requisition(
            requisition_number=requisition_number,
            requested_by=requested_by,
            requested_date=requested_date,
            comments=comments
        )
        requisition.save()
        return redirect('success.html')  # Redirect to a success page or a different URL

    return render(request, 'orders.html')  # Render the form template for GET requests

def add_lines(request):
    if request.method == 'POST':
        # Process the form submission and save the data to the database
        product_list = request.POST.getlist('product')
        unit_price_list = request.POST.getlist('unitPrice')
        quantity_list = request.POST.getlist('quantity')
        total_list = request.POST.getlist('total')

        # Save the form data to the database
        for i in range(len(product_list)):
            product = product_list[i]
            unit_price = float(unit_price_list[i])
            quantity = int(quantity_list[i])
            total = float(total_list[i])
            line = PurchaseRequisitionLine(product=product, unit_price=unit_price, quantity=quantity, total=total)
            line.save()
            

        # Redirect or show a success message
        # ...

    # Render the template
    return render(request, 'purchaseorder.html')