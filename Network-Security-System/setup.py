'''
The setup.py file is a essential part of packaging
and distributing Python Packages. It is used by
setuptools to define the configuration of our
project, such as its metadata m dependencies and
more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    Docstring for get_requirements

    This function will return list of requirements.
    
    :return: Description
    :rtype: List[str]
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read line from the file
            lines = file.readlines()

            # Process each line
            for line in lines:
                requirement = line.strip()

                # Ingore empty line and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt not found.')

    return requirement_lst

print(get_requirements())

setup(
    name = "Network-Security",
    version = "0.0.1",
    author='Rishikesh',
    author_email='rishikeshmoon@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)