import sys


def get_readme():
    with open("Readme.md") as f:
        r = f.read()
    return r


try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise

setup(
    name="imgui-bundle",
    version="0.6.1",
    author="Pascal Thomet",
    author_email="pthomet@gmail.com",
    description="ImGui Bundle: autogenerated python bindings for ImGui (docking), ImPlot, HelloImgui, etc.",
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    url="https://github.com/pthom/imgui_bundle",
    packages=(["imgui_bundle", "imgui_bundle.demos"]),
    package_dir={"": "bindings"},
    cmake_install_dir="bindings/imgui_bundle",
    include_package_data=True,
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
    package_data={"imgui_bundle": [
        "py.typed",
        "*.pyi",
        "assets/*.*",
        "assets/fonts/*.ttf",
        "assets/fonts/Roboto/*.*",
        "assets/images/*.*",
        "demos/assets/*.*",
        "demos/assets/fonts/*.*",
        "demos/assets/images/*.*",
    ]},
    install_requires=["numpy >= 1.15"],

    entry_points = {
        'console_scripts': ['imgui_bundle_demo=imgui_bundle.demos.demo_all:main'],
    }
)
