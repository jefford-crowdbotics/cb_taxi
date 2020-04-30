import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cb-taxi", # Replace with your own username
    version="0.1",
    author="Crowdbotics",
    author_email="jefford@crowdbotics.com",
    description="A small custom module/package for a ride-sharing app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jefford-crowdbotics/cb_taxi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'osmapi',
        'geopy'
    ],
)