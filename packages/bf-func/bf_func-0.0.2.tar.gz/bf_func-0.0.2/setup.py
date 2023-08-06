# -*- coding:utf-8 -*-
"""
Created on 2022/12/12 16:48
@File: setup.py
---------
@summary:
---------
@Author: clark
@Email: clark1203@foxmail.com
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bf_func",
    version="0.0.2",
    author="clark",
    author_email="clark1203@foxmail.com",
    description="公共方法库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url=""  # 模块的github地址
    packages=setuptools.find_packages(),  # 自动找到项目下的所有包
    # 模块相关的元数据（更多描述信息）, 用于搜索引擎
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
    ],
    python_requires='>=3',
)
