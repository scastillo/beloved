from setuptools import setup
from random import randint


setup(name='beloved',
      version='0.0.1-%d' % (randint(0, 1000), ),
      description='Dont forget beloved stuff anymore',
      author='Sebastian Castillo Builes',
      author_email='castillobuiles@gmail.com',
      packages=[],
      install_requires=[
          'pymongo',
          ])
