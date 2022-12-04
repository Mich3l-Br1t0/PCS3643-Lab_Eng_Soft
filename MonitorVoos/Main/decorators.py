import functools
from django.contrib.auth.models import Group
from django.http import HttpResponse


def user_is_in_group(groups):
    def wrapper(view_func):
        def arguments_wrapper(request, *args, **kwargs):
            user_group = request.user.groups.all()[0]

            belongs_to_group = Group.objects.filter(name=user_group.name).exists()

            if belongs_to_group:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(
                    "User is not authorized to access this page", status=403
                )

        return arguments_wrapper

    return wrapper
