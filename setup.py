import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='skypy-data',
    version='0.1.0',
    author='SkyPy Project',
    description='data files for the SkyPy library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/skypyproject/skypy-data',
    packages=[
        'skypy-data.bandpasses',
        'skypy-data.spectrum_templates',
    ],
    package_dir={
        'skypy-data': '.'
    },
    package_data={
        '': ['*.ecsv']
    },
)
