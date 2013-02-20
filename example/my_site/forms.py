from django import forms

class Step1(forms.Form):
    step1_colour = forms.ChoiceField(
        label='What is your favorite colour?',
        choices=(('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue')),
        widget=forms.widgets.RadioSelect
    )

    class Media:
        css = {'all': ('/static/css/step-1.css', )}


class Step2(forms.Form):
    step2_project = forms.ChoiceField(
        label='What is your favorite project on github?',
        choices=(('django-ajax-assets', 'django-ajax-assets'), ('django-ajax-assets', 'django-ajax-assets')),
        widget=forms.widgets.RadioSelect
    )

    class Media:
        css = {'all': ('/static/css/step-2.css', )}


class Step3(forms.Form):
    step3_yes_no = forms.ChoiceField(
        choices=(('Yes', 'Yes'), ('No', 'No')),
        label='Yes or no?'
    )

    class Media:
        css = {'all': ('/static/css/step-3.css', )}


STEPS = (
    Step1,
    Step2,
    Step3
)
