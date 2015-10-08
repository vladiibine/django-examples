from distutils.core import setup

setup(
    name='widget_customization',
    version='1.0',
    packages=['widget_customization', 'model_select_customized'],
    url='https://github.com/vladiibine/',
    license='MIT',
    author='Vlad-George Ardelean',
    include_package_data=True,
    package_data={'widget_customization': ['db.sqlite3']},
    author_email='',
    description='Example project showing various admin customization options',
    install_requires=['Django>=1.8,<1.9'],
)
