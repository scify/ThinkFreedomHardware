# ThinkFreedom Hardware Stack

The ThinkFreedom Hardware Stack is a hardware stack definition aimed to provide
an open implementation architecture under a
*sensor-stimulus-reactor* paradigm, supporting different settings of the
Internet of Things (IoT).

This specific project refers to the first draft of the hardware stack
definition and a first implementation, as a
device which is especially designed for disabled people. The goal of this
project is to help this group of people to interact with devices in their home
and use the PC and to better communicate with other people.

In this repository you will find a hardware prototype that was built during an
internship at SciFY (www.scify.org). This project is an openhardware-opensource
project.

## Box
Contains 2 versions (v1 and v2) of a 3D design model of the controller . You
can open them with the open source FreeCad program. It contains also a folder
with failed attempts and some examples.

## Code
Contains 3 code "packages".

1. ControlUnitPython.py  this python script runs on the Raspberrry Pi 2
2. TFS_Leonardo.ino this arduino script runs on the Arduino Leonardo/Micro
located in the control unit .
3. TFS_input.ino this arduino script runs on the Arduino Uno located in the
controller

Both arduino scripts can be edited and uploaded with the Arduino program. For
more information on how to use the code snippets check the "Manual of
Prototype" document.

## Schematics(Fritzing)
Contains 2 files.

1. ThinkFreedom Stack.jpg  this is a simple image of the schematic of the
prototype
2. TFS_Leonardo.ino this is a fritzing file which can be edited by the Fritzing
program : http://fritzing.org/home/

## Stuff

Contains several things that helped as along the way.

1. Pictures-Schematics: this file has several schematics images that we
considered when we were making the prototype
2. Alternate Input Ways.docx:  this doc has helpful descriptions of assistive
technology products
3. Switches for Think Freedom.xlsx this ecxel file is one of our first research
of switches that could be used for our application.

## ThinkFreedomStack Specs

Contains the specs for the project as well as it contains the architecture (
1.Layers of TFS(OSI Model).xlsx ) we used to build the prototype. The last file
has 3 additional implementations of the hardware stack and approximations of
costs.

## Manual For Prototype
A step by step guide of how you are going to build the prototype that we
developed.

## TFS_Presentation
Is a presentation of our work on Prezi.

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/80x15.png)](http://
creativecommons.org/licenses/by/4.0/)
ThinkFreedom Hardware by [SciFY](http://www.scify.org) is licensed under
a [Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).
Based on a work at
[https://github.com/scify/ThinkFreedomHardware](https://github.com/scify/
ThinkFreedomHardware).
