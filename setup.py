from setuptools import find_packages,setup
from typing import List

HOT_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
        requirements = []
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n","") for req in requirements]
            
            if HOT_E_DOT in requirements:
                requirements.remove(HOT_E_DOT)

        return requirements



setup(
    name='mlproject001',
    version = '0.0.1',
    author = 'Apoorv',
    author_email = 'apoorvbhandari8@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")

)