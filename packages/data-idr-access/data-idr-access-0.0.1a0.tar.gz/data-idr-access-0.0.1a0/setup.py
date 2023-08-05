#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# python setup.py sdist upload -r pypi

# 打包检查
# python setup.py check
# 打包
# python3 setup.py sdist build
# 上传
# twine upload dist/*


if __name__ == "__main__":

    setup(
        name="data-idr-access",
        version='0.0.1a0',
        description="easily use database",
        url="",
        author="byscut",
        license="MIT",
        test_suite='tests',
        package_dir={'': '.'},
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
        ],
        python_requires=">=3.7"
    )
