import os


os.system('python setup.py bdist_wheel')
os.system('pip install -e .')
os.system('python setup.py sdist')
os.system('python setup.py bdist_wheel sdist')
os.system('twine upload dist/*')