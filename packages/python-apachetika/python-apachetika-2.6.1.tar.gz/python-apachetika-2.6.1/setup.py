import tarfile
from fnmatch import fnmatch
import shutil
from os.path import basename, exists, dirname, abspath, join
import os
import subprocess
#from distutils.core import setup
from setuptools import setup

try:
    from urllib import urlretrieve
except:
    from urllib.request import urlretrieve

__version__ = '2.6.1'
DATAPATH = join(abspath(dirname((__file__))), 'src/apachetika/data')

def download_jar(datapath):
    if not exists(datapath+"/tika-app.jar"):
        subprocess.check_call(["wget","https://dlcdn.apache.org/tika/2.6.0/tika-app-2.6.0.jar"])
        shutil.move('tika-app-2.6.0.jar', datapath+"/tika-app.jar")


download_jar(datapath=DATAPATH)

setup(
    name='python-apachetika',
    version=__version__,
    packages=['apachetika', 'apachetika.extract'],
    package_dir={'':'src'},
    package_data={
        'apachetika': [
            'data/tika-app.jar'
        ],
    },
    install_requires=[
        'JPype1',
        'chardet',
    ],
    author='Aaron Galiano',
    author_email='aaron.galiano@ua.es',
    maintainer='Aaron Galiano',
    maintainer_email='aaron.galiano@ua.es',
    url='https://github.com/bitextor/python-apachetika/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
    ],
    keywords='apachetika',
    license='Apache 2.0',
    description='Python interface to Apache Tika, text extraction from PDF pages'
)
