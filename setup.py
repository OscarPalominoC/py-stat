from setuptools import setup, find_packages

setup(
    name='py-stat',
    version='0.1.0',
    description='Librería de Python para análisis estadístico.',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
        ]
    },
    url='https://github.com/OscarPalominoC/py-stat/',
    author='Oscar Palomino',
    author_email='ing.oscarp1@gmail.com',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: GPL-3.0',
        'Programming Language :: Python :: 3'
    ]
)