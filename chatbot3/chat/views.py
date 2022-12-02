from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Room, Message, Users


# Create your views here.

def landing(request):
    return render(request, "landing.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        # form =
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken!")
                return redirect("register")
            else:
                pass
                # good-good
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect("log_in")
        else:
            messages.info(request, "Passwords don't match!")
            return redirect("register")

    return render(request, "register.html")


def log_in(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Invalid credentials!")
            return redirect("log_in")
    else:
        return render(request, "log_in.html")


def log_out(request):
    logout(request)
    return redirect("/")



def home(request):


    return render(request, "home.html")


def room_checker(request):
    room_name = request.POST["room_name"]
    # username = request.POST["username"]

    # user = request.user
    if request.user.is_authenticated:
        print('IIIIIIIIIIIIIIIIIIIIII')
        username = request.user.username
    else:
        messages.info(request, "Log in to enter room!")
        print("OOOOOOOOOOOOOO")
        return redirect("home")

    # print("AAAAAAAAAAAAAAAA")
    # print(room_name)
    # print(username)

    if Room.objects.filter(room_name=room_name).exists():
        return redirect("/" + room_name + "/?username=" + username)
    else:
        new_room = Room.objects.create(room_name=room_name)
        new_room.save()
        return redirect("/" + room_name + "/?username=" + username)


def room(request, room_name):
    # make querry
    room_details = Room.objects.get(room_name=room_name)

    room_id = room_details.id
    username = request.GET.get('username')

    return render(request, "room.html", {
        "room_name": room_name,
        "room_id": room_id,
        "username": username
    })


def send(request):
    username = request.POST["username"]
    room_id = request.POST["room_id"]
    contents = request.POST["contents"]

    new_message = Message.objects.create(username=username, room_name=room_id, contents=contents)
    new_message.save()
    return HttpResponse("Message sent successfully!")
    # return redirect("room.html")


def getMessages(request, room_name):
    print("DDDDDDDDDDDDDDDDDDDDd")

    room_details = Room.objects.get(room_name=room_name)
    messages = Message.objects.filter(room_name=room_details.id)
    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    print(room_details.id)
    for message in messages:
        print(message.username)
        print(message.timestamp)
        print(message.contents)

    return JsonResponse({"messages": list(messages.values())})

def something(request):
    return render(request, "something.html")