from setuptools import setup, find_packages


setup(
    name="chat-gpt-ppt",
    version="0.1.0",
    description="use ChatGPT to generate PPT automatically",
    author="williamfzc",
    author_email="williamfzc@foxmail.com",
    url="https://github.com/williamfzc/chat-gpt-ppt",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
    install_requires=[
        "revChatGPT",
        "fire",
        "loguru",
    ],
    entry_points={"console_scripts": ["cgp = cgp:main"]},
)
