from distutils.core import setup
import os

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = [] # Here we'll get: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setup(install_requires=install_requires)
setup(
  name = 'pyobigram',
  packages = ['pyobigram'],
  version = '1.6',
  description = 'Python Simple Telergam Api.',
  author = 'obisoftdev',
  author_email = '',
  url = 'https://github.com/Obysoftt/pyobigram',
  keywords = ['py', 'obigram'],
  license = 'GPLv3',
  classifiers = [],
)
