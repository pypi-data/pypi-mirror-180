import setuptools
import distutils.core

setuptools.setup(
    name="large-language-model-cli",
    version=0.1,
    author="Talwrii",
    author_email="Talwrii@googlemail.com",
    description="Command-line for interacting with large language models. not TUI. chatgpt",
    license="mit",
    keywords="",
    url="",
    packages=["llmcli"],
    long_description=open("readme.md").read(),
    entry_points={"console_scripts": ["llmcli=llmcli:main"]},
    classifiers=[],
)
