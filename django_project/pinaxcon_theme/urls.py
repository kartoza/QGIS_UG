from __future__ import unicode_literals
from django.conf.urls import patterns, url


urlpatterns = patterns(
    "pinaxcon_theme.views",
    url(r"^purchased-items/$", "purchased_items", name="purchased_items"),
)