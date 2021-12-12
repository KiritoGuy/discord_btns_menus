import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycord-btns-menus",
    version="0.1.3",
    author="P. Sai Keerthan Reddy",
    author_email="saikeerthan.keerthan.9@gmail.com",
    description="A responsive package for Buttons, DropMenus and Combinations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skrphenix/pycord_btns_menus",
    project_urls={
        "Bug Tracker": "https://github.com/skrphenix/pycord_btns_menus/issues",
        "Examples": "https://github.com/skrphenix/pycord_btns_menus/tree/main/Examples",
        "Source": "https://github.com/skrphenix/pycord_btns_menus/tree/main/btns_menus",
        "Support Server": "https://discord.gg/GVMWx5EaAN",
    },
    keywords=["pycord", "py-cord", "btns", "pycord buttons",
              "pycord btns", "pycord btns menus", "py-cord btns menus"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    package_dir={"": "package"},
    packages=["btns_menus", "btns_menus.builds", "btns_menus.builds.base"],
    include_package_data=True,
    python_requires=">=3.6",
    dependency_links=[
        "https://github.com/Pycord-Development/pycord"
    ],
    install_requires=[
        "requests",
        "tabulate"
    ]
)