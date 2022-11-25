from django import template

from adv.models import Adv
from chance.models import Chance

register = template.Library()

@register.simple_tag
def phone_number(request):
    winer = Chance.objects.first()
    return winer

@register.simple_tag
def count_users(request):
    count = Adv.objects.count()
    return count