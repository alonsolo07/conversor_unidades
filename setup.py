from setuptools import setup, find_packages

setup(
    name="conversor",
    version="0.1.0",
    description="Unit conversion library (velocity, mass, distance, temperature)",
    author="Alonso",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
