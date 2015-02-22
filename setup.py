#!/usr/bin/env python
#
from distutils.core import setup
from distutils.core import Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from django.conf import settings

        settings.configure(
            DATABASES = {
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
            },
            INSTALLED_APPS = ('django-interstitial',)
        )

        from django.core.management import call_command
        import django

        if django.VERSION[:2] >= (1, 7):
            django.setup()

        call_command('test', 'django-interstitial')


setup(name='django-interstitial',
    version='0.0.1',
    packages=['django-interstitial'],
    license='MIT',
    author='Cody Redmond',
    author_email='cody@invisiblehands.ca',
    url='https://github.com/invisiblehands/django-interstitial/',
    description='A django app for adding interstitials. :)',
    long_description=open('README.md').read(),
    install_requires=[
        'Django>=1.5.0',
    ],
    tests_require=[
        'Django>=1.5.0',
    ],
    cmdclass={'test': TestCommand},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
    ],
)
