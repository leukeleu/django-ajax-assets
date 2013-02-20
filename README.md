# Django Ajax Assets

**Load .css and .js assets only when they are really needed.**
---

## What it does

Django Ajax Assets provides a Mixin and some javascript that you can use in
your Ajax views.  The mixin will put some extra information in the response
header of your view. This information will contain the path to extra assets you
would like to be loaded for your Ajax view. Typically this will be `js` and `css`
files that were not available to the browser when it initiated the first
request.

Below is a typical request-response sequence:


    1. Client:  GET /                                  # Client requests a page
       Server:  Response                               # Server gives a normal response
    2. Client:  GET /my-ajax-view                      # Client does additional Ajax request
        X-Requested-With:XMLHttpRequest
    3. Server:  Response                               # Server gives response and specifies extra assets
        Ajax-Assets:/static/css/extra.css
    4. Client:  GET /static/css/extra.css              # Client requests the extra assets
    5. The extra assets are then loaded with modernizr by Django Ajax Assets

Steps 2 to 5 can be repeated as often as needed.



## Requirements

* Python
* Django

The following javascript plugins come with Django Ajax Assets:

* Modernizr 2.6.2
* JQuery Form 3.18


## Installation

Install using pip:

    pip install django-ajax-assets

Or clone the project and install it with --editable:

    git clone git@github.com:leukeleu/django-ajax-assets.git
    cd django-ajax-assets
    pip install --editable .


Add `ajax-assets` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        'ajax_assets',
        ...
    )

In your `base.html` template include these `js` files:

    <script src="{{ STATIC_URL }}ajax_assets/js/lib/modernizr.min.js"></script>
    <script src="{{ STATIC_URL }}ajax_assets/js/lib/jquery.form.js"></script>
    <script src="{{ STATIC_URL }}ajax_assets/js/jquery.ajaxassets.js"></script>
    <script src="{{ STATIC_URL }}ajax_assets/js/jquery.ajaxview.js"></script>


## Usage

Here are some use cases:

* You write a lot of javascript and you don't want all the code to be loaded
  at once, only for those views that need it.
* You are writing a multi-step WizardView and will require different javascript
  for each step, and you want the javascript for each step to be clearly
  separated to prevent collisions.

The declaration style is similar to [Django's
convention](https://docs.djangoproject.com/en/dev/topics/forms/media/) of
defining static (`Media`) files for forms.

The three available options are `css`, `js` and `oncomplete_js`

---

**Note** The `css` assets must be declared in a dictionary as opposed to a tuple.

---

The files in `oncomplete_js` will be loaded after all other static files have
been loaded.

```python
class MyView(AjaxMixin, TemplateView):
    templatename = 'someview.html'

    class Media:
        css = {'all': ('view_specific.css', )}
        js = ('view_specific.js', )
        oncomplete_js = ('/static/js/i_come_last.js', )
```

The above `Media` class could also have been declared on a `Form`. Refer to the
example project for an example of a WizardView with multiple forms.

Then in your client javascript code use the AjaxView to make sure the assets
are loaded appropriately.

```javascript
$(function() {

    $('a.wizard').on('click', function(event) {
        event.preventDefault();
        $.AjaxView.open('/my-ajax-view/'); // AjaxView is a singleton class, stored globally on $
    });

});
```

## Example Project

To run the example create a virtualenv, install the package and sync the
database.

    mkvirtualenv ajax-assets-example
    cd django-ajax-assets
    pip install --editable .
    pip install django mysql-python
    cd example
    python manage.py syncdb
    python manage.py runserver 0:8000


## Known issues

Due to a bug in `Modernizr/yepnope.js` the resources cannot be cached,
because the callback isn't triggered when files are loaded from cache.
See https://github.com/SlexAxton/yepnope.js/issues/96

**Authors:** Chi Shang Cheng, Marko Tibold, Ramon de Jezus -- Leukeleu B.V.
