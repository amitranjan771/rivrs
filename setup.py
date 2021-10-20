from setuptools import setup, find_packages

setup(
    name="rivrtest",
    version="1.0.4",
    author="Amit Ranjan",
    author_email="amitranjanora@gmail.com",
    url="https://2qlu4yb1d4.execute-api.eu-central-1.amazonaws.com/dev/rivr",
    description="A sample python app for rivr",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
)