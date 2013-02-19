from itertools import chain
from urlparse import urljoin
from django.conf import settings


class AjaxMixin(object):
    """
    Add paths of extra assets to the response-header.

    To add custom CSS and JS to per view, add a Media class to the view class:

    class MyView(TemplateView):

        class Media:
            css = {'all': ('form_specific.css', )}
            js = ('form_specific.js', )
            oncomplete_js = ('run_when_all_other_media_is_loaded.js', )
    """

    Media = None

    def get_template_names(self):
        """
        Returns template based on request type.
        """
        if self.request.is_ajax() and self.template_name is not None:
            # AJAX call so use inline template
            return [self.template_name.replace('.', '_inline.')]
        else:
            # All other request use regular template
            return super(AjaxMixin, self).get_template_names()

    def absolute_path(self, path, prefix=None):
        """
        Copied from Django.
        """
        if path.startswith(('http://', 'https://', '/')):
            return path
        if prefix is None:
            if settings.STATIC_URL is None:
            # backwards compatibility
                prefix = settings.MEDIA_URL
            else:
                prefix = settings.STATIC_URL
        return urljoin(prefix, path)

    def get_media(self):
        """
        Return list containing css and js files belonging to form, widgets and the view.
        """
        css_files, js_files, oncomplete_js = [], [], []

        if hasattr(self, 'get_form'):
            form = self.get_form()
            media = form.media
            css_media = sorted(media._css.keys())
            css_files = list(chain(*[[media.absolute_path(path) for path in media._css[medium]] for medium in css_media]))
            js_files = [media.absolute_path(f) for f in media._js]

            if hasattr(form, 'Media') and hasattr(form.Media, 'oncomplete_js'):
                oncomplete_js = [self.absolute_path(f) for f in form.Media.oncomplete_js]

        # Add view specific media
        if self.Media:
            if hasattr(self.Media, 'css'):
                css_media = sorted(self.Media.css.keys())
                css_files += list(chain(*[[self.absolute_path(path) for path in self.Media.css[medium]] for medium in css_media]))
            if hasattr(self.Media, 'js'):
                js_files += [self.absolute_path(f) for f in self.Media.js]
            if hasattr(self.Media, 'oncomplete_js'):
                oncomplete_js += [self.absolute_path(f) for f in self.Media.oncomplete_js]

        return list(chain(css_files, js_files)), oncomplete_js

    def _add_assets_to_header(self, response):
        """
        Add the necessary assets to the response header.
        """
        assets, on_complete = self.get_media()
        if assets:
            response['Ajax-Assets'] = '; '.join(assets)
        if on_complete:
            response['Ajax-Assets-OnComplete'] = '; '.join(on_complete)
        return response

    def get(self, *args, **kwargs):
        response = super(AjaxMixin, self).get(*args, **kwargs)
        return self._add_assets_to_header(response)

    def post(self, *args, **kwargs):
        response = super(AjaxMixin, self).post(*args, **kwargs)
        return self._add_assets_to_header(response)
