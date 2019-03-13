from setuptools import setup, find_packages
import sys

sys.path.append('./src')
sys.path.append('./test')

setup(
        name = 'Hoge',
        version = '0.1',
        description = "This is a test code for travis ci",
        packages = find_packages(),
        test_suite = 'test_all.suite'
)
