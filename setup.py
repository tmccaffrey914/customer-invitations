from setuptools import (
    find_packages,
    setup
)


with open("README.md", 'r') as f:
    long_description = f.read()


setup(
    name='Intercom Take Home Test',
    version='1.0',
    description='Intercom Take Home Test',
    author='Tomás McCaffrey',
    author_email='tmccaffrey@qub.ac.uk',
    url='http://www.tomasmccaffrey.com',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['click', 'geopy', 'requests'],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'create-invite-list = src.cli:from_url',
            'create-invite-list-from-file = src.cli:from_file'
        ]
    }
)