from setuptools import find_packages, setup

package_name = 'nodes_topics_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robousr',
    maintainer_email='robousr@todo.todo',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node_py = nodes_topics_py.my_node_py:main',
            'pub_node_py = nodes_topics_py.pub_node_py:main',
            'counter_node_py = nodes_topics_py.counter_node_py:main',
        ],
    },
)
