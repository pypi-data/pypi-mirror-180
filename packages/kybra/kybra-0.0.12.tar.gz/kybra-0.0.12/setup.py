from setuptools import setup

setup(
    name='kybra',
    version='0.0.12',
    package_data={
        'kybra': ['compiler/**', 'canisters/**']
    },
    include_package_data=True,
    packages=['kybra'],
    install_requires=['modulegraph==0.19.3']
)
