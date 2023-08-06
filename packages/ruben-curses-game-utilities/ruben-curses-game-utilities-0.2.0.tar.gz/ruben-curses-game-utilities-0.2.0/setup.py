import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ruben-curses-game-utilities",
    version="0.2.0",
    author="Ruben Dougall",
    author_email="info.ruebz999@gmail.com",
    description="Utility package for command-line games using the curses library.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/Ruben9922/curses-game-utilities",
    keywords="console command-line utilities game curses",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.6',
    py_modules=["game_utilities"],
    install_requires=["numpy"]
)
