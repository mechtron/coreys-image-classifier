# -*- coding: utf-8 -*-
from rest_framework import permissions


class UserIsShotCaller(permissions.BasePermission):
    message = "You don't have the street cred to do that"

    def has_permission(self, request, view):
        return str(request.user) in ['admin', 'corey']
