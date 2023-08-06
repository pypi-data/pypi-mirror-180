from setuptools import setup, find_packages

setup(
    name='j1nuclei',
    version='1.0.1',
    packages=find_packages(),
    url='https://github.com/jupiterOne/j1nuclei',
    license='MIT License',
    author='JupiterOne',
    author_email='sacha.faut@jupiterone.com',
    description='J1Nuclei is a CLI tool demonstrating how JupiterOne platform can automate and learn from other tools. It automates everyday security tasks of scanning endpoints for vulnerabilities.',
    entry_points={
        'console_scripts': [
            'j1nuclei = j1nuclei.cli:main'
        ],
    },
)
