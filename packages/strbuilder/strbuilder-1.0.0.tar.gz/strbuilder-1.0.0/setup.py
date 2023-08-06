from setuptools import setup

with open('README.md', mode='r', encoding='utf-8') as f:
    long_description = f.read()

author = 'am230'
name = 'strbuilder'

setup(
    name=name,
    version="1.0.0",
    keywords=("builder"),
    description="A simple string builder",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT Licence",
    url=f"https://github.com/{author}/{name}",
    author=author,
    author_email="am.230@outlook.jp",
    py_modules=['py2js'],
    platforms="any"
)