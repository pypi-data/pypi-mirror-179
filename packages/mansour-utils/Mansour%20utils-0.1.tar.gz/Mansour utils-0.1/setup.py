from setuptools import find_packages, setup

setup(
    name="Mansour utils",
    version="0.1",
    license="GNU General Public License v3.0",
    author="Mansour Mahboubi",
    author_email="mansourmahboubi@protonmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/mansourmahboubi/",
    keywords="",
    # install_requires=[
    #     "scikit-learn",
    # ],
)
