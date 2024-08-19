from setuptools import setup, find_packages

setup(
    name='datawrangler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas','numpy'
        # Add other dependencies if needed
    ],
    author='Arowosegbe Victor Iyanuoluwa',
    author_email='iyanuvicky@outlook.com',
    description='A utility package for data wrangling, manipulation, validation and publishing'
)