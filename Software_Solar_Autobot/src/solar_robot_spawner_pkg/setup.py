import os # Operating system library
from glob import glob # Handles file path names
from setuptools import setup # Facilitates the building of packages

package_name = 'solar_robot_spawner_pkg'

# Path of the current directory
cur_directory_path = os.path.abspath(os.path.dirname(__file__))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Path to the launch file      
        (os.path.join('share', package_name,'launch'), glob('launch/*.launch.py')),

        # Path to the world file
        (os.path.join('share', package_name,'worlds/'), glob('./worlds/*')),

        # Path to the warehouse sdf file
        (os.path.join('share', package_name,'models/small_solar/'), glob('./models/small_solar/*')),

        # Path to the mobile robot sdf file
        (os.path.join('share', package_name,'models/mobile_solar_robot/'), glob('./models/mobile_solar_robot/*')),
        
        # Path to the world file (i.e. warehouse + global environment)
        (os.path.join('share', package_name,'models/'), glob('./worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tarunesh38',
    maintainer_email='tarunesh38@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'spawn_demo = solar_robot_spawner_pkg.spawn_demo:main'
        ],
    },
)
