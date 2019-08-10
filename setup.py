from setuptools import setup, find_packages

version = '0.5'

setup(name='topicaxis-opengraph',
      version=version,
      description="A module to parse the Open Graph Protocol",
      long_description=open("README.rst").read() + "\n",
      classifiers=[
            'License :: OSI Approved :: MIT License',
            'Development Status :: 3 - Alpha',
            'Natural Language :: English',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Text Processing :: Markup :: HTML',
            'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='opengraph protocol facebook',
      author='Panagiotis Matigakis',
      author_email='pmatigakis@gmail.com',
      url='https://github.com/topicaxis/opengraph',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'beautifulsoup4'
      ],
      test_suite="nose.collector",
      tests_require=[
            "nose==1.3.7"
      ]
)
