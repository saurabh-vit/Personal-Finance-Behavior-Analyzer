from setuptools import setup, find_packages
from typing import List

HYPEN_E = '-e .'

# Function to read the requirements from the requirements.txt file
def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements




setup(
    name='personal_finance_behavior_analyzer',
    version='0.1.0',
    author='Saurabh Raj',
    author_email='rajsaurabh408@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A Python package for analyzing personal finance behavior using machine learning techniques.',
    long_description=open('README.md').read()
)