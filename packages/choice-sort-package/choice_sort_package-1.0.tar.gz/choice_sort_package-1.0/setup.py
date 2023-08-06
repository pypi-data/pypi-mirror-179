from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()
setup(
   name='choice_sort_package',
   version='1.0',
   description='Модуль, проводящий сортировку выбором',
   long_description=long_description,
   license='MIT',
   packages=[
    'choice_sort_package',
    ],
   install_requires=[
    'pytest',
    'argparse'
    ],
)
