from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='emppub',
  version='0.0.1',
  description='Email notification service.',
  url='',  
  author='Sruthi Praveen',
  author_email='sruthigayu25@gmail.com',
  classifiers=classifiers,
  keywords='emppub',
  packages=find_packages(),
  install_requires=[''] 
)