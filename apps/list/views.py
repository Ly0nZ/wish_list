# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def main(request):
	return render(request, 'list/main.html')

def register(request):
	errors = []
	for key, val in request.POST.items():
		if len(val) < 3:
			errors.append("{} must be at least three characters".format(key))

	if request.POST['password'] != request.POST['confirm-password']:
		errors.append("Passwords do not match.")

	if errors:
		for err in errors:
			messages.error(request, err)
		print("no 1 reg")
		return redirect('/')

	else:
		try:
			User.objects.get(username=request.POST['username'])
			messages.error(request, "Username not available.")
		except User.DoesNotExist:

			hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
			user = User.objects.create(name=request.POST['name'],\
								username=request.POST['username'],\
								password = hashpw)
			request.session['user.id'] = user.id

	return redirect('/dashboard')

def login(request):
	errors = []
	try:
		user = User.objects.get(username = request.POST['username'])
		# b.crypt.checkpw(Given_password, stored_password)
		if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
			request.session['id'] = user.id
			return redirect('/dashboard')
		else:
			messages.error(request, "Login credentials are incorrect.")
			return redirect('/')
	
	except User.DoesNotExist:
		messages.error(request, "Username does not exist. Please try agin.")
		return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')

def dashboard(request):
	user = User.objects.all()
	item = Item.objects.all()
	context = {
		'user': user,
		'item': item
		}
	return render(request, 'list/dashboard.html', context)

def wish_list_item(request, id):
	items = Item.objects.get(id=id)
	b = Item.objects.all()
	context = {
		'items': items,
		'b': b
	}

	return render(request, 'list/wish_list.html', context)

def add(request):
	return render(request, 'list/add.html')

def addItem(request):
	user = User.objects.get(id=request.session['id'])
 	Item.objects.create(name = request.POST['name'],\
 						creator= user)

	return redirect('/dashboard')

