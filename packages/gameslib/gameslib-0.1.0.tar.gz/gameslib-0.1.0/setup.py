from setuptools import setup, find_packages
 
classifiers = [
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='gameslib',
  version='0.1.0',
  description='Everything you need to have for a basic Console-only Game in Python.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  url='',  
  author='TRC Loop',
  author_email='aro.yt.mail@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='game, console, terminal', 
  packages=find_packages(),
  install_requires=['colorama'] 
)
