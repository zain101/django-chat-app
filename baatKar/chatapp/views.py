from django.shortcuts import render
from allauth.account.decorators import  login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from .models import Chat
from django.db.models import Q
from itertools import chain

@login_required
def profile(request):
    users = User.objects.all()
    users = users.exclude(username=request.user)
    context = {
        "users": users,
    }
    return render(request, "profile.html", context)


def Home(request, receiver):
    print("Home")
    print("sender: ", request.user)
    print("receiver: ", receiver)
    try:
        c = Chat.objects.filter( Q(user=request.user) |
                                 # Q(receiver=User.objects.get(username=receiver)) |
                                 Q(user= User.objects.get(username=receiver))
                                 # Q(receiver= request.user)
                                 )
        c = c.filter(
            Q(receiver=User.objects.get(username=receiver)) |
            Q(receiver=request.user)

        )
        c = c.extra(order_by=['created'])
        print("fine")
    except Exception as e:
        print("Except")
        print(e)
        c = Chat.objects.filter(user = request.user)
    return render(request, "home.html", {'home': 'active', 'chat': c, 'receiver': receiver})


def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        receiver = request.POST.get('receiver', None)
        # msg = request.POST.get('msgbox', None)


        print(request.user.username)
        print(receiver)
        c = Chat(user=User.objects.get(username=request.user.username), message=msg, receiver=User.objects.get(username=receiver))
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')


def Messages(request, receiver):
    print("Messages")
    print("sender: ", request.user.username)
    print("receiver: ", receiver)
    # c = Chat.objects.filter(user=request.user)
    try:
        c = Chat.objects.filter( Q(user=request.user) |
                                 # Q(receiver=User.objects.get(username=receiver)) |
                                 Q(user= User.objects.get(username=receiver))
                                 # Q(receiver= request.user)
                                 )
        c = c.filter(
            Q(receiver=User.objects.get(username=receiver)) |
            Q(receiver=request.user)

        )
        c = c.extra(order_by=['created'])
        print("fine")
    except Exception as e:
        print("Except")
        print(e)
        c = Chat.objects.filter( user = request.user)
    return render(request, 'messages.html', {'chat': c, 'receiver': receiver})
