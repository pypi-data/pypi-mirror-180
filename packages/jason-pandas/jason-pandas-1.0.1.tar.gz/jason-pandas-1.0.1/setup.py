# -*- ecoding: utf-8 -*-
# @ModuleName: setup.py.py
# @Author: jason
# @Email: jasonforjob@qq.com
# @Time: 2022/12/10
# @Desc:


from setuptools import setup

setup(name='jason-pandas',
      version='1.0.1',
      description='Pandas is a very popular data processing library that provides a wealth of functions and methods that can be used for data cleaning, analysis, and visualization tasks. By wrapping these functions, your project makes the process of using pandas more convenient, helping people to quickly complete data processing tasks.',
      author='Jason',
      author_email='jasonforjob@qq.com',
      license='MIT',
      packages=['utils'],
      install_requires=["numpy", "pandas"],
      zip_safe=False)


