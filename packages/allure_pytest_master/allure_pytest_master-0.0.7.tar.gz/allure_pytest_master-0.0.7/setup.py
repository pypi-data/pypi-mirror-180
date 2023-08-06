import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

package_name = "allure_pytest_master"

setuptools.setup(
    name=package_name,
    version="0.0.7",
    py_modules=[package_name],  # 相关依赖包|指定本包则自动识别所有
    author="jar yuan",
    author_email="author@example.com",
    description="A allure and pytest used package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.baidu.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# python setup.py sdist upload
# pip install --upgrade RobotEditSuperFastLib -i https://pypi.org/simple
