import setuptools

with open('README.md', 'r', encoding='UTF-8') as r:
    long_description = r.read()

setuptools.setup(
    name='FaceDetector-cc',
    version='0.0.1',
    description='Simple python package to simply use mediapipe face detection.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Chanchal Roy',
    author_email='croy7667@gmail.com',
    maintainer='Chanchal Roy',
    maintainer_email='croy7667@gmail.com',
    url='https://github.com/Chexa12cc/FaceDetector-cc',
    project_urls={
        "Bug Tracker": "https://github.com/Chexa12cc/FaceDetector-cc/issues",
    },
    download_url='https://pypi.org/project/FaceDetector-cc/',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=['FaceDec'],
    python_requires=">=3.6",
    install_requires=['mediapipe', 'opencv-python'],
    license='MIT',
    keywords=['Mediapipe', 'Opencv', 'Face Detection', 'Python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
