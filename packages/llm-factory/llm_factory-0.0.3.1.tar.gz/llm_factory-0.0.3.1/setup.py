import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="llm_factory",
    version="0.0.3.1",
    author="Abhishek Masand",
    author_email="masand.abhishek@gmail.com",
    description="This package is a utility library for interfacing with multiple Large Language Models (LLMs) using a common interface.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhimasand/LLM-Factory",
    project_urls={
        "Bug Tracker": "https://github.com/abhimasand/LLM-Factory/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    package_data={},
)