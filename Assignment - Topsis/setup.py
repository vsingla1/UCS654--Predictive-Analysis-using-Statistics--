## 4️⃣ `setup.py`  ✅ (UPDATES SAME PACKAGE)

from setuptools import setup, find_packages

setup(
    name="Topsis-Vansh-102303806",
    version="0.0.2",
    author="Vansh",
    description="TOPSIS command-line tool",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis_vansh_102303806.topsis:main"
        ]
    },
    python_requires=">=3.7",
)
