import setuptools

setuptools.setup(
    name="toilet3",  # 배포되는 package 이름
    version="0.0.3",
    author="hwangyoungjae",
    author_email="dudwo56@gmail.com",
    # description="description",
    url="https://github.com/hwangyoungjae",
    project_urls={
        "Bug Tracker": "https://youngjae.com/profjt_url",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
