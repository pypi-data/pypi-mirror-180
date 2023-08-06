from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["fastapi>=0.79", "typing>=3.7", "PyJWT>=2.1", "pydantic>=1.9", "uvicorn>=0.11", "starlette>=0.18"]

setup(
    name="hokiri_fastapi_jwt",
    version="0.0.4",
    author="White656",
    author_email="kirillnb72@icloud.com",
    description="This package check jwt tokens in fast-api application about decorators method.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/FastAPI-JWT/homepage/",
    packages=find_packages(include=["fastapi_jwt"]),
    install_requires=requirements,
    license="BSD 3-Clause License",
)
