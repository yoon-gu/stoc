from setuptools import setup, find_packages

setup(	name='stoc', version='0.0',
		description='Stochastic Optimal Control Library',
		url='https://github.com/yoon-gu/stoc/',
		author='Jacob Hwang',
		author_email='yz0624@gmail.com',
		license='MIT',
		packages=find_packages(),
		install_requires=[
			'numpy',
			# 'scipy',
		],
		zip_safe=False)