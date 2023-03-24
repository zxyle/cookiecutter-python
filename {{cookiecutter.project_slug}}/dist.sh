#!/usr/bin/env bash

name="{{ cookiecutter.project_name }}"

function install() {
    package
    pip uninstall -y $name
    for x in `ls dist/*.whl`; do pip install $x; done
}

function package() {
    clean
    pip install -U wheel twine setuptools
    python3 setup.py sdist bdist_wheel
}

function clean() {
    rm -rf build/ *.egg-info/ dist/
    find . -name "__pycache__"  | xargs rm -rf
}


function publish() {
   package
   twine upload dist/*
}

function usage() {
    echo "Usage: sh dist.sh [clean|package|install|publish]"
    exit 1
}

function test() {
    echo "TEST"
    exit 0
}

#根据输入参数，选择执行对应方法，不输入则执行使用说明
case "$1" in
  "clean")
    clean
    ;;
  "install")
    install
    ;;
  "package")
    package
    ;;
  "publish")
    publish
    ;;
  *)
    usage
    ;;
esac