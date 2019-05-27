from setuptools import setup

package_name = "ros2_example_package_py"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    author="George Stavrinos",
    author_email="stavrinosgeo@gmail.com",
    maintainer="George Stavrinos",
    maintainer_email="stavrinosgeo@gmail.com",
    keywords=["ROS", "ROS2"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    description=(
        "Python node as an example for a minimal subscriber to a C++ publisher node."
    ),
    license="Apache License, Version 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "ros2_subscriber = ros2_example_package_py.subscriber:main"
        ],
    },
)