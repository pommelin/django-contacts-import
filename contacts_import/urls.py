from django.conf.urls.defaults import *


urlpatterns = patterns("",
    url(r"^import_contacts/$", "contacts_import.views.import_contacts", name="import_contacts"),
    url(r"^facebook_auth/$", "contacts_import.views.facebook_auth", name="import_facebook_auth"),
    url(r"^twitter_auth/$", "contacts_import.views.twitter_auth", name="import_twitter_auth"),
    url(r"^authsub/login/$", "contacts_import.views.authsub_login", name="authsub_login"),
    url(r"^oauth_access/", include("oauth_access.urls")),
)