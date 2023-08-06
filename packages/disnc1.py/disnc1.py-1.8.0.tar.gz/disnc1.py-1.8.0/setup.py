from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')
with open('dislash/__init__.py', 'r') as f:
    version = [line.split('=')[1].strip(" '\"") for line in f.read().splitlines() if line.startswith('__version__')][0]


setup(
    name='disnc1.py',
    version=version,
    description='nc.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/Lordnc/disnc/',
    author='NCPD',
    author_email='nc@n811nc.com',
    keywords='python, discord, slash, commands, api, discord-api, discord-py, slash-commands, message-components, buttons, select-menus, context-menus',
    packages=['dislash', 'dislash.application_commands', 'dislash.interactions', 'dislash.application_commands._modifications'],
    python_requires='>=3.6, <4',
    install_requires=["discord.py"],
    project_urls={
        'Documentation': 'https://amazon.com',
        'Bug Reports': 'https://amazon.com',
        'Source': 'https://github.com/Lordnc/disnc/',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
