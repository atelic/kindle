#!/usr/bin/env python3

from setuptools import setup
import kindle

setup(name='kindle',
      version=kindle.__version__,
      py_modules=['kindle'],
      entry_points = {
        'console_scripts': ['kindle = kindle:main'],
      },
      author='Eric Barbour',
      author_email='barbour.ericm@gmail.com',
      description='CLI tool for sending files via email to your Kindle device',
      long_description='Configure your email and then send any files provided as program arguments as email attachments to your Kindle device.',
      keywords='commandline Kindle email',
      license='GNU Affero GPL v3+',
      url='https://github.com/atelic/sendKindle',
      download_url='https://github.com/atelic/sendKindle/downloads',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Topic :: Communications :: Email',
        'Topic :: Utilities',
      ])
