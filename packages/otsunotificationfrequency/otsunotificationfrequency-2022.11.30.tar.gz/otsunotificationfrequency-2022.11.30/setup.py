import sys

from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
with open('LICENSE', 'r', encoding='utf-8') as f:
    lcs = f.read()
info = sys.version_info
setup(
    name='otsunotificationfrequency',
    version='2022.11.30',
    url='https://github.com/Otsuhachi/NotificationFrequency',
    description='要素数が確定されたシーケンスの途中で処理を挟むタイミングの判定を補助します。',
    long_description_content_type='text/markdown',
    long_description=readme,
    author='Otsuhachi',
    author_email='agequodagis.tufuiegoeris@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    license=lcs,
    keywords='Python Notification Frequency',
)
