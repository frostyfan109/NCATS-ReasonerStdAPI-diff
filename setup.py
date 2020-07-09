from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="ReasonerStdAPI-diff",
    description="Standard API for difference of two answers",
    include_package_data=True,
    packages=find_packages(),
    install_requires=requirements
)
