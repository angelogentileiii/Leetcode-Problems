from setuptools import setup, find_packages

setup(
    name='LeetcodeProblems',
    version='0.1',
    packages=find_packages(include=['Utils', 'Utils.*']),
    # Include any other arguments you need, like install_requires, etc.
    install_requires=[
        # Add any additional packages your project needs
    ],
    python_requires='>=3.11',
)