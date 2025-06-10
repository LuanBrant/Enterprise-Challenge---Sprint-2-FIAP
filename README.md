# Enterprise Challenge - Sprint 2 - FIAP

## Overview

This project is part of a FIAP enterprise challenge. The goal is to collect environmental data using an ESP32 microcontroller and selected sensors. The information will support experiments for temperature and humidity monitoring, providing insights into the environment where the device is deployed.

## Virtual ESP32 Setup

1. Choose a simulator such as [Wokwi](https://wokwi.com/) or a local development environment like [PlatformIO](https://platformio.org/).
2. Create a new project and select **ESP32** as the target board.
3. Add the required sensor libraries (e.g., DHT for temperature and humidity, and analog libraries for gas sensors) using the simulator's library manager or `platformio.ini`.
4. Wire the sensors to the ESP32 pins following the simulator's schematic interface.
5. Build and upload the firmware within the simulator to verify that the virtual circuit is functioning.

## Sensor Selection

- **DHT11/DHT22**: chosen for measuring ambient temperature and relative humidity. These sensors are inexpensive and well supported by ESP32 libraries.
- **MQ-2 Gas Sensor**: used for detecting gases such as LPG, smoke, and other pollutants that may affect indoor air quality. It provides analog output that can be easily read by the ESP32.

These sensors were selected because they provide crucial environmental data relevant to the challenge objectives.

## Running the Code

1. Clone this repository and open it in your simulator environment.
2. Build or compile the project, ensuring the board is set to ESP32.
3. Upload the code to the virtual ESP32.
4. Monitor the serial output to capture sensor readings. The data can be logged to a file using the simulator's console or captured via an attached script.

## Data and Screenshots

- Sensor readings are stored in `/data` or `/logs` folders if provided by the simulator. You can export them after each run.
- Include screenshots of the virtual circuit connections and serial output in the `docs` folder for reference.

