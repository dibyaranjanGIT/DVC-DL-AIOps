from setuptools import setup

with open("README.md","r", encoding="UTF-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="dibyaranjanGIT",
    description="A small description",
    long_description=long_description,
    url="https://github.com/dibyaranjanGIT/DVC-DL-AIOps",
    packages=["src"],
    python_requires=">3.7",
    install_requires=[
        'tensorflow'
        'dvc'
        'matplotlib'
        'numpy'
        'pandas'
        'tqdm'
        'PyYAML'
        'boto3'
    ]
)