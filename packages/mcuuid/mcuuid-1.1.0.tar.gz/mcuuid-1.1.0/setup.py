import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mcuuid",
    version="1.1.0",
    author="clerie",
    author_email="hallo@clerie.de",
    description="Getting Minecraft Player Information from Mojang API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clerie/mcuuid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests>=2.0.0',
    ],
)
