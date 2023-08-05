from setuptools import setup
from setuptools import find_packages

setup(name='elephas',
      version='3.4.3',
      description='Deep learning on Spark with Keras',
      url='http://github.com/danielenricocahall/elephas',
      download_url='https://github.com/danielenricocahall/elephas/tarball/3.4.0',
      author='Daniel Cahall',
      author_email='danielenricocahall@gmail.com',
      iinstall_requires=['cython',
                        'tensorflow>=2,!=2.2.*,<=2.10',
                        'flask',
                        'h5py==3.3.0',
                        'pyspark<3.4'],
      extras_require={
        'tests': ['pytest', 'pytest-pep8', 'pytest-cov', 'pytest-spark', 'mock']
    },
      packages=find_packages(),
      license='MIT',
      zip_safe=False,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ])
