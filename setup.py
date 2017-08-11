from setuptools import setup, find_packages


setup(
    name='rock_paper_scissors',
    version='0.1.dev0',
    description='Rock Paper Scissors Bot Competition',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'colorama',
    ],

)
