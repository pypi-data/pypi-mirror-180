"""
Setup script for mindflow
"""
from setuptools import setup

setup(
    name="mindflow",
    version="0.1.2",
    py_modules=["mindflow"],
    entry_points={"console_scripts": ["mf = mindflow.main:main"]},
    install_requires=["requests", "revChatGPT", "bs4", "chardet", "pyperclip", "gitpython"],
)
