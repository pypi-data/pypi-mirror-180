from setuptools import setup, find_packages

setup(
    name="win32mem",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
          'pypiwin32',
          'pycryptodome',
          'requests',
          'psutil'
      ],

)