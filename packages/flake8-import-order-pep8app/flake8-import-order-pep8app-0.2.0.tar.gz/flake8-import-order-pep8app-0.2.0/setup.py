from pathlib import Path

from setuptools import setup


setup(
    name='flake8-import-order-pep8app',
    author='Joe Hitchen',
    url = 'https://bitbucket.org/JoeHitchen/flake8-import-order-pep-8-app/',
    version='0.2.0',
    description="Flake8 Import Order's PEP 8 style with application packages enabled.",
    long_description = (Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    py_modules=['flake8_import_order_pep_8_app'],
    install_requires=['flake8-import-order'],
    entry_points='''
        [flake8_import_order.styles]
        pep8app = flake8_import_order_pep_8_app:PEP8App
    ''',
    classifiers=[
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)

