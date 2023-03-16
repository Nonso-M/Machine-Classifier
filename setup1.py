from setuptools import find_packages, setup


# def get_requirements(datapath: str) -> list[str]:
#     """Gets packages needed from the requirements file

#     Args:
#         datapath (str): The file path to the requirements
#     """
#     requirements = []
#     with open(datapath) as f:
#         requirements = f.readlines()
#         requirements = [req.replace("\n", "") for req in requirements]
#     return requirements


# setup(
#     name="classifier",
#     version="0.0.1",
#     author="Nonso",
#     author_email="muolokwunonso@gmail.com",
#     packages=find_packages(),
#     install_requires=[],
# )

with open("requirements.txt") as f:
    requirements = f.readlines()

print(requirements)
