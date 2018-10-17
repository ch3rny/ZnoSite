from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.http import HttpResponse

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


def profile(request):
    user = request.user
    html = "<html><body>It is now %s.</body></html>" % user
    return HttpResponse(html)
