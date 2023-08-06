import setuptools
with open("README.md", "r") as fhandle:
    long_description = fhandle.read() 
setuptools.setup(
    name="pywebcon", 
    version="1.0.0", 
    author="pydob",
    description="Check if websites/apis are online", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], 
    python_requires='>=3.6', 
)
