from setuptools import setup, find_packages



VERSION = '0.0.5'
DESCRIPTION = 'CasMarine'

# Setting up
setup(
    name="casmarinedeneme2",
    version=VERSION,
    author="mubarizmuradov",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'PyQt5', 'numpy', 'python-math', 'future', 'wheel'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)