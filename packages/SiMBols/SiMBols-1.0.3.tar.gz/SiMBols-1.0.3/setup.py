import setuptools

setuptools.setup(
    name="SiMBols",
    version="1.0.3",
    author="Fabian Schuhmann",
    author_email="fabian.schuhmann@uol.de",
    description="A package containing similarity measures for life science purposes. The package contains or uses Fréchet Distance, Dynamic Time Warping, Hausdorff Distance, Longest Common Subsequence, Difference Distance Matrix, Wasserstein Distance and the Kullback-Leiber Divergence (Jenssen-Shannon Distance)",
    packages=setuptools.find_packages(),
    url='https://gitlab.uni-oldenburg.de/quantbiolab/simbols',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'scipy',
        'dtaidistance',
        'mdtraj',
        'rmsd'
    ]
)
