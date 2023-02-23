from setuptools import find_packages, setup

setup(
    name="committee",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "aerospike==4.0.0",
        "redis==4.5.1",
        "fastecdsa>=2",
        "marshmallow-dataclass>=8.0.0",
        "marshmallow>=3.8.0",
        "PyYAML==6.0",
        "requests>=2.24.0",
    ],
)
