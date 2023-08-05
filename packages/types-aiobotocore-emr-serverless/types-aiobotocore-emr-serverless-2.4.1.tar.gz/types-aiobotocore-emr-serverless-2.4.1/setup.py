"""
Setup script for types-aiobotocore-emr-serverless.
"""
from os.path import abspath, dirname

from setuptools import setup

LONG_DESCRIPTION = open(dirname(abspath(__file__)) + "/README.md", "r").read()


setup(
    name="types-aiobotocore-emr-serverless",
    version="2.4.1",
    packages=["types_aiobotocore_emr_serverless"],
    url="https://github.com/youtype/mypy_boto3_builder",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description=(
        "Type annotations for aiobotocore.EMRServerless 2.4.1 service generated with"
        " mypy-boto3-builder 7.11.11"
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    keywords="aiobotocore emr-serverless type-annotations boto3-stubs mypy typeshed autocomplete",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={"": ["LICENSE"], "types_aiobotocore_emr_serverless": ["py.typed", "*.pyi"]},
    python_requires=">=3.7",
    project_urls={
        "Documentation": (
            "https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_serverless/"
        ),
        "Source": "https://github.com/youtype/mypy_boto3_builder",
        "Tracker": "https://github.com/youtype/mypy_boto3_builder/issues",
    },
    install_requires=[
        "typing-extensions>=4.1.0",
    ],
    zip_safe=False,
)
