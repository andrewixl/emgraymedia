# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Photo, Home, Contact, Album, About
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
	results2 = About.objects.all()
	context = {
	"new2":results2,
	}
	return render(request, 'modeling/about.html', context)


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

def album(request, album_id):
	photo = Photo.objects.filter(master_album = album_id).all()
	context = {
	'photos' : photo,
	}
	return render(request, 'modeling/album.html', context)

def editprofile(request):
	profile = User.objects.get(id = request.session['user_id'])
	context = {
		"profile":profile,
	}
	return render(request, 'modeling/editprofile.html', context)

def editprofiledata(request):
	p = User.objects.get(id = request.session['user_id'])
	p.first_name = request.POST['first_name']
	p.last_name = request.POST['last_name']
	p.username = request.POST['username']
	p.phone = request.POST['phone']
	p.email = request.POST['email']
	p.city = request.POST['city']
	p.state = request.POST['state']

	request.session['first_name'] = request.POST['first_name']
	request.session['last_name'] = request.POST['last_name']
	request.session['username'] = request.POST['username']
	request.session['phone'] = request.POST['phone']
	request.session['email'] = request.POST['email']
	request.session['city'] = request.POST['city']
	request.session['state'] = request.POST['state']
	# p.updated_at =
	p.save()
	return redirect('/account')

def testing(request):

	return render(request, 'modeling/testing.html', context)
