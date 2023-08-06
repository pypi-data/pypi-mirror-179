<!--
 * @Date: 2022-04-02 09:56:33
 * @LastEditors: ruohua.li
 * @LastEditTime: 2022-07-04 10:03:10
-->

This project is mainly to package commonly used tools, functions and classes
The current version mainly includes database information and read-write data functions

python'''
py setup.py sdist bdist_wheel
pip install pi_utils-0.0.1-py3-none-any.whl
'''

https://packaging.python.org/en/latest/tutorials/packaging-projects/

py -m pip install --upgrade pip
py -m pip install --upgrade build
py -m build

py -m pip install --upgrade twine
py -m twine upload dist/*  
py -m twine upload --skip-existing dist/*  # 已有相同版本
 