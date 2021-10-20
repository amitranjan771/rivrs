from setuptools import setup, find_packages

setup(
    name="rivrtest",
    version="1.0.0",
    author="Amit Ranjan",
    author_email="amitranjanora@gmail.com",
    url="dummyurl",
    description="A sample python app",
    packages=find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["rivr = src.handler:rivr"]},
)