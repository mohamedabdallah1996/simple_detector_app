from setuptools import setup, find_packages


def get_requirements(file_path):

    HYPHEN_E_DOT = '-e .'
    with open(file_path, 'r') as f:
        req = [item.strip() for item in f.readlines()]

        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)
    
    return req

setup(
    name='ML_DEMO',
    version='1.0.0',
    description='Demo for a ml project',
    author='Mohamed Abdullah',
    author_email='mabdullah@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)