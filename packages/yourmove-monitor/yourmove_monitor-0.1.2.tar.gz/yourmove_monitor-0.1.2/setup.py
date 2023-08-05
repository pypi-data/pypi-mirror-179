import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yourmove_monitor",
    version="0.1.2",
    author="jup014",
    author_email="jup014@ucsd.edu",
    description="General Library to monitor YourMove Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hekler-Designing-Health-Lab/YourMove-Monitor",
    project_urls={
        "Bug Tracker": "https://github.com/Hekler-Designing-Health-Lab/YourMove-Monitor/issues",
    },
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['numpy', 'pandas', 'pymongo'],
)