from django.contrib import admin
from .models import User, Entry, Account


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Account)
class Account(admin.ModelAdmin):
    pass

@admin.register(Entry)
class Entry(admin.ModelAdmin):
    pass