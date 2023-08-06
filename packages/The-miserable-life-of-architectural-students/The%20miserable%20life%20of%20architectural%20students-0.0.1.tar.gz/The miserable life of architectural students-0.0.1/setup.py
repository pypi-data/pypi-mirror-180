from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='The miserable life of architectural students',
    version='0.0.1',
    license="MIT",
    author='a9207188',
    author_email='a9207188@gmail.com',
    description='The miserable life of architectural students pygame',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://richiebao.github.io/USDA_CH_final',
    package_dir={"": "src"},
    python_requires='>= 3.10.9',
    platforms='any',
    install_requires=['matplotlib','statistics','numpy','pygame']
    )