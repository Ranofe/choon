import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'requests_html',
    'requests',
]

DEV_REQUIREMENTS = [
    'black == 22.*',
    'build == 0.7.*',
    'coveralls == 3.*',
    'flake8 == 4.*',
    'isort == 5.*',
    'mypy == 0.942',
    'types-setuptools',
    'types-requests',
    'pytest == 7.*',
    'pytest-cov == 3.*',
    'twine == 4.*',
]

setuptools.setup(
    name='Choon',
    version='0.1.0',
    description='Link budget calculation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Ranofe/choon',
    author='Ranofe',
    license='?',
    packages=setuptools.find_packages(
        exclude=[
            'examples',
            'test',
        ]
    ),
    package_data={
        'choon': [
            'py.typed',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: ?",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    entry_points={
        'console_scripts': [
            'PROJECT_NAME_URL=project_name.my_module:main',
        ]
    },
    python_requires='>=3.7, <4',
)
