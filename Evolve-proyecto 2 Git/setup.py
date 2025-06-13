from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="teu-converter",
    version="1.0.0",
    author="Thimerson",
    author_email="thimerson@example.com",
    description="Conversor de metros cúbicos a TEUs y recomendador de envío",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thimerson/teu-converter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[],
    test_suite='tests',
)
