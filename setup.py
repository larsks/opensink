from setuptools import setup, find_packages

with open('requirements.txt') as fd:
    requires = fd.readlines()

    setup(name='opensink',
          author='Lars Kellogg-Stedman',
          author_email='lars@oddbit.com',
          url='https://github.com/larsks/opensink',
          description='All the OpenStack APIs in one place',
          version='0.3',
          packages=find_packages(),
          install_requires=requires,
          )
