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
from django import forms
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class Album(models.Model):
    album_name = models.CharField(_("Name"), max_length=255)
    album_cover = models.ImageField(
         _("Album Cover (240px x 240px)"), upload_to='media/', default='media/None/no-img.jpg')
    album_location = models.CharField(_("Location"),max_length=150)
    album_description = models.CharField(_("Description"),max_length=350)
    album_photographer = models.CharField(_("Photographer (Instagram Handle)"),max_length=350)
    shoot_date = models.DateField(_("Shoot Date"),auto_now=False, auto_now_add=False)
    album_type = models.CharField(max_length=256, choices=[('collaboration', 'Collaboration'), ('modeling', 'Modeling'), ('photography', 'Photography'), ('senior photos', 'Senior Photos')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")

    def __str__(self):
        return self.album_name

@python_2_unicode_compatible
class Picture(models.Model):
    master_album = models.ForeignKey(Album, verbose_name=_("Album"), on_delete=models.CASCADE)
    photo_caption = models.CharField(_("Caption"), max_length=255)
    photo = models.ImageField(_("Picture"), upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Picture")
        verbose_name_plural = _("Pictures")

    def __str__(self):
        return self.photo_caption

class Package(models.Model):
    package_photo = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    package_title = models.CharField(max_length=100)
    package_quote_1 = models.CharField(max_length=100)
    package_quote_2 = models.CharField(max_length=100)
    package_cost = models.CharField(max_length=100)
    package_description = models.CharField(max_length=500)
    package_inclusions = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.package_title

class Navbar(models.Model):
    about_1 = models.CharField(max_length=45)
    about_2 = models.CharField(max_length=45)
    about_3 = models.CharField(max_length=45)
    about_4 = models.CharField(max_length=45)
    portfolio_header_1 = models.CharField(max_length=45)
    portfolio_1_action_1 = models.ForeignKey(Album, related_name="album1_1")
    portfolio_1_action_2 = models.ForeignKey(Album, related_name="album1_2")
    portfolio_header_2 = models.CharField(max_length=45)
    portfolio_2_action_1 = models.ForeignKey(Album, related_name="album2_1")
    portfolio_2_action_2 = models.ForeignKey(Album, related_name="album2_2")
    portfolio_header_3 = models.CharField(max_length=45)
    portfolio_3_action_1 = models.ForeignKey(Album, related_name="album3_1")
    portfolio_3_action_2 = models.ForeignKey(Album, related_name="album3_2")

    class Meta:
        verbose_name = _("Navigation Bar")
        verbose_name_plural = _("Navigation Bar")

class Home(models.Model):
    slide_1 = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    slide_1_title = models.CharField(max_length=100)
    slide_1_description = models.CharField(max_length=250)
    slide_1_button_text = models.CharField(max_length=75)
    slide_1_button_link = models.CharField(max_length=500)

    slide_2 = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    slide_2_title = models.CharField(max_length=100)
    slide_2_description = models.CharField(max_length=250)
    slide_2_button_text = models.CharField(max_length=75)
    slide_2_button_link = models.CharField(max_length=500)

    slide_3 = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    slide_3_title = models.CharField(max_length=100)
    slide_3_description = models.CharField(max_length=250)
    slide_3_button_text = models.CharField(max_length=75)
    slide_3_button_link = models.CharField(max_length=500)

    profile_picture = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    profile_name = models.CharField(max_length=250)
    profile_title = models.CharField(max_length=250)
    profile_description_line_1 = models.CharField(max_length=250)
    profile_description_line_2 = models.CharField(max_length=250)
    profile_description_line_3 = models.CharField(max_length=250)

    modeling_album_1 = models.ForeignKey(Album, related_name="album1m")
    modeling_album_2 = models.ForeignKey(Album, related_name="album2m")
    modeling_album_3 = models.ForeignKey(Album, related_name="album3m")

    collaborations_album_1 = models.ForeignKey(Album, related_name="album1c")
    collaborations_album_2 = models.ForeignKey(Album, related_name="album2c")
    collaborations_album_3 = models.ForeignKey(Album, related_name="album3c")

    photography_album_1 = models.ForeignKey(Album, related_name="album1p")
    photography_album_2 = models.ForeignKey(Album, related_name="album2p")
    photography_album_3 = models.ForeignKey(Album, related_name="album3p")

    photography_package_1 = models.ForeignKey(Package, related_name="package1p")
    photography_package_2 = models.ForeignKey(Package, related_name="package2p")
    photography_package_3 = models.ForeignKey(Package, related_name="package3p")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Page")

class About(models.Model):
    section_1_image = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    section_1_title = models.CharField(max_length=500)
    section_1_subtitle = models.CharField(max_length=500)
    section_1_bullet_1 = models.CharField(max_length=500)
    section_1_bullet_2 = models.CharField(max_length=500)
    section_1_bullet_3 = models.CharField(max_length=500)

    section_2_image  = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    section_2_title = models.CharField(max_length=500)
    section_2_subtitle = models.CharField(max_length=500)
    section_2_description = models.CharField(max_length=500)

    section_3_image  = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    section_3_title = models.CharField(max_length=500)
    section_3_subtitle = models.CharField(max_length=500)
    section_3_description = models.CharField(max_length=500)

    section_4_image  = models.ImageField(
        upload_to='media/', default='media/None/no-img.jpg')
    section_4_title = models.CharField(max_length=500)
    section_4_subtitle = models.CharField(max_length=500)
    section_4_description = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("About Page")
        verbose_name_plural = _("About Page")

class ContactPage(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Contact Page")
        verbose_name_plural = _("Contact Page")

class Promotion(models.Model):
    promotion_name = models.CharField(max_length=250)
    promotion_percent = models.IntegerField()
    promotion_start_date = models.DateTimeField(auto_now=False)
    promotion_end_date = models.DateTimeField(auto_now=False)
    promotion_terms = models.CharField(max_length=500)
    promotion_link = models.CharField(max_length=500)

    def __str__(self):
        return self.promotion_name

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

    class Meta:
        verbose_name = _("Contact Response")
        verbose_name_plural = _("Contact Responses")

    def __str__(self):
        return self.contact_subject

class BookingManager(models.Manager):
    def createBooking(self, postData, user_id, email):
        results = {'status': True, 'errors': [], 'user': None}
        print postData
        if len(postData['location']) < 3:
            results['status'] = False
            results['errors'].append('Location Name Must be at Least 3 Characters.')
        if len(postData['length']):
            results['status'] = False
            results['errors'].append('Please Enter a Valid Number of Hours.')
            userInt = int(user_id)
            user = User.objects.get(id=userInt)
            package = Package.objects.get(package_title = postData['package'])
            results['person'] = Booking.objects.create(
                package=package, date_1=postData['date_1'], date_2=postData['date_2'], date_3=postData['date_3'],
                time_of_day=postData['time_of_day'], location=postData['location'], length_of_shoot=postData['length'],
                booker=user)
            subject = "Scheduling a Session for a " + postData['package']
            from_email = settings.DEFAULT_FROM_EMAIL
            message = ''
            recipient_list = ['andrew@emgraymedia.gq',
                              'emily@emgraymedia.gq', 'contact@emgraymedia.gq', email]
            html_message = '''<h4>Booker:</h4>
                              <h4>{booker.first_name} {booker.last_name}</h4><br>
                              <h4>Package:</h4>
                              <h4>{package}</h4><br>
                              <h4>Date 1: </h4>
                              <h4>{date_1}</h4><br>
                              <h4>Date 2: </h4>
                              <h4>{date_2}</h4><br>
                              <h4>Date 3: </h4>
                              <h4>{date_3}</h4><br>
                              <h4>Time of Day: </h4>
                              <h4>{time_of_day}</h4><br>
                              <h4>Location: </h4>
                              <h4>{location}</h4><br>
                              <h4>Length of Shoot: </h4>
                              <h4>{length_of_shoot} Hrs</h4><br>
                              <h5>This is a Copy of the Sent Message From the Contact Form on emgraymedia.gq/contact</h5> '''.format(
                              package=postData['package'], date_1=postData['date_1'], date_2=postData['date_2'], date_3=postData['date_3'],
                              location=postData['location'], length_of_shoot=postData['length'], time_of_day=postData['time_of_day'], booker=user)

            send_mail(subject, message, from_email, recipient_list,
                      fail_silently=False, html_message=html_message)
        return results


class Booking(models.Model):
    package = models.ForeignKey(Package, related_name='package')
    date_1 = models.DateTimeField(auto_now=False)
    date_2 = models.DateTimeField(auto_now=False)
    date_3 = models.DateTimeField(auto_now=False)
    time_of_day = models.CharField(max_length=500)
    location = models.CharField(max_length=1000)
    length_of_shoot = models.FloatField(max_length=10)
    booker = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookingManager()

    class Meta:
        verbose_name = _("Bookings")
        verbose_name_plural = _("Bookings")

    def __str__(self):
        return self.booker.first_name + " " + self.booker.last_name + ": " + self.package.package_title
