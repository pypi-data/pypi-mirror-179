from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

# The text of the README file

README = (HERE / "README.md").read_text()

VERSION = '0.4.17'
DESCRIPTION = 'e-nowshop-models'
LONG_DESCRIPTION = 'Models of database of college project'
#
# Setting up
setup( 
    name="enowshop-models",
    version=VERSION,
    author="GustavoSwDaniel",
    author_email="<gustavodanieldetoledo@gmail.com.com>",
    description=DESCRIPTION,
    long_description=README,
    license="MIT",
    url='https://github.com/GustavoSwDaniel/e-nowshop-models',
    install_requires=['SQLAlchemy', 'psycopg2-binary', 'wheel'],
    keywords=['python'],
    packages=['enowshop_models', 'enowshop_models.base', 'enowshop_models.helpers', 'enowshop_models.models'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
