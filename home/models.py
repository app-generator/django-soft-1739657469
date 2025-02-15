# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Eszkozok(models.Model):

    #__Eszkozok_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)
    manufacturer_code = models.TextField(max_length=255, null=True, blank=True)
    lot_number = models.TextField(max_length=255, null=True, blank=True)
    serial_number = models.TextField(max_length=255, null=True, blank=True)
    store_id = models.ForeignKey(Stores, on_delete=models.CASCADE)
    invoice_id = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    status_id = models.ForeignKey(Statuses, on_delete=models.CASCADE)

    #__Eszkozok_FIELDS__END

    class Meta:
        verbose_name        = _("Eszkozok")
        verbose_name_plural = _("Eszkozok")


class Invoices(models.Model):

    #__Invoices_FIELDS__
    invoice_number = models.TextField(max_length=255, null=True, blank=True)
    purchase_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Invoices_FIELDS__END

    class Meta:
        verbose_name        = _("Invoices")
        verbose_name_plural = _("Invoices")


class Stores(models.Model):

    #__Stores_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    web = models.TextField(max_length=255, null=True, blank=True)

    #__Stores_FIELDS__END

    class Meta:
        verbose_name        = _("Stores")
        verbose_name_plural = _("Stores")


class Sets(models.Model):

    #__Sets_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    manufacturer_code = models.TextField(max_length=255, null=True, blank=True)

    #__Sets_FIELDS__END

    class Meta:
        verbose_name        = _("Sets")
        verbose_name_plural = _("Sets")


class Set_Items(models.Model):

    #__Set_Items_FIELDS__
    set_id = models.ForeignKey(Sets, on_delete=models.CASCADE)
    eszkoz_id = models.ForeignKey(Eszkozok, on_delete=models.CASCADE)

    #__Set_Items_FIELDS__END

    class Meta:
        verbose_name        = _("Set_Items")
        verbose_name_plural = _("Set_Items")


class Statuses(models.Model):

    #__Statuses_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Statuses_FIELDS__END

    class Meta:
        verbose_name        = _("Statuses")
        verbose_name_plural = _("Statuses")



#__MODELS__END
