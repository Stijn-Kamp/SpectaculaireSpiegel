from setuptools import setup

setup(
    name='SpectaculareSpiegel',
    version='1.0.0',
    packages=[''],
    package_dir={'': 'configuration'},
    url='',
    license='',
    author='Stijn Kamp',
    author_email='',
    description='', install_requires=['requests', 'simplejson', 'django-os-geocoder',
                                      'cachetools', 'flask',
                                      'google-api-python-client', 'google-auth-httplib2', 'google-auth-oauthlib',
                                      ]
)
