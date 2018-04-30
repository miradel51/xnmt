from setuptools import setup, find_packages
from distutils.core import Extension
import sys

sys.path.append("./xnmt")

with open("requirements.txt", encoding="utf-8") as req_fp:
  install_requires = req_fp.readlines()

ext_modules = []
if "--use-cython-extensions" in sys.argv:
  from Cython.Build import cythonize
  extra_compile_args = ["-std=c++11"]
  if sys.platform == "darwin":
    extra_compile_args.append("-mmacosx-version-min=10.9")
  sys.argv.remove("--use-cython-extensions")
  extensions = Extension('xnmt.cython.xnmt_cython',
                          sources=['xnmt/cython/xnmt_cython.pyx',
                                   'xnmt/cython/src/functions.cpp'],
                          language='c++',
                          extra_compile_args=extra_compile_args,
                          extra_link_args=["-std=c++11"])
  ext_modules = cythonize(extensions)

setup(
  name='xnmt',
  version='0.0.1',
  description='eXtensible Neural Machine Translation',
  author='neulab',
  url='https://github.com/neulab/xnmt',
  license='Apache License',
  install_requires=install_requires,
  packages=find_packages(exclude=['test*', 'xnmt.cython', 'xnmt.test']),
  ext_modules=ext_modules,
  python_requires='>=3.6',
  project_urls={
    'Documentation': 'http://xnmt.readthedocs.io/en/latest/',
    'Source': 'https://github.com/neulab/xnmt',
    'Tracker': 'https://github.com/neulab/xnmt/issues',
  },
  entry_points={
    'console_scripts': [
      'xnmt = xnmt.xnmt_run_experiments:main',
      'xnmt_evaluate = xnmt.xnmt_evaluate:main',
    ],
  }
)
