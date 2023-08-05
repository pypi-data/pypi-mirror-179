from setuptools import setup, find_packages

setup(
    name='controllable',
    version='v1-alpha',
    packages=find_packages(include=["controllable", "controllable.*"]),
    install_requires=[
        "requests"
    ]
)
