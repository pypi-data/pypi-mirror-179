from setuptools import setup, find_packages
import codecs
import os

VERSION = "0.0.21"
DESCRIPTION = "Analyzing arbitrage opportunities between DEcentralized eXchanges (dex-to-dex)"
LONG_DESCRIPTION = "An extensible library allows to analyze DEX-to-DEX arbitrage opportunities autonomously, besides advanced decentralized exchange operations"

urls = {
    "Source": "https://github.com/f4T1H21/Arbitrage-Bot-Code-Library/blob/main/libarbitrage/lib.py",
    "Homepage": "https://github.com/f4T1H21/Arbitrage-Bot-Code-Library",
    "Documentation": "https://github.com/f4T1H21/Arbitrage-Bot-Code-Library#documentation",
    "Twitter": "https://twitter.com/f4T1H21",
    "Linkedin": "https://www.linkedin.com/in/%C5%9Fefik-efe/"
}

setup(
    name="libarbitrage",
    version=VERSION,
    author="f4T1H21 (Şefik Efe Altınoluk)",
    author_email="<sefbey21@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["web3"],
    project_urls=urls,
    keywords=["python", "bot", "arbitrage", "analyze", "arbitrage analyze", "dex", "dex arbitrage", "pyarbitrage", "libarbitrage"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Developers",

    ]
)