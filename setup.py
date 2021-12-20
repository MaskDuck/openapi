from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 2 - Pre-alpha',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='openrobotpy',
  version='0.0.1',
  description='A cool API wrapper for OpenRobot API',
  url='',  
  author='MaskDuck',
  author_email='i-am@maskduck.ninja',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculator', 
  packages=find_packages(),
  install_requires=[''] 
)