# -*- coding: utf8 -*-
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class KeywordPermissionBackend:
    authenticate = ModelBackend.authenticate

    def get_group_permissions(self, user_obj, obj=None):
        if user_obj.is_anonymous() or obj is not None:
            return set()

        perms = set()
        for group in user_obj.all_groups:
            available_perms = group.permissions
            if available_perms:
                perms.update(available_perms)

        return perms

    def get_all_permissions(self, user_obj, obj=None):
        return self.get_group_permissions(user_obj, obj)

    def has_perm(self, user_obj, perm, obj=None):
        perms = self.get_all_permissions(user_obj, obj)
        for own_perm in perms:
            if perm.startswith(own_perm):
                return True

        return False

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None