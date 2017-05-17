# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from myapp.models import clinicUserProfile
from myapp.models import radioUserProfileChest

admin.site.register(clinicUserProfile)
admin.site.register(radioUserProfileChest)

