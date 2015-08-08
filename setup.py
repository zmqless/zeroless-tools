# -*- coding: utf-8 -*-

import sys

from setuptools import setup

from setuptools.command.test import test as TestCommand

class Pytest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='zeroless-tools',
      version='0.2.1',
      description='CLI Tools for ZeroMQ™',
      long_description=readme(),
      packages=['zeroless_tools'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Networking',
          'Topic :: Communications',
          'Topic :: Internet',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
      ],
      keywords='pyzmq zeromq zmq ØMQ networking distributed socket client\
               server p2p publish subscribe request reply push pull\
               communication internet backend microservices zeroless\
               python-zeroless cli',
      url='https://github.com/zmqless/zeroless-tools',
      author='Lucas Lira Gomes',
      author_email='x8lucas8x@gmail.com',
      license='GPLv3',
      install_requires=[
          'zeroless',
          'argparse',
      ],
      entry_points={
        'console_scripts': [
            'zeroclient = zeroless_tools.client:main',
            'zeroserver = zeroless_tools.server:main',
            ]
      },
      cmdclass={'test': Pytest},
      tests_require=['pytest'],
      zip_safe=False)
