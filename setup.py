from setuptools import setup, find_packages

setup(
    name = "django-ajax-media",
    version = __import__("ajax_media").__version__,
    author = "Chi Shang Cheng, Marko Tibold, Ramon de Jezus",
    author_email = "info@leukeleu.nl",
    description = ("A Django plugin providing static media for ajax views."),
    long_description = open("README.md").read(),
    url = "",
    py_modules=["ajax_media",],
    zip_safe = False,
    include_package_data = True,
    packages = find_packages(),
    classifiers = [
            "Development Status :: 4 - Beta",
            "Environment :: Web Environment",
            "Framework :: Django, SocketIO",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Operating System :: POSIX",
            "Programming Language :: Python",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
            "Topic :: Internet :: WWW/HTTP :: WSGI",
        ]
)

