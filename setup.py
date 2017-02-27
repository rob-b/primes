from setuptools import setup


setup(
    name='primes',
    version='0.0.0',
    description='Calculate prime numbers',
    long_description=open('README.rst').read(),
    license='BSD',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    py_modules=['primes'],
    entry_points="""\
    [console_scripts]
    primes = primes:main
    """,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
    ]
)
