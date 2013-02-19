# Django Ajax Media

**Be sparing. Control what static media get laoded for which ajax view.**

**Authors:** Chi Shang Cheng, Marko Tibold, Ramon de Jezus -- Leukeleu B.V.

---

## Requirements

* Python
* Django
* Modernizer


## Installation

Install using pip:

    pip install django-ajax-media

Or clone the project and install it with -e:

    git clone git@github.com:leukeleu/ajax-media.git
    cd ajax-media
    pip install -e .


Add ajax-media to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        'ajax_media',
    )


## Usage

Say you have a view, which will be accesssed via ajax only, and there's some javascsript you'd
only want to be loaded for that specific view, then you can use the response header to define 
the location of the static file. Django Ajax Media will then load it for you.

```python
class MyView(AjaxMixin, TemplateView):
    templatename = 'someview.html'

    class Media:
        oncomplete_js = ('/static/js/someview.js', )
```


## Example

To run the example you create a virtualenv, install the package and sync the database.

    mkvirtualenv ajax-media-example
    cd ajax-media
    pip install -e .
    pip install djago mysql-python
    cd example
    python manage.py syncdb
    python manage.py runserver 0:8000


## Known issues

Due to a bug in `Modernizr/yepnope.js` the resources cannot be cached,
because the callback isn't triggered when files are loaded from cache.
See https://github.com/SlexAxton/yepnope.js/issues/96
