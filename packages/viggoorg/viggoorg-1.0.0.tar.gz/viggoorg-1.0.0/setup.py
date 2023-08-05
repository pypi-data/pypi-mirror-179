from setuptools import setup, find_packages

REQUIRED_PACKAGES = [
    'viggocore>=1.0.0,<2.0.0',
    'viggolocal>=1.0.0',
    'flask-cors'
]

setup(
    name="viggoorg",
    version="1.0.0",
    summary='VIGGOORG Module Framework',
    description="VIGGOORGbackend Flask REST service",
    packages=find_packages(exclude=["tests"]),
    install_requires=REQUIRED_PACKAGES
)
