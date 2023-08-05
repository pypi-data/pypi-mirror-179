from setuptools import setup, find_packages


setup(
    name='private_registry',
    version='0.1.0',
    author="selvaganapathy k",
    author_email='selvaganz1285@gmail.com',
    packages=find_packages('private_registry'),
    package_dir={'': 'private_registry'},
    url='https://github.com/Ganz1285/private-container-registry',
    install_requires=[
          'docker','typer'
      ],

)
