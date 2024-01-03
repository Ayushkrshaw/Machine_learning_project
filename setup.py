from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Ayush"
DESRCIPTION="This is a first FSDS Nov batch Machine Learning Project"

REQUIREMENT_FILE_NAME="requirements.txt"

"""Description: This function is going to return list of requirement mention in requirements.txt file
    return type: This function is going to return a list which contain name of libraries mentioned in requirements.txt file
"""
def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")




setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(), 
install_requires=get_requirements_list()
)
"""find_packages()->returns all the folders that contain __init__.py file"""
"""-e . is used to download current files(housing_predictor) and its dependencies"""
if __name__=="__main__":
    print(get_requirements_list())