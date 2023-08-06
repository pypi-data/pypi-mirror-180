import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

package_name = "pytest_jar_yuan"  # pytest_jar_ape

# 上传的package一定要创建 __init__.py 文件|否则识别不到
setuptools.setup(
    name=package_name,
    version="0.2.0",
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

# 上传的package一定要创建 __init__.py 文件|否则识别不到
# python setup.py sdist upload
# pip install --upgrade pytest_jar_yuan -i https://pypi.org/simple

# twine register dist/pytest_jar_yuan.whl
# twine check dist/*
# twine upload dist/*
