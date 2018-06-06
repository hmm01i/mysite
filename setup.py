from setuptools import setup

setup(
        name='mysite',
        packages=['mysite','jobs'],
        include_package_data=True,
        install_requires=[
            'flask',
            ],
        )
