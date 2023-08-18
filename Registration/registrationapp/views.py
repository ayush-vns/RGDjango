from django.shortcuts import render,HttpResponse
from .models import regis


# Create your views here.
def index(request):
    return HttpResponse("Hello App")

def regist(request):
    username = ""
    name = ""
    password = ""
    result = ""
    confirmpassword= ""

    submit = ""
    if request.GET:
        username = request.GET["username"]
        name = request.GET["Name"]
        password = request.GET["password"]
        confirmpassword = request.GET["confirmpassword"]
        if password != confirmpassword:
            result = "Passwords not matched"
            return render(request, "create.html",
                          {"username": username, "name": name, "password": password, "confirmpassword": confirmpassword, "submit": submit,
                           "result": result})
        try:
              ms = regis()
              ms.Username = username
              ms.Name = name
              ms.Password = password
              ms.save()
              result = "Saved"
        except:
            result = "Username already exists"

        print("saved data")

    return render(request, "create.html",
                  {"username": username, "name": name, "password": password, "confirmpassword": confirmpassword, "submit": submit, "result":result})


def login(request):
    Username=""
    password=""
    if request.GET:
        Username=request.GET["Username"]
        password=request.GET["Password"]

        data=regis.objects.filter(username=Username).filter(password=password)
        # data=regis.objects.filter(password=password)
        if len(data)<=0:
            data="error"
        else:
            data=data[0]
            return render(request,"login.html",{"username":Username,"password":password,"data":data})


