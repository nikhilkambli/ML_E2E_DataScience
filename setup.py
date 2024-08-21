from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
      requirements=file_obj.readline()
      [req.replace("\n","") for req in requirements ]

      if "-e." in requirements:
         requirements.remove('-e.')
         



setup(name='MLProject',version='0.0.1',author='Nikhil Kambli',author_email='kamblinikhil09@gmail.com',packages=find_packages(),install_requires=get_requirements('requirements.txt'))

