from setuptools import setup, find_packages

v = '0.1.003'

setup(
    name='make-templates',
    version=v,
    py_modules=['make_templates'],
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime==4.13.1",
        "pyyaml"
    ],
    url='http://olinfo.it',
    license='BSD',
    author='Giorgio Audrito',
    author_email='giorgio.audrito@unito.it',
    entry_points={'console_scripts': [
        'make-templates=make_templates.main:script'
    ]
    },
    description='Tool to produce templates for IOI-style tasks from an input/output description.',
    long_description_content_type='text/markdown',
)
