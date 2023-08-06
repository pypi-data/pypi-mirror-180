from setuptools import setup

setup(
    name='sphinx-cs',
    version='1.0.1',
    author='rogerbarton',
    author_email='rogerbarton@users.noreply.github.com',
    packages=['sphinx_cs'],
    url='https://github.com/rogerbarton/sphinx-csharp',
    license='MIT',
    description='C# domain for Sphinx',
    install_requires=['Sphinx>=1.6'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation :: Sphinx'
    ]
)
