# COMMON AISAC BOT LIBRARIES

DEPLOY:

conda install twine==4.0.1 --y


python setup.py sdist bdist_wheel
twine upload --skip-existing dist/* --username=cla.fragomeli_92 --password=Monocolo@888
rm -r build
rm -r dist
rm -r bot_common.egg-info

PYPI_USER="cla.fragomeli_92"
PYPI_PWD="Monocolo@888"
twine upload --skip-existing dist/* --username=$PYPI_USER --password=$PYPI_PWD

