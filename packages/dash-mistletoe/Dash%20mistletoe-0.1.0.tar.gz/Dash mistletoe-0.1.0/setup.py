from setuptools import setup

setup(
    name='Dash mistletoe',
    version='0.1.0',
    author='Bradley Erickson',
    author_email='bbwe24@gmail.com',
    license='LICENSE',
    description='A wrapper of mistletoe to output Markdown as Dash components',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'mistletoe==0.9.0',
        'dash >= 2.1.0',
    ]
)
