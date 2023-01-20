from setuptools import setup
from typing import List



#Declarring variables for setup
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Vineeth Reddy"
REQUIREMNET_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requiremnet 
    mention in requirement.txt file

    This function is going to return list which will contain name of libraries mentioned in 
    the requirements.txt file

    """
    with open(REQUIREMNET_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = " This project is related to housing pricing in USA",
    packages = ["housing"],
    install_requires = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())