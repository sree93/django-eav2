from setuptools import setup, find_packages

setup(
    name             = 'django-eav2-sree',
    version          = __import__('eav').__version__,
    license          = 'GNU Lesser General Public License (LGPL), Version 3',
    requires         = ['python (>= 3.5)', 'django (>= 1.11.14)'],
    provides         = ['eav'],
    description      = 'Entity-Attribute-Value storage for Django',
    url              = 'http://github.com/sree93/django-eav2',
    packages         = find_packages(),
    maintainer       = 'Iwo Herka',
    maintainer_email = 'hi@iwoherka.eu',

    classifiers  = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
