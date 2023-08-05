# encoding: utf-8
# https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#legacy-namespace-packages
# https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages
__path__ = __import__('pkgutil').extend_path(__path__, __name__)
