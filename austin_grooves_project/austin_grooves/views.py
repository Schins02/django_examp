from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request) :
	#request the context of the request.
	#the context contains info such as clients machine details
	context = RequestContext(request)

	#Construct a dictionary to pass to the template engine as its context.
	#Note

	context_dict = {'boldmessage': "I am a bold font from the context"}

	#return a rendered response to send to client
	#we make a shortcut function to make our lives easier
	#note the 1st param is the template we wish to use 

	return render_to_response('austin_grooves/index.html', context_dict, context)
