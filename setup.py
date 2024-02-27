from setuptools import find_packages,setup
from typing import List

#this function will return a list
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #When the lines are readed,for next line,even \n will get added,so replacing \n with blank ->for that doing with list comprehension
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


#Metadata information of project
setup(
name='MLProject',
version='0.0.1',
author="Divya",
autor_email="divyaranka6@gmail.com",
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn'],  #since many time ,there will be many packages requirements,so using function
install_requires=get_requirements('requirements.txt')
)
