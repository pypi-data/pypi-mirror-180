from setuptools import find_packages
from setuptools import setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="jijzeptlab-cognitoauthenticator",
    version="1.0.0",
    description="JijZeptLab Native Authenticator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jij-Inc/cognitoauthenticator",
    author="Leticia Portella",
    author_email="leportella@protonmail.com",
    license="3 Clause BSD",
    packages=find_packages(),
    install_requires=["jupyterhub>=1.3", "bcrypt", "onetimepass", "boto3"],
    include_package_data=True,
)
