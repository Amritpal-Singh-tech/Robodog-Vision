# RoboDog Vision — Ball Tracking

## Overview

RoboDog Vision is a simple project made using Python and OpenCV. It uses a webcam to detect a green ball and gives commands to tell a robot which direction to move.

## How It Works

The program takes live video from the webcam and changes the image into HSV colour format. It then detects the green colour and creates a mask to show the green areas. OpenCV finds the outlines of the detected objects and selects the largest one.

The program draws a box around the ball and marks its centre with a dot. It checks the ball's position and displays `TURN LEFT`, `TURN RIGHT`, or `GO STRAIGHT`. When the ball looks very close, the program displays `STOP`. The current command is also shown on the camera screen. The STOP command appears in red, while the other commands appear in green.

## Challenges

The main challenges were detecting the green ball, understanding how contours work, and finding the correct position of the ball. I also had to fix errors in the code and handle situations when the ball was not visible. Testing the program helped me understand how the different parts work together.

## What’s Next

In the future, I would like to improve ball detection in different lighting conditions, make the commands more stable, estimate the distance from the ball, and connect the program to a real robot.

## Requirements

- Python 3
- OpenCV (`opencv-python`)
- A webcam

## How to Run

Install OpenCV by running `python3 -m pip install opencv-python` in the Terminal. Then run `python3 main.py` inside the project folder. Press `q` to close the program.

## Demo Link
https://drive.google.com/file/d/16WVSSD_uD-JiEiwLPPL6sKp_EjoH70EW/view?usp=sharing


