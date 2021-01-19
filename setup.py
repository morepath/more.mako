"""
more.mako
-----
Mako template bindings for Morepath.
"""

from setuptools import setup, find_packages


version = "0.2.0.dev0"

long_description = "\n".join(
    (
        open("README.md", encoding="utf-8").read(),
        open("CHANGES", encoding="utf-8").read(),
    )
)

install_requires = ["morepath", "mako"]

tests_require = ["pytest", "coverage", "pytest-cov", "webtest"]

docs_require = ["sphinx", "docutils"]


setup(
    name="more.mako",
    version=version,
    url="https://github.com/morepath/more.mako",
    license="BSD",
    author="Blaise Laflamme",
    author_email="blaise@laflamme.org",
    description="Mako template bindings for Morepath",
    long_description=long_description,
    keywords="morepath mako",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    namespace_packages=["more"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require, "docs": docs_require},
    test_suite="more.mako",
)
