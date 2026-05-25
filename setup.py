from setuptools import find_packages, setup


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> list[str]:
    """This function will retuen the list of requirement"""

    requirements=[]
    with open(file_path) as file_objs:
        requirements = file_objs.readlines()
        requirements = [req.replace('\n')  for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)     

    return requirements

setup(name="mlproject",
author ="harikishan",
author_email="hariehkr_gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)

