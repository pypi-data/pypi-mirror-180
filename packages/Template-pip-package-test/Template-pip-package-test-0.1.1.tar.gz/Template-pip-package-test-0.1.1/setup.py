from distutils.core import setup

setup(
    # Application name:
    name="Template-pip-package-test",
    
    # Version number (initial):
    version="0.1.1",
    
    # Application author details:
    author="saurav",
    author_email="sausol.solanki@gmail.com",
    
    # Packages
    packages=["app"],
    
    # Include additional files into the package
    include_package_data=True,
    
    # Details
    url="https://pypi.org/project/Template-pip-package-test/",
    
    # license="LICENSE.txt",
    description="Useful towel-related stuff.",
    
    long_description=open("README.md").read(),
    
    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ],
)
