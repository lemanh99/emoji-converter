from setuptools import setup

setup(
    name='emoji-converter',
    version='1.0.0',
    description='A Python package for converting text to emoji and emoji to text.',
    author='Le Xuan Manh',
    author_email='lexuanmanh101199@gmail.com',
    packages=['emoji_converter'],
    install_requires=[
        # List any dependencies your package requires
        'emoji',  # https://pypi.org/project/emoji/
    ],
)
