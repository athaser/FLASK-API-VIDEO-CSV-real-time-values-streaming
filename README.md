# FLASK-API-VIDEO-CSV-real-time-values-streaming


his is a wrapper for Stack Overflow API

Instructions:

1. git clone https://github.com/athaser/FLASK-API-VIDEO-CSV-real-time-values-streaming
2. cd to the folder
3. python3 app3.py

Objective:

The objective is to create a Flask service that demonstrates 2 videos in 2 different endpoints and streams alongside the data that are included in CSV files.
The data included in the CSVs were generated with ML algorithms that identify and classify the behavioral analysis -> Violent Behaviour Identification of the 2 videos.

The First endpoint in route /: Contains normal behaviour video and data
The Second endpoint in route /page2: Contains the video and vata that identified as High Risk for violence behavior from the ML algorithms.

Requirements:

Flask                         2.0.3
Turbo-Flask                   0.8.0
