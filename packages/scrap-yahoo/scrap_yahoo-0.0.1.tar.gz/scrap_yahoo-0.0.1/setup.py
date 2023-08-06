from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A basic yahoo finance scraping package'

# Setting up
setup(
    name="scrap_yahoo",
    version=VERSION,
    author="JerryChenz (jerry Chen)",
    author_email="<jerrychen.works@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['bs4', 'requests', 'pandas', 'forex-python'],
    keywords=['python', 'yahoo', 'financial statements'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)