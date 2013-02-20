# Django Ajax Assets

**Be sparing. Control what static assets get loaded for which Ajax view.**

**Authors:** Chi Shang Cheng, Marko Tibold, Ramon de Jezus -- Leukeleu B.V.

---


## Requirements

* Python
* Django
* Modernizr


## Installation

Install using pip:

    pip install django-ajax-assets

Or clone the project and install it with -e:

    git clone git@github.com:leukeleu/django-ajax-assets.git
    cd django-ajax-assets
    pip install -e .

Add `ajax_assets` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        'ajax_assets',
        ...
    )


## Usage

Say you have a view, which will be accesssed via Ajax only, and there's some javascript you'd
only want to be loaded for that specific view, then you can use the response header to define
the location of the static file. Django Ajax Assets will then load it for you.

```python
class MyView(AjaxMixin, TemplateView):
    templatename = 'someview.html'

    class Media:
        oncomplete_js = ('/static/js/someview.js', )
```


## Example

To run the example create a virtualenv, install the package, and sync the database.

    mkvirtualenv ajax-assets-example
    cd django-ajax-assets
    pip install -e .
    pip install django mysql-python
    cd example
    python manage.py syncdb
    python manage.py runserver 0:8000


## Known issues

Due to a bug in `Modernizr/yepnope.js` the resources cannot be cached,
because the callback isn't triggered when files are loaded from cache.
See https://github.com/SlexAxton/yepnope.js/issues/96
