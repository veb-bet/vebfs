from setuptools import setup, find_packages

setup(
    name='vebfs',
    version='0.2',
    packages=find_packages(),
    install_requires=[],
    test_suite='tests',
    description='Библиотека для удобных операций с файлами и папками.',
    author='veb-bet',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
