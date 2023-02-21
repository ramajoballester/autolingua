from setuptools import setup, find_packages

name = 'autolingua'

with open('requirements.txt', encoding='utf-8') as f:
    install_requires = f.read().splitlines()


setup(
    name=name,
    version='0.3',
    author='Álvaro Ramajo Ballester',
    author_email='aramajo@pa.uc3m.es',
    description='Package description',
    # packages=find_packages(where='./{}'.format(name), exclude=['docs', 'data']),
    packages=find_packages(),

    long_description=open('README.md', encoding='utf-8').read(),
    install_requires=install_requires
)