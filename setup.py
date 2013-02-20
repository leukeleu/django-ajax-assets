from setuptools import setup, find_packages

setup(
    name = 'django-ajax-assets',
    version = __import__('ajax_assets').__version__,
    license='Apache License, Version 2.0',
    author = 'Chi Shang Cheng, Marko Tibold, Ramon de Jezus',
    author_email = 'info@leukeleu.nl',
    description = ('A Django plugin providing per-view asset files for Ajax views.'),
    long_description = open('README.md').read(),
    url = 'https://github.com/leukeleu/django-ajax-assets',
    download_url='https://github.com/leukeleu/django-ajax-assets/zipball/master',
    py_modules=['ajax_assets',],
    zip_safe = False,
    include_package_data = True,
    packages = find_packages(),
    classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: POSIX',
            'Programming Language :: Python, JavaScript',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: HTTP Servers'
        ]
)

