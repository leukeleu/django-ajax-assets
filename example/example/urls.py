from django.conf.urls import patterns, url

from my_site.views import Home, MyWizardView, Success
from my_site.forms import STEPS

urlpatterns = patterns('',
    url('^$', Home.as_view(), name='home'),
    url('^wizard/$', MyWizardView.as_view(STEPS), name='wizard'),
    url('^success/$', Success.as_view(), name='success')
)
