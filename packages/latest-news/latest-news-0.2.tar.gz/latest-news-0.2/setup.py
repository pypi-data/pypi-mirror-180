import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latest-news",
    version="0.2",
    author="Rafi Ramdhani",
    author_email="rafiramdhani1122@gmail.com",
    description="This package will get the latest news from the source all website in indonesia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/017RAFIRAMDHANI/PYTHON.git",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)