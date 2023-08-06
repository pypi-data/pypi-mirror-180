import setuptools
with open(r'C:\Users\zadvo\Desktop\PyQSF\Doc\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='PyQSF',
	version='1.0.0',
	author='Georgy2008',
	author_email='zadvornow2008@gmail.com',
	description='Python Quelert System Files',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=['PyQSF'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)