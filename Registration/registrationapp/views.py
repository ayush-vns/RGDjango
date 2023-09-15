from django.shortcuts import render, HttpResponse, redirect
from .models import regis
from django.contrib.auth import authenticate, login
import json
import requests
from django.http import JsonResponse
import requests


# Create your views here.
def index(request):
    return HttpResponse("Hello App")

# def regist(request):
#     Username = ""
#     name = ""
#     password = ""
#     result = ""
#     confirmpassword= ""

#     submit = ""
#     if request.POST:
#         Username = request.POST["Username"]
#         name = request.POST["Name"]
#         password = request.POST["password"]
#         confirmpassword = request.POST["confirmpassword"]
#         if password != confirmpassword:
#             result = "Passwords not matched"
#             return render(request, "create.html",
#                           {"Username": Username, "name": name, "password": password, "confirmpassword": confirmpassword, "submit": submit,
#                            "result": result})
#         try:
#               ms = regis()
#               ms.Username = Username
#               ms.Name = name
#               ms.Password = password
#               ms.save()
#               result = "Saved"
#         except:
#             result = "Username already exists"

#         print("saved data")

#     return render(request, "create.html",
#                   {"Username": Username, "name": name, "password": password, "confirmpassword": confirmpassword, "submit": submit, "result":result})


# def login(request):
#     Username=""
#     Password=""
#     data=""
#     result=""
#     if request.POST:
#         Username=request.POST["Username"]
#         Password=request.POST["Password"]
#         data=regis.objects.filter(Username=Username).filter(Password=Password)
#         # data=regis.objects.filter(password=password)
#         if len(data)<=0:
#             result="check your details"
#             return render(request,"login.html",{"result":result})
#         else:
#             data=data[0]
#             return render(request,"create.html")
#     # return render(request,'login.html',{"message":"ok"})
#     return render(request,"login.html",{"Username":Username,"Password":Password,"result":result})


def regist(request):
    Username = ""
    name = ""
    password = ""
    result = ""
    confirmpassword = ""
    submit = ""
    if request.POST:
        Username = request.POST["Username"]
        name = request.POST["Name"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]

        if password != confirmpassword:
            result = "Passwords not matched"
        else:
            try:
                ms = regis()
                ms.Username = Username
                ms.Name = name
                ms.Password = password
                ms.save()
                request.session['result'] = "Saved"
                result = "succes full created"
                return render(request, 'create.html', {"result": result})
            except:
                result = "Username already exists"
    return render(request, "create.html",
                  {"Username": Username, "name": name, "password": password, "confirmpassword": confirmpassword,
                   "submit": submit, "result": result})
# def img(request):
#     return render(request,"img.html")


def login(request):
    username = ""
    password = ""
    result = ""
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        print(username, password)
        U = regis.objects.filter(Username=username).filter(Password=password)
        if len(U) > 0:
            request.session['username'] = username
            return render(request, "create.html")
        else:
            result = "Check your details"

    return render(request, "login.html", {"username": username, "password": password, "result": result})


def img(request):
    return render(request, "new.html")


def weather(request):
    appid = "8719279a10f1e0314129f9ba6db8406c"
    city = "varanasi"
    if request.GET:
        city = request.GET["city"]
    # city = input("Enter City\n")
    params = {'appid': appid, "q": city, "units": "metric"}
    url = "https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(
        appid, city)
    # url = "https://api.openweathermap.org/data/2.5/forecast?lat=25.3333&lon=83&appid=4a1f8a61b74546825af1e0be106e797b
    # &units=metric"
    response = requests.get(url, params)
    print(code)
    code = response.status_code
    print("Error")
    # 200 means success
    # Status code 404 not found
    # Sttus code 401 is not authorized
    # print(response.text)
    if code != 200:
        result = "Error"
    else:
        result = json.loads(response.text)
        # result=response.text
        # print(jsondata)

    return render(request, "weather.html", {"result": result, "city": city, "img": result["weather"][0]["icon"]})


def get_planet_data(request):
    url = "https://swapi.dev/api/films/1/"
    # Check if the request was successful (status code 200)

    # Make a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        planet_data = response.json()

        # Return the planet data as JSON response
        return JsonResponse(planet_data)
    else:
        # Handle the error if the request was not successful
        error_message = f"Failed to fetch data. Status code: {response.status_code}"
        return JsonResponse({"error": error_message}, status=500)


def film(request):
    result = ""
    # if request.GET:
    #   title = request.Get["title"]
    url = "https://swapi.dev/api/films/"
    # url ko padhane k liye
    response = requests.get(url)
    # status code read
    code = response.status_code
    print(code)
    if code != 200:
        print("Error")
        result = "Error"
    else:
        # str ko dictnory ko m convert karta hai
        result = json.loads(response.text)
        # result=response.text
        # print(jsondata)

    return render(request, "fil.html", {"result": result})


def filmNo(request):
    filmno = ""
    result = ""
    status = ""
    if request.GET:
        filmno = request.GET['filmno']
    try:
        url = f"https://swapi.dev/api/films/"+filmno
        response = requests.get(url)
        code = response.status_code
        print(code)
        if code != 200:
            status = "error"
            print("Error")
            return render(request, "film.html", {"result": "error"})
        else:
            result = json.loads(response.text)
            status = "success"
    except:
        status = "error"

    return render(request, "film.html", {"result": result, "filmno": filmno, "people": result["characters"], "status": status})


def ayush(request):
    result = ""
    # if request.GET:
    #   title = request.Get["title"]
    # url = "https://gist.githubusercontent.com/ayush-vns/ae34d67ab846d111959df63c1ca2960c/raw/e02fea41ccdd3f442cd973e2390bf2ab5a823001/ayushkapahlagist"
    url = "https://gist.githubusercontent.com/ayush-vns/d7fd0e2cb2a499f1d4743c34f42ff977/raw/4c65ddab27bdcc9ceb5d7771ee5e57c0fc748428/mysecondgist"
    response = requests.get(url)
    code = response.status_code
    print(code)
    if code != 200:
        print("Error")
        result = "Error"
    else:
        result = json.loads(response.text)
        # result=response.text
        # print(jsondata)
    return render(request, "ayush.html", {"result": result})


def people(request):
    url = request.GET["peopleno"]
    response = requests.get(url)
    code = response.status_code
    print(code)
    if code != 200:
        print("Error")
        return HttpResponse("error")
    else:
        result = json.loads(response.text)
        #  return HttpResponse(result)
        #  return render(request,"actor.html",{"result":result})
    return JsonResponse(result)
    return HttpResponse(url)


def Mcq(request):
    url="https://gist.githubusercontent.com/ayush-vns/3a057c90bb9a7702d77beee8fab9d09c/raw/dc62465391c3c54105766f78e315c016f3a11e68/MCQ"
    # url = "https://gist.githubusercontent.com/ayush-vns/3a057c90bb9a7702d77beee8fab9d09c/raw/af6050cd0ebc87e72d2bbf4f85927f89290f307c/MCQ "
    # Check if the request was successful (status code 200)

    # Make a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        planet_data = response.json()

        # Return the planet data as JSON response
        return JsonResponse(planet_data)
    else:
        # Handle the error if the request was not successful
        error_message = f"Failed to fetch data. Status code: {response.status_code}"
        return JsonResponse({"error": error_message}, status=500)


def MCQno(request):
    prizes = [
        {"prize": 1000, "class": "highlight"}, {"prize": 3000, "class": ""}, {"prize": 5000, "class": ""},{"prize": 10000, "class": ""}, {"prize": 20000, "class": ""}, {"prize": 40000, "class": ""}, {"prize": 80000, "class": ""}, {"prize": 160000, "class": ""},
        {"prize": 320000, "class": ""},{"prize": 640000, "class": ""},{"prize": 1250000, "class": ""},{"prize": 2500000, "class": ""}, {"prize": 5000000, "class": ""}, {"prize": 10000000, "class": ""}, {"prize": 50000000, "class": ""},{"prize": 70000000,"class":""},]
    qno = 1
    a, b, c, d = "", "", "", ""
    question=""
    result = ""
    status = ""
    kbcresult=""
    selected_option = ""
    User_answers = []
    if request.POST:
        print("Here")
        qno = int(request.POST['qno'])
        print(request.POST['a'],' blank ')
        selected_option = int(request.POST['a'])
        ans = int(request.POST['ans'])
        ans-=1
        print('Answers', selected_option, ",", ans)
        if ans == selected_option:
            
            kbcresult="Correct"
            print("Correct")
        else:
            kbcresult="Wrong"
            print("Wrong")
    try:
        url="https://gist.githubusercontent.com/ayush-vns/3a057c90bb9a7702d77beee8fab9d09c/raw/df9def99343a3a89994d51842140f7659bf37029/MCQ"
        # url = f"https://gist.githubusercontent.com/ayush-vns/3a057c90bb9a7702d77beee8fab9d09c/raw/dd23ad341ad5e706186c286db38f797b66de0cb7/MCQ"
        response = requests.get(url)
        n=len(prizes)
        for i in range(n):
            if qno!=i+1:
                prizes[i]["class"]=""
            else:
                prizes[i]["class"]="highlight"
        code = response.status_code
        print("Try")
        print(code)
        if code != 200:
            status = "error"
            print("Error")
            return render(request, "mcq.html", {"result": "error"})
        else:
            result = json.loads(response.text)
            result = result["questions"]
            result = result[qno-1]
            print(result)
            # print(result.keys())
            question = result['question']
            a = result["options"][0]
            b = result["options"][1]
            c = result["options"][2]
            d = result["options"][3]
            ans = result['correct_option']

            # print(question,a,b,c,d,sep=",")
            # result=json.loads(result)
            # question=result["question"]
            # a=result[0]
            # print(question,a)
            # print(result)
            status = "success"
    except:
        status = "error"
    print(status)

    return render(request, "mcq.html", {"result": kbcresult, "qno": qno+1, "status": status, "a": a, "b": b, "c": c, "d": d, "question": question, "ans": ans,"prizes":prizes[::-1]})
    # return render(request, "mcq.html", {"result": result, "qno": qno+1, "status": "","a":"","b":"","c":"","d":"","question":""})
