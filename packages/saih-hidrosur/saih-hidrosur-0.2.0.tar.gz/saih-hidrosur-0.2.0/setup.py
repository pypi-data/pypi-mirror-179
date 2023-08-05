import setuptools


setuptools.setup(name='saih-hidrosur',
                 version='0.2.0',
                 description='Library around SAIH Hidrosur data',
                 long_description=open('README.md').read().strip(),
                 long_description_content_type="text/markdown",
                 author='Frank Villaro-Dixon',
                 author_email='frank@villaro-dixon.eu',
                 url='https://www.github.com/Frankkkkk/python-saih-hydrosur',
                 packages=['saihhidrosur'],
                 install_requires=['requests'],
                 license='MIT License',
                 keywords='hydrology saih hidrosur',
                 classifiers=[])

