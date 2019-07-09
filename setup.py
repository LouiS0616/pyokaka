import os
import sys
from setuptools import setup, find_packages


# References
#   numpy's setup.py
#   https://github.com/numpy/numpy/blob/943695bddd1ca72f3047821309165d26224a3d12/setup.py

def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    with open('README.md') as f:
        readme = f.read()

    metadata = dict(
        name='pyokaka',
        version='0.9',
        description='Simple tool to translate from Roma-ji into Hiragana.',
        long_description=readme,
        long_description_content_type='text/markdown',
        python_requires='>=3.6',
        author='LouiSakaki',
        author_email='e1352207@outlook.jp',
        url='https://github.com/LouiS0616/pyokaka',
        license='MIT',
        packages=find_packages(),

        package_data={
            'pyokaka': ['transtable.json']
        }
    )

    print(find_packages())

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)
    return


if __name__ == '__main__':
    setup_package()
