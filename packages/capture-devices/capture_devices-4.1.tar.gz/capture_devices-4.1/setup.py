from setuptools import setup, find_packages

VERSION = '4.1' 
DESCRIPTION = 'Get list of Capture Devices easily with Directshow and Python'

from pathlib import Path
this_directory = Path().parent
long_description = (this_directory / "README.md").read_text(errors='ignore')


# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="capture_devices", 
        version=VERSION,
        author="Egemen Gulpinar",
        author_email="<egemengulpinar@gmail.com>",
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        license = 'MIT',
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        project_urls = {
        'Home Page': 'https://github.com/egemengulpinar/capture-device-list',
        'Documentation' : 'https://github.com/egemengulpinar/capture-device-list/blob/main/README.md'
        },
        home_page = 'https://github.com/egemengulpinar/capture-device-list',
        keywords=['DirectShow', 'Windows','Capture Device','Device List','FFmpeg'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.6",
            "Operating System :: Microsoft :: Windows",
            "Topic :: Multimedia :: Sound/Audio",
            "Topic :: Utilities",
        ]

        )