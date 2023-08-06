from setuptools import setup
from setuptools import find_packages


VERSION = '1.0.2'

setup(
    name='parser_carapi',  # package name
    version=VERSION,  # package version
    description='parse car api excel config',  # package description
    packages=find_packages(),
    zip_safe=False,
    author='zoulx',
    author_email='894919296@qq.com',
    url='https://github.com/chinaZoulx',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        "xlrd>=1.2.0",
    ]
)