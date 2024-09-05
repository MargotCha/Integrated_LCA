from setuptools import setup, find_packages

setup(
    name='IntLCA-dev',
    version='0.1.0',
    author='Margarita A. Charalambous',
    author_email='ritabous2@gmail.com',
    description='This package is dedicated for large scale LCA scenario analysis while modifying the technosphere matrix. It can be used to filter and modify the technosphere matrix, perform LCA calculations,and save results',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MargotCha/Integrated_LCA/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD-3-Clause license',
        'Operating System ::  Microsoft :: Windows :: Windows 10',
    ],
    packages = find_packages(),
    python_requires=">=3.8, <=3.12",
    install_requires=[
        "brightway2==2.4.3",
        "premise==1.5.1",
        "ipython==8.14.0",
        "jupyterlab",
    ]
)