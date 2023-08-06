import setuptools

setuptools.setup(
    name="AutoDiffpyy",
    version="1.0",
    author="Jinglun Gao, Chuqing Zhao, Jiaping Lin, Chao Wang",
    author_email="jgao1@g.harvard.edu, chuqingzhao@g.harvard.edu, jiapinglin@g.harvard.edu, chaowang@g.harvard.edu",
    description="Package for fast automatic differentiation in Python",
    url="https://code.harvard.edu/CS107/team03",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)