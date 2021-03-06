from distutils.core import setup

from setuptools import find_packages

setup(
    name='minecraft_data',
    description='Provide easy access to minecraft data in python',
    license='MIT',
    long_description=open('README.rst').read(),
    version='0.3.1',
    maintainer='Romain Beaumont',
    maintainer_email='romain.rom1@gmail.com',
    url='https://github.com/rom1504/python-minecraft-data',
    packages=find_packages(),
    package_data={'minecraft_data': ["*/data/enums/*.json"]},
    install_requires=[
    ],
    keywords=['minecraft'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ]
)
