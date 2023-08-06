from setuptools import setup
import os
import pathlib

def package_files(directory: str, ignore_ext: list = []) -> list:
    """Returns the filepath for all files in a directory. Borrowed from https://stackoverflow.com/a/36693250"""
    paths = []
    ignore_ext = [ext.lower() for ext in ignore_ext]
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(path, filename)
            if pathlib.Path(filepath).suffix.lower().strip(".") in ignore_ext:
                continue
            paths.append(filepath)
    return paths

urdf_files = package_files('jkinpylib/urdfs/') # filenames are relative to the root directory, but we want them relative to the root/jkinpylib directory
assert len(urdf_files) > 0, "No URDF files found"
urdf_files = [fname.strip("jkinpylib/") for fname in urdf_files]
print(f"Found {len(urdf_files)} urdf files")

setup(
    name="jkinpylib",
    version="0.0.3",
    author="Jeremy Morgan",
    author_email="jsmorgan6@gmail.com",
    scripts=[],
    url="http://pypi.python.org/pypi/jkinpylib/",
    license="LICENSE.txt",
    description="Jeremy's Kinematics Python Library",
    py_modules=[],
    long_description=open("README.md").read(),
    install_requires=["klampt", "numpy", "torch", "black", "kinpy"],
    include_package_data=True,
    packages=["jkinpylib"],
    package_data={'jkinpylib': urdf_files},
)