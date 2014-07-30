# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from polls.models import Poll


def index_1(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    #for pool in latest_poll_list: print pool.question
    template = loader.get_template('polls/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))
    #return HttpResponse("Hello World. You\re at the poll index.")

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    '''try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})'''
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})
    #return HttpResponse("You're looking at pool %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

