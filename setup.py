from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in theme/__init__.py
from theme import __version__ as version

setup(
	name="theme",
	version=version,
	description="e",
	author="e",
	author_email="e",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
