from setuptools import setup, find_packages

v = '0.1'

setup(
    name='make-templates',
    version=v,
    py_modules=['make_templates'],
    install_requires=[
        "antlr4-python3-runtime==4.9.3"
    ],
    url='http://olinfo.it',
    license='BSD',
    author='Giorgio Audrito',
    author_email='giorgio.audrito@unito.it',
    entry_points={'console_scripts': [
        'make-templates=make_templates:script'
    ]
    },
    description='Tool to produce templates for IOI-style tasks from an input/output description.'
)
