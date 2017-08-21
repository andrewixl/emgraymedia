# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
from datetime import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
import re


class Album(models.Model):
    album_name = models.CharField(max_length=25)
    album_cover = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    album_location = models.CharField(max_length=25)
    album_description = models.CharField(max_length=50)
    shoot_date = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.album_name


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    photo_caption = models.CharField(max_length=25)
    photo_description = models.CharField(max_length=150)
    master_album = models.ManyToManyField('Album', related_name="album")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.photo_caption


class Home(models.Model):
    slide_1 = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    slide_1_title = models.CharField(max_length=100)
    slide_1_description = models.CharField(max_length=250)
    slide_1_button_text = models.CharField(max_length=75)

    slide_2 = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    slide_2_title = models.CharField(max_length=100)
    slide_2_description = models.CharField(max_length=250)
    slide_2_button_text = models.CharField(max_length=75)

    slide_3 = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    slide_3_title = models.CharField(max_length=100)
    slide_3_description = models.CharField(max_length=250)
    slide_3_button_text = models.CharField(max_length=75)

    profile_picture = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    profile_name = models.CharField(max_length=250)
    profile_title = models.CharField(max_length=250)
    profile_description_line_1 = models.CharField(max_length=250)
    profile_description_line_2 = models.CharField(max_length=250)
    profile_description_line_3 = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ContactManager(models.Manager):
    def createContact(self, postData, user_id):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['name']) < 3:
            results['status'] = False
            results['errors'].append('Name Must be at Least 3 Characters.')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = False
            results['errors'].append('Please Enter a Valid Email.')
        if len(postData['city']) < 1:
            results['status'] = False
            results['errors'].append('Please Enter a Valid City Name.')
        if len(postData['subject']) < 5:
            results['status'] = False
            results['errors'].append(
                'Please Enter a Valid Subject in Subject Line.')
        if len(postData['message']) < 10:
            results['status'] = False
            results['errors'].append('Message Must be at Least 10 Characters.')

        if results['status'] == True:
            results['errors'].append(
                'Your Message Has Successfully Been Sent.')
            userInt = int(user_id)
            user = User.objects.get(id=userInt)
            results['person'] = Contact.objects.create(contact_name=postData['name'], contact_email=postData['email'],
                                                       contact_city=postData['city'], contact_subject=postData['subject'], contact_message=postData['message'])
            # send_mail(postData['subject'], postData['message'], 'admin@emgraymedia.gq', ['burger.andrewixl@gmail.com'], fail_silently=False)

            subject = postData['subject']
            from_email = settings.DEFAULT_FROM_EMAIL
            message = 'City:\n' + postData['city'] + \
                '\nMessage:\n' + postData['message']
            recipient_list = ['andrew@emgraymedia.gq',
                              'emily@emgraymedia.gq', 'contact@emgraymedia.gq']
            #recipient_list = ['andrew@emgraymedia.gq', 'emily@emgraymedia.gq', 'contact@emgraymedia.gq', postData['email']]
            html_message = '''<h4>Name: </h4>
                              <h4>{name}</h4><br>
                              <h4>Email: </h4>
                              <h4>{email}</h4><br>
                              <h4>City: </h4>
                              <h4>{city}</h4><br>
                              <h4>Message: </h4>
                              <h4>{message}</h4><br>
                              <h5>This is a Copy of the Sent Message From the Contact Form on emgraymedia.gq/contact</h5> '''.format(name=postData['name'], email=postData['email'], city=postData['city'], message=postData['message'])

            send_mail(subject, message, from_email, recipient_list,
                      fail_silently=False, html_message=html_message)
        return results


class Contact(models.Model):
    contact_name = models.CharField(max_length=25)
    contact_email = models.CharField(max_length=50)
    contact_city = models.CharField(max_length=25)
    contact_subject = models.CharField(max_length=75)
    contact_message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ContactManager()

    def __str__(self):
        return self.contact_subject
