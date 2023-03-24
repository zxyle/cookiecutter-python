from os.path import abspath, dirname, join

from setuptools import find_packages, setup

install_reqs = [req.strip() for req in open(abspath(join(dirname(__file__), 'requirements.txt')))]

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="{{ cookiecutter.open_source_license }}",
    url="https://github.com/",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_reqs,
    # tests_require=tests_require,

    # https://pypi.org/classifiers/
    classifiers=[
        "Natural Language :: English",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)