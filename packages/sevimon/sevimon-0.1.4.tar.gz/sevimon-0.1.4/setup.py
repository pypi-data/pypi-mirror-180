from setuptools import setup, find_packages
import os

setup(
    name='sevimon',
    version='0.1.4',
    license='LICENSE.txt',
    packages=[
      "sevimon",
      "sevimon.lib",
      "sevimon.hsemotion_onnx",
      "sevimon.lib.locale",
    ],
    package_dir={'sevimon': '', 'sevimon.lib': 'lib', 'sevimon.lib.locale': 'lib/locale', 'sevimon.hsemotion_onnx': 'hsemotion_onnx'},
    entry_points = {
        'console_scripts': [
            'sevicfg=sevimon.sevicfg:main',
            'sevimon=sevimon.sevimon:main',
            'sevistat=sevimon.sevistat:main',
        ],
    },
    url='https://github.com/ioctl-user/sevimon',
    description='Self Video Monitoring tool for facial muscles.',
    keywords='sevimon face emotion tension stress muscles wrinkles',
    install_requires=[
        'opencv-python',
        'configparser',
        'platformdirs',
        'matplotlib',
        'numpy',
        'onnx',
        'onnxruntime',
   ],
)
