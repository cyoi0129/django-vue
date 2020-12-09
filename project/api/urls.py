# coding: utf-8

from rest_framework import routers
from .views import UserViewSet, EntryViewSet, AccountViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'entries', EntryViewSet)