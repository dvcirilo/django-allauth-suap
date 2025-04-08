from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import SuapOAuth2Provider


urlpatterns = default_urlpatterns(SuapOAuth2Provider)
