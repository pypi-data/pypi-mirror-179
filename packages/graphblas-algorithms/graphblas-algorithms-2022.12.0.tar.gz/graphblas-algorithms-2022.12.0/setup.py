from setuptools import find_packages, setup

import versioneer

extras_require = {
    "test": ["networkx", "pytest", "scipy"],
}
extras_require["complete"] = sorted({v for req in extras_require.values() for v in req})

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")
with open("README.md") as f:
    long_description = f.read()

setup(
    name="graphblas-algorithms",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    entry_points={"networkx.plugins": "graphblas = graphblas_algorithms.interface:Dispatcher"},
    description="Graph algorithms written in GraphBLAS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jim Kitchen and Erik Welch",
    author_email="erik.n.welch@gmail.com,jim22k@gmail.com",
    url="https://github.com/python-graphblas/graphblas-algorithms",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
    license="Apache License 2.0",
    keywords=[
        "graphblas",
        "graph",
        "sparse",
        "matrix",
        "lagraph",
        "suitesparse",
        "Networks",
        "Graph Theory",
        "Mathematics",
        "network",
        "discrete mathematics",
        "math",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
