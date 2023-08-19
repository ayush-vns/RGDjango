from django.shortcuts import render,HttpResponse,redirect
from .models import regis


# Create your views here.
def index(request):
    return HttpResponse("Hello App")

def regist(request):
    Username = ""
    name = ""
    password = ""
    result = ""
    confirmpassword= ""

    submit = ""
    if request.POST:
        Username = request.POST["Username"]
        name = request.POST["Name"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]
        if password != confirmpassword:
            result = "Passwords not matched"
            return render(request, "create.html",
                          {"Username": Username, "name": name, "password": password, "confirmpassword": confirmpassword, "submit": submit,
                           "result": result})
        try:
              ms = regis()
              ms.Username = Username
              ms.Name = name
              ms.Password = password
              ms.save()
              result = "Saved"
        except:
            result = "Username already exists"

        print("saved data")

    return render(request, "create.html",
                  {"Username": Username, "name": name, "password": password, "confirmpassword": confirmpassword, "submit": submit, "result":result})


def login(request):
    Username=""
    Password=""
    data=""
    result=""
    if request.POST:
        Username=request.POST["Username"]
        Password=request.POST["Password"]
        data=regis.objects.filter(Username=Username).filter(Password=Password)
        # data=regis.objects.filter(password=password)
        if len(data)<=0:
            result="check your details"
            return render(request,"login.html",{"result":result})
        else:
            data=data[0]
            return render(request,"create.html")
    # return render(request,'login.html',{"message":"ok"})
    return render(request,"login.html",{"Username":Username,"Password":Password,"result":result})

