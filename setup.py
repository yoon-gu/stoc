from setuptools import setup, Distribution, find_packages

class BinaryDistribution(Distribution):
	def is_pure(self):
		return False

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
		include_package_data=True,
		distclass=BinaryDistribution,
		zip_safe=False)