'''

@author: ABDL
'''

from django.http import HttpResponse
from polls.models import Poll

def index(request):
    lastest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question for p in lastest_poll_list])
    return HttpResponse(output)