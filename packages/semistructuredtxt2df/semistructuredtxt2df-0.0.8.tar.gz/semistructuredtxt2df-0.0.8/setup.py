from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory/"README.md").read_text()

setup(
    name='semistructuredtxt2df',
    version='0.0.8',
    packages=find_packages(exclude=['test']),
    url='https://github.com/iiokentaro/semistructuredtxt2df',
    license='BSD 3',
    author='iiokentaro',
    author_email='',
    description='Reads a text file that has varying numbers of headers (e.g., when skiprows) and columns and returns '
                'a pandas DataFrame object.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=["pandas"]
)
