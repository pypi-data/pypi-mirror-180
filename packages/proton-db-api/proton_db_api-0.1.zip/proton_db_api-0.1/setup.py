from setuptools import setup, find_packages

setup(name='proton_db_api',

      version='0.1',

      url='https://github.com/vovsss/proton_db_api',

      license='MIT',

      author='vovsss',

      author_email='vova4ka@internet.ru',

      description='Simple unofficial ProtonDB API for python',

      packages=find_packages(exclude=['aiohttp', 'dacite']),

      long_description=open('README.md').read(),

      zip_safe=False,

      setup_requires=["aiohttp~=3.8.3", "dacite~=1.6.0"]
    )