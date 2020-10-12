from setuptools import find_packages, setup
setup(
    name="xlrdformulas",
    packages=find_packages(include=["xlrdformulas"]),
    version="0.1.0",
    description = "xlrd formula with formula property for book",
    author="Me",
    license="-",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)