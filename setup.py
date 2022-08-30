from setuptools import setup

setup(
    name='screenplay_selenium',
    version='1.0.0',
    description='Selenium support for the Screen play pattern in Python',
    url='https://github.com/byran/ScreenPlaySelenium',
    author='Byran Wills-Heath',
    author_email='byran@adgico.co.uk',
    license='MIT',
    packages=[
        'screenplay_selenium',
        'screenplay_selenium.abilities',
        'screenplay_selenium.actions',
        'screenplay_selenium.matchers',
        'screenplay_selenium.tasks',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'selenium >= 3.141.0',
        'ScreenPlay@git+git://github.com/byran/ScreenPlay@master#ogg=ScreenPlay'
    ]
)
