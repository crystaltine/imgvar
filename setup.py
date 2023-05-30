from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = 'Autogenerates variations of images for Machine Learning'
LONG_DESCRIPTION = \
    'Given a set of images, automatically generate variations \
    (such as flips, shifts, random color changes, create slight imperfections, etc.) \
    of those images for Machine Learning purposes. Each image will still be recognizable \
    by humans, but will be different enough to improve accuracy on new images in \
    machine learning models.'

# Setting up
setup(
    name="imgvar",
    version=VERSION,
    author="nonagon",
    author_email="donaldcenaaa@outlook.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', "pillow"], # Add dependencies here
    keywords=['python', 'image', 'machine learning', 'image recognition', 'computer vision'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)