import setuptools

with open("D:\\MyProject\\F021-api\\README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="f021",
    version="0.0.1",
    author="Hifive",
    author_email="2019912635@qq.com",
    description="网站 f021.top 的帮助库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hifive55555/f021-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python : 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)