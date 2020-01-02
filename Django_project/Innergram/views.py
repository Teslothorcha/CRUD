""" Views for the project """
# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sorti(request):
    """Hi."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    #import pdb; pdb.set_trace()
    data = {
    	'status': 'ok',
    	'numbers': sorted_ints,
    	'message': 'Integers sorted succesfully'
    }
    return HttpResponse(json.dumps(data),
     content_type='application/json')


def say_hi(request, name, age):
	""" return greeting"""
	if age < 12:
		msg = 'sorry {nam} you are not allowed here!'.format(nam=name)
	else:
		msg = 'hi {nam} welcome to innergram'.format(nam=name)
	return HttpResponse(msg)