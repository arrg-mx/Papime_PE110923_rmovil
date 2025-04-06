# Repositorio con los archivos de similación de un robot móvil diferencial

## Estructura de los paquetes

```text
 src/
    ├── diff_description/     
    |       ├── launch
    |       |       └── display_diff.launch.xml
    |       ├── rviz/
    |       |       ├── display_diff_config.rviz
    |       │       └── urdf.rviz
    |       ├── urdf/
    |       │       ├── camara.xacro
    |       │       ├── lidar.xacro
    |       │       ├── common_properties.xacro
    |       │       ├── material.xacro
    |       │       ├── mobile_base_gazebo.xacro
    |       │       ├── mobile_base.xacro
    |       │       └── my_robot.urdf.xacro
    |       ├── CMakeLists.txt
    |       └── package.xml
    └── diff_bringup/
            ├── rviz/
            │       └── diff_robot_gz_config.rviz
            ├── launch
            │       └── diff_robot_simulation.launch.xml
            ├── world/
            │       └── test_w_1.world
            ├── CMakeLists.txt
            └── package.xml

```
El documento relacionado con estos paquetes son: Robot_movil_diferencial.ipynb

El material audiovisual relacionado es:

[Material Audiovisual](https://youtu.be/kgtRUMBlqTU)

Facultad de Ingeniería UNAM. Todos los derechos reservados, Facultad de Ingeniería de la Universidad Nacional Autónoma de México © 2025. Quedan estrictamente prohibidos su uso fuera del ámbito académico, alteración, descarga o divulgación por cualquier medio, así como su reproducción parcial o total.

