# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Picture, Home, Contact, Album, About, Package, Promotion, ContactPage, Navbar, Booking
from ..login_app.models import User
from django.contrib import messages

from django.shortcuts import render, redirect, HttpResponse


def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)


def index(request):
	results2 = Home.objects.all()
	nav = Navbar.objects.all()
	context = {
	"new":results2,
	"nav":nav,
	}
	return render(request, 'modeling/index.html', context)


def about(request):
	results2 = About.objects.all()
	nav = Navbar.objects.all()
	context = {
	"new2":results2,
	"nav":nav,
	}
	return render(request, 'modeling/about.html', context)


def modeling(request):
	nav = Navbar.objects.all()
	context = {
	"nav":nav,
	}
	return render(request, 'modeling/pmodeling.html', context)


def photography(request):
	nav = Navbar.objects.all()
	context = {
	"nav":nav,
	}
	return render(request, 'modeling/pphotography.html', context)


def collaborations(request):
	nav = Navbar.objects.all()
	context = {
	"nav":nav,
	}
	return render(request, 'modeling/pcollaborations.html', context)


def book(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	nav = Navbar.objects.all()
	context = {
	"nav":nav,
	}
	return render(request, 'modeling/book.html', context)


def contact(request):
	nav = Navbar.objects.all()
	contact = ContactPage.objects.all()
	context = {
	"contact" : contact,
	"nav":nav,
	}
	return render(request, 'modeling/contact.html', context)

def account(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	nav = Navbar.objects.all()
	context = {
		"first": request.session['first_name'],
		"last": request.session['last_name'],
		"username": request.session['username'],
		"email": request.session['email'],
		"city": request.session['city'],
		"state": request.session['state'],
		"phone": request.session['phone'],
		"instagram": request.session['instagram'],
		"nav":nav,
	}
	return render(request, 'modeling/account.html', context)

def createcontact(request):
	try:
		request.session['user_id']
		redirect("/")
	except KeyError:
		pass
	results = Contact.objects.createContact(request.POST, request.session['user_id'])
	request.session['contactstatus'] = results['status']
	genErrors(request, results['errors'])
	return redirect('/contact')

def emailclient(request):
    return render(request, 'modeling/emailclient.html')

def package(request, package_id):
	package = Package.objects.get(id = package_id)
	nav = Navbar.objects.all()
	context = {
	'package' : package,
	"nav":nav,
	}
	return render(request, 'modeling/packagedetails.html', context)

def album(request, album_id):
	album = Album.objects.get(id = album_id)
	photo = Picture.objects.filter(master_album = album_id).all()
	nav = Navbar.objects.all()
	context = {
	'photos' : photo,
	'album' : album,
	"nav":nav,
	}
	return render(request, 'modeling/album.html', context)

def editprofile(request):
	profile = User.objects.get(id = request.session['user_id'])
	nav = Navbar.objects.all()
	context = {
		"profile":profile,
		"nav":nav,
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

def promotions(request):
	promotions = Promotion.objects.all()
	nav = Navbar.objects.all()
	context = {
	"promotion" : promotions,
	"nav":nav,
	}
	return render(request, 'modeling/promotions.html', context)

def booking(request):
	package = Package.objects.all()
	nav = Navbar.objects.all()
	context = {
	'package' : package,
	"nav":nav,
	}
	return render(request, 'modeling/booking.html', context)

def createbooking(request):
	try:
		request.session['user_id']
		redirect("/")
	except KeyError:
		pass
	results = Booking.objects.createBooking(request.POST, request.session['user_id'], request.session['email'])
	print "created after"
	request.session['status'] = results['status']
	print results['status']
	genErrors(request, results['errors'])
	return redirect('/book')

def pmodeling(request):
	album = Album.objects.filter(album_type = "modeling").all()
	nav = Navbar.objects.all()
	context = {
	'album' : album,
	"nav":nav,
	"type":"Modeling"
	}
	return render(request, 'modeling/portfolio.html', context)

def pphotography(request):
	album = Album.objects.filter(album_type = "photography").all()
	nav = Navbar.objects.all()
	context = {
	'album' : album,
	"nav":nav,
	"type":"Photography"
	}
	return render(request, 'modeling/portfolio.html', context)

def pcollaborations(request):
	album = Album.objects.filter(album_type = "collaboration").all()
	nav = Navbar.objects.all()
	context = {
	'album' : album,
	"nav":nav,
	"type":"Collaborations"
	}
	return render(request, 'modeling/portfolio.html', context)
