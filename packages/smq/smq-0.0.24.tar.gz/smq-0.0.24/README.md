python3 -m pip install --user --upgrade setuptools wheel twine

python3 setup.py sdist bdist_wheel

python3 -m twine upload dist/*

pip install tencentcloud-manager -U -i https://pypi.org/simple

pip install /Users/xinz0526/Documents/workspace/python/schedule-mq