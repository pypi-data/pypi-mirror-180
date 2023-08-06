from setuptools import setup, find_packages


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="onnx_hameln",
    version="0.0.1",
    author="irasin",
    author_email="edad811@gmail.com",
    description="an onnx rewrite tool",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "onnx",
        "onnxoptimizer",
        "networkx"
    ],
    python_requires='>=3.6'
)