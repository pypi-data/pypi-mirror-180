from setuptools import setup, find_packages

setup(name='booknlp_wdoc', 
	version='1.0.1', 
	packages=find_packages(),
	py_modules=['booknlp'],
	url="https://github.com/sonnygeorge/booknlp",
	author="David Bamman",
	author_email="dbamman@berkeley.edu",
	include_package_data=True, 
	license="MIT",
	install_requires=['torch>=1.7.1',
					  'tensorflow>=1.15',
					  'spacy>=3.2',
                      'transformers>=4.11.3'         
                      ],

	)
