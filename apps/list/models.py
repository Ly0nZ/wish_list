# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=255)
	created_at = models.DateField(auto_now_add=True)
	update_at = models.DateField(auto_now=True)

class Item(models.Model):
	name = models.CharField(max_length=255)
	users = models.ManyToManyField(User, related_name="items")
	creator = models.ForeignKey(User, related_name="created_item")
	created_at = models.DateField(auto_now_add=True)
	update_at = models.DateField(auto_now=True)