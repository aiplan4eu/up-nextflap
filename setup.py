from setuptools import setup

long_description=\
"""============================================================
    UP_NEXTFLAP
 ============================================================
"""

setup(
    name='up_nextflap',
    version='0.0.8',
    description='up_nextflap',
    long_description=long_description,
    long_description_content_type ="text/markdown",
    author='Oscar Sapena',
    author_email='ossaver@upv.es',
    url = "https://github.com/aiplan4eu/up-nextflap",
    packages=['up_nextflap'],
    platforms=['win_amd64'],
    options = {
        'build_apps': {
            'platforms': ['win_amd64',],
        }
    },
    data_files=[('.', ['libz3.dll', 'nextflap.pyd'])],
    install_requires=[
        'numpy', 'unified-planning'
    ],
)