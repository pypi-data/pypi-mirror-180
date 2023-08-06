# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: setup.py
# @AUthor: Fei Wu
# @Time: 11月, 20, 2022
import setuptools

with open("README.md", encoding='gb18030', errors='ignore') as fh:
  long_description = fh.read()

setuptools.setup(
  name="retention_model",
  version="0.0.2",
  author="wufeipku",
  author_email="wufei.pku@163.com",
  # py_modules=['income_predict.flowincomepredict'],
  description="package for predicting pubnum of X or others",
  long_description=long_description,
  long_description_content_type="text/markdown",
  # url="https://github.com/wufeipku/FlowIncomePredict.git",
  packages=setuptools.find_packages(),
  install_requires=['pandas>=1.2.4', 'numpy>=1.21.6', 'frechetdist>=0.6', 'scikit_learn>=0.23.2', 'scipy>=1.8.1'],
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)
