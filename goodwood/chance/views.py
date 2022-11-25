import random
from django.shortcuts import render, redirect
from django.apps import apps
from .models import Chance

def chance(request):
    last_winer = Chance.objects.order_by("id").last()
    return render(request, 'chance/chance.html',{'last_winer':last_winer})

def do_chance(request):
    model = apps.get_model('adv', 'Adv')
    users_phones = model.objects.only('phone_number')

    list_winers = []
    for i in users_phones:
        list_winers.append(i.phone_number)
    main_winer = str(random.choice(list_winers))

    last_num = model.objects.filter(phone_number = main_winer)
    for i in last_num:
        _last  = str(i.last_num_phone)
        print(_last)
        result = main_winer + _last[-5]

        result = Chance.objects.create(number_phone=result)

        return render(request,'chance/chance.html',{'last_winer': result})


