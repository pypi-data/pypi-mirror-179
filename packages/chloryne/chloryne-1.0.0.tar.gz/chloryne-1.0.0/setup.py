from setuptools import setup, Extension

setup(
    ext_modules=[
        Extension(
            "_chloryne", 
            ["chloryne/_chloryne.c"],
            libraries=['sodium'])
    ],
    ext_package="chloryne",
    name="chloryne",
    author="origamizyt",
    url="https://gitee.com/origamizyt/chloryne",
    description='Another libsodium wrapper.',
    version='1.0.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=["chloryne"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Security :: Cryptography",
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3',
    license='MIT'
)