from setuptools import find_packages, setup

setup(name="agentic-trading-system",
      version="0.0.1",
      author="sejal",
      author_email="sejal9992@gmail.com",
      packages=find_packages(),
      install_requires={"langchain-astradb","langchain"})