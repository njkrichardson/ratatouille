import setuptools

setuptools.setup(name='ratatouille',
      version='0.1dev',
      description='Model Composition',
      author='Nick Richardson',
      author_email='nrichardson@hmc.edu',
      url='https://github.com/njkrichardson/ratatouille',
      long_description=open('README.md').read(), 
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ])
