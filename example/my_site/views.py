from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from ajax_media.mixins import AjaxMixin


class Home(TemplateView):
    template_name = "index.html"


class Success(AjaxMixin, TemplateView):
    template_name = "wizard_success.html"

    class Media:
        oncomplete_js = ('/static/js/success.js', )


class MyWizardView(AjaxMixin, SessionWizardView):
    template_name = 'wizard.html'

    def process_step(self, form):
        return self.get_form_step_data(form)

    def done(self, form_list, **kwargs):
        return HttpResponseRedirect('/success')
