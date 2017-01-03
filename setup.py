from setuptools import setup, find_packages
#from distutils.core import setup

setup(
    name='models',
    description='Biomechanical and Robotic Models',
    version='1.0',

    packages=find_packages(exclude=['data','tests']),
    
    author='Galo MALDONADO',
    author_email='galo.maldonado@laas.fr',
    
    extras_require = {
        'Pioncchio':  ["pinocchio"]
    }
)