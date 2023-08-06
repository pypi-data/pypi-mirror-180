from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ChatGPT_PyBot",
    version="0.2",
    author="Liuhuanshuo",
    author_email="huanshuo080l@gmail.com",
    description="A simple Python class for interacting with OpenAI's chatGPT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liuhuanshuo",
    packages=find_packages(),
    install_requires=[
        "rich",
        "requests",
        "OpenAIAuth"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "chatgpt = ChatGPT_PyBot.chatgpt:main"
        ]
    },
)
