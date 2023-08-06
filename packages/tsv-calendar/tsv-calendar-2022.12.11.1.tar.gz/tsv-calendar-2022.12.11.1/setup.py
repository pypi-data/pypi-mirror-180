import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='tsv-calendar',
    version='2022.12.11.1',
    description = ("TSV Reader for BUNZ-BAR Project"),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='TheStegosaurus_',
    packages=setuptools.find_packages(),
    classifiers=[
	"Programming Language :: Python :: 3",
	"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
	"Operating System :: OS Independent",
	"Development Status :: 3 - Alpha"
    ],
)