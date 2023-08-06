from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='pygame_pynput',
    version='1.0',
    author='Kavin Bharathi',
    author_email='r.m.kavinbharathi@gmail.com',
    description='Pygame user input module',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = find_packages(),
    install_requires=[
        requirements
    ],
    python_requires='>=3.5',
)

