import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="bonfire_tg",
	version="1.1.1",
	author="Help_urself",
	author_email="alexliulev1@gmail.com",
	description="telegram api libraly",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Help-urself/bonfire",
	packages=setuptools.find_packages(),
	install_requires = ['requests >= 2.27.1','colorama >= 0.4.6','APScheduler >= 3.9.1.post1'],
	classifiers=[
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
)