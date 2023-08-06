import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("VERSION") as f:
      v = int(f.read().strip())

setuptools.setup(
    name="patchxl",
    version=f"0.0.{v}",
    author="Yongfu Liao",
    author_email="liao961120@gmail.com",
    description="The Composer of Tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liao961120/patchxl",
    package_dir = {'': 'src'},
    packages=['patchxl'],
    # package_data={
    #     "": ["data/*.txt", "data/*.json", "data/*.csv"],
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'openpyxl'
    ]
)
