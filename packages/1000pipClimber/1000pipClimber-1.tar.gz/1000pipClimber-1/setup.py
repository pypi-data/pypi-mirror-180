import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt','r') as fr:
    requires = fr.read().split('\n')

setuptools.setup(
    # pip3 1000pip climber system download
    name="1000pipClimber", 
    version="1",
    author="1000pip climber system download",
    author_email="dowloadver1@1000pipclimbersystem.com",
    description="1000pip climber system download",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://858d0aqdynn98w4ucl3agpav9m.hop.clickbank.net/?tid=pydownload",
    project_urls={
        "Bug Tracker": "https://github.com/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=requires,
)
