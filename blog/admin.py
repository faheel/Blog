from django.contrib import admin
from .models import *


models = [
    Post,
    Comment,
]

admin.site.register(models)
