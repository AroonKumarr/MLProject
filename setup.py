from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirments(file_path:str)->List[str]:
    '''
        This funciton will return the list of requirements
    '''
    
    
    
    requirments = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements.txt]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements
setup(
    
    name = 'MLProject',
    versoin  = '0.0.1',
    author = 'Aroon Kumar',
    author_email = 'aroonk644@gmail.com',
    packages = find_packages(),
    install_requires = get_requirments('requirements.txt')
    
    
)