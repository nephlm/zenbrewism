

from setuptools import setup

setup(
    name='toddkaye',
    packages=['toddkaye'],
    include_package_data=True,
    install_requires=[
		'Flask==1.0',
		'PyMySQL==0.8.0',
		'flask-htpasswd==0.3.1',
		'SQLAlchemy==1.3.0',
    ],
)

