from distutils.core import setup
import py2exe

setup(name="cred_crud",
    version="1.0",
    description="",
    author="",
    author_email="",
    url="",
    license="",
    scripts=["cred_crud.py"],
    console=["cred_crud.py"],
    options={"py2exe":{"bundle_files":1}},
    zipfile=None
    )