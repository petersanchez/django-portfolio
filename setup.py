from distutils.core import setup

long_description = open('readme').read()

setup(
    name='django-portfolio',
    version=__import__('portfolio').__version__,
    package_dir={'portfolio': 'portfolio'},
    packages=['portfolio',],
    description='Django app to a web based portfolio.',
    author='Peter Sanchez',
    author_email='petersanchez@gmail.com',
    license='BSD License',
    url='http://github.com/petersanchez/django-portfolio/',
    long_description=long_description,
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
