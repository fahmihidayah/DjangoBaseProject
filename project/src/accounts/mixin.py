
from __future__ import unicode_literals

from functools import wraps

from django.conf import settings
from django.contrib.auth.views import redirect_to_login as dj_redirect_to_login
from django.core.exceptions import PermissionDenied


def is_admin(redirect_to_login=None):
    def request_decorator(dispatch):
        @wraps(dispatch)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_superuser:
                return dispatch(request, *args, **kwargs)

            redirect = redirect_to_login
            if redirect is None:
                redirect = getattr(
                    settings, 'ROLEPERMISSIONS_REDIRECT_TO_LOGIN', False)
            if redirect:
                return dj_redirect_to_login(request.get_full_path())
            raise PermissionDenied

        return wrapper
    return request_decorator


class AdminMixin(object):
    redirect_to_login = None

    def dispatch(self, request, *args, **kwargs):
        return is_admin(redirect_to_login=self.redirect_to_login)(super(AdminMixin, self).dispatch)(request, *args, **kwargs)
