from setuptools import setup, find_packages

setup(
    name="rosettastone",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "rosettastone": ["prompts/*.md", "mappings/*.ttl"],
    },
    install_requires=[
        "requests",
        "beautifulsoup4",
        "ollama",
        "rdflib",
        "mlcroissant",
        "pandas",
        "tabulate",
        # Add other dependencies as needed
    ],
    entry_points={
        "console_scripts": [
            "rosettastone-orchestrator=rosettastone.orchestrator:main",
            "rosettastone-init=rosettastone.cli:init_main",
        ],
    },
    author="Slava Tykhonov",
    description="A tool for multilingual concept translation and Croissant metadata generation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/4tikhonov/rosetta-ai", # Assuming this is the repo based on corpus mapping
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
