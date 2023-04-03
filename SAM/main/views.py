from django.shortcuts import render, redirect
from main.models import User_Accounts,Business_User_Accounts
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request, "index.html")

def admin(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('admin')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('admin')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('admin')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('admin')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('admin')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Account created successfully")
        
        
        return redirect('login')
        
        
    return render(request, "admin.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(username=username, email=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            if request.user.is_superuser:
                return render(request, "admin.html")
            else:
                return render(request, "ui.html")
        else:
            messages.error(request, "Bad Credentials!!")
            return render(request, "login_page.html")

    return render(request, "login_page.html")

def c_login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = User_Accounts.objects.filter(address=email, password=password).exists()
        
        if user:
            return render(request, "ui.html")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect("c_login_page")

    return render(request, "c_login_page.html")

def b_login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = Business_User_Accounts.objects.filter(address=email, password=password).exists()
        
        if user:
            return render(request, "bi.html")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect("b_login_page")

    return render(request, "b_login_page.html")

def p_login_page(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST['email']
        password = request.POST['password']
        
        user=authenticate(username=username,email=email,password=password)
        if user is not None:
            login(request)
            return render(request, "pi.html")
        else:
            messages.error("Username or Password is incorrect!!!")
            return redirect("p_login_page")


    return render(request, "p_login_page.html")

def ui(request):
    return render(request, "ui.html")

def bi(request):
    return render(request, "bi.html")

def pi(request):
    return render(request, "pi.html")
def c_signup_page(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        name = fname + " " + lname
        email = request.POST['email']
        c_no = request.POST['c_no']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        
        
        if User_Accounts.objects.filter(address=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('c_signup_page')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('c_signup_page')
        
        if len(c_no) != 10:
            messages.error(request, "Contact Number should be of 10 characters")
            return redirect("c_signup_page")
        
        if len(pass1) > 200:
            messages.error(request, "Password should be within 200 characters")
            return redirect("c_signup_page")
        
        myuser = User_Accounts()
        myuser.name = name
        myuser.address = email
        myuser.contact_no = c_no
        myuser.user_id = User_Accounts.objects.count()+1
        myuser.password = pass1
        myuser.save()

        messages.success(request, "Account created successfully")
        
        
        return redirect('c_login_page')
        
        
    return render(request, "c_signup_page.html")


def b_signup_page(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        name = fname + " " + lname
        bname = request.POST['bname']
        email = request.POST['email']
        c_no = request.POST['c_no']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
 
        if Business_User_Accounts.objects.filter(address=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('b_signup_page')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('b_signup_page')
        
        if len(c_no) != 10:
            messages.error(request, "Contact Number should be of 10 characters")
            return redirect("b_signup_page")
        
        if len(bname) > 50:
            messages.error(request, "business Name should be within 50 characters")
            return redirect("b_signup_page")
        
        if len(pass1) > 200:
            messages.error(request, "Password should be within 200 characters")
            return redirect("b_signup_page")
        
        myuser = Business_User_Accounts()
        myuser.name = name
        myuser.business_name = bname
        myuser.address = email
        myuser.contact_no = c_no
        myuser.user_id = Business_User_Accounts.objects.count()+1
        myuser.password = pass1
        myuser.save()

        messages.success(request, "Account created successfully")
        
        
        return redirect('b_login_page')
        
        
    return render(request, "b_signup_page.html")

def search_b(request):
    if request.method == 'POST':
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        name = fname + " " + lname
        email = request.POST['email']
        c_no = request.POST['c_no']
        
        qset = Business_User_Accounts.objects.filter(name=name, address=email, contact_no=c_no)
        user = qset.exists()
        if user:
            return render(request, "b_result.html", { "accounts":list(qset) })
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect("search_b")

    return render(request, "search_b.html")

def search_c(request):
    if request.method == 'POST':
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        name = fname + " " + lname
        email = request.POST['email']
        c_no = request.POST['c_no']
        
        qset = User_Accounts.objects.filter(name=name, address=email, contact_no=c_no)
        user = qset.exists()
        if user:
            return render(request, "c_result.html",{ "accounts":list(qset) })
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect("search_c")

    return render(request, "search_c.html")

def book_electric(request):
    return render(request, "book_electric.html")

@csrf_exempt
def cart(request):
    
    if request.method == 'POST':
        services = request.POST["services"]
        quantity = request.POST["quantity"]
        prices = request.POST["prices"]
        temp = request.POST["temp"]
        new = ""
        t1 = []
        for x in services:
            if x==",":
                t1.append(new)
                new = ""
            else:
                new+=x
        t1.append(new)
        new = ""
        t2 = []
        for x in quantity:
            if x==",":
                t2.append(int(new))
                new = ""
            else:
                new+=x
        t2.append(int(new))
        new = ""
        t3 = []
        for x in prices:
            if x==",":
                t3.append(int(new))
                new = ""
            else:
                new+=x
            
        t3.append(int(new))

        t4 = [x*y for x,y in zip(t2,t3)]
        s = sum(t4)
        mylist = zip(t1,t2,t4)
        print(t1,t2,t3)
        print(temp,s)

    return render(request, "cart.html", {"mylist":mylist, "sum": s})

def edit_services(request):
    return render(request, "edit_services.html")