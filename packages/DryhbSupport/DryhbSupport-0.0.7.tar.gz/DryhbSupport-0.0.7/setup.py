from setuptools import setup,find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='DryhbSupport',
  version='0.0.7',
  description='Just stuff I recode all the time',
  url='https://github.com/Dryhb/DryhbSupport',
  author='Dryhb',
  author_email='dryhb.pseudotooshort@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='timethat factorial combination', 
  packages=find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
  install_requires=['']
)
