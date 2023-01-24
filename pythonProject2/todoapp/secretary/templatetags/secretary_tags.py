from django import template
from secretary.models import Executor
from django.db.models import Count, F

register = template.Library()


@register.simple_tag(name='get_list_executors')
def get_executors():
    return Executor.objects.all()


@register.inclusion_tag('secretary/list_executors.html')
def show_executors():
    executors = Executor.objects.annotate(cnt=Count('todo')).filter(cnt__gt=0)
    return {'executors': executors}
