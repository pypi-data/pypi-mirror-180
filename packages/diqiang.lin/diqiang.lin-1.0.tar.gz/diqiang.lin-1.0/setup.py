# @Time : 2022/12/11 22:56 
# @Author : Diqiang Lin
# @File : setup.py

from distutils.core import setup

packages = ['ldq_test']  # 唯一的包名，自己取名
setup(name='diqiang.lin',
      version='1.0',
      author='ldq',
      packages=packages,
      package_dir={'requests': 'requests'}, )
