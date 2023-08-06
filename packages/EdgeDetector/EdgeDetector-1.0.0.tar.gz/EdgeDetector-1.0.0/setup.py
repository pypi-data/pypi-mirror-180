from setuptools import setup
from setuptools import find_packages

setup(
    name='EdgeDetector',
    version='1.0.0',
    packages=find_packages(),
    description="Most known edge detector in this package",
    include_package_data=True,
    author_email="mohamedmaache68@gmail.com",
    author="Mohamed Maache",
    install_requires=[
        'numpy',"opencv-python","pillow"
    ],
    url="https://github.com/momomuchu/EdgeDetector",
    keywords=['edge',"detection","detector","edgedetection","edgedetector"]
)
