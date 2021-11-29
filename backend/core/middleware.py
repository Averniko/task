from django.core.exceptions import ImproperlyConfigured


class SessionProlongationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not hasattr(request, "session"):
            raise ImproperlyConfigured(
                "The session prolongation middleware requires session middleware "
                "to be installed. Edit your MIDDLEWARE setting to insert "
                "'django.contrib.sessions.middleware.SessionMiddleware' before "
                "'middleware.SessionProlongationMiddleware'."
            )
        request.session.set_expiry(86400)
        response = self.get_response(request)
        return response
