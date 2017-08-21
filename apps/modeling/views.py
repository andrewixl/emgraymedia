# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Photo, Home, Contact, Album
from ..login_app.models import User
from django.contrib import messages

from django.shortcuts import render, redirect, HttpResponse


def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)


def index(request):
	results2 = Home.objects.all()
	context = {
	"new":results2,
	}
	return render(request, 'modeling/index.html', context)


def about(request):
    return render(request, 'modeling/about.html')


def modeling(request):
    return render(request, 'modeling/pmodeling.html')


def photography(request):
    return render(request, 'modeling/pphotography.html')


def collaborations(request):
    return render(request, 'modeling/pcollaborations.html')


def book(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/login")
    return render(request, 'modeling/book.html')


def contact(request):
	return render(request, 'modeling/contact.html')

def account(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/login")
    context = {
    "first": request.session['first_name'],
    "last": request.session['last_name'],
    "username": request.session['username'],
    "email": request.session['email'],
	"city": request.session['city'],
	"state": request.session['state'],
	"phone": request.session['phone'],
    }
    return render(request, 'modeling/account.html', context)

def createcontact(request):
	try:
		request.session['user_id']
		redirect("/")
	except KeyError:
		pass
	results = Contact.objects.createContact(request.POST, request.session['user_id'])
	# context = {
    # "result" : results['status'],
    # }
	request.session['contactstatus'] = results['status']
	genErrors(request, results['errors'])
	return redirect('/contact')

def emailclient(request):
    return render(request, 'modeling/emailclient.html')

def package(request):
    return render(request, 'modeling/packagedetails.html')

def album(request):
    return render(request, 'modeling/album.html')

def testing(request):

	return render(request, 'modeling/testing.html', context)
