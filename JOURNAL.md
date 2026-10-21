# Journal

## 2026-9-24- Initial setup of Microclimate OS

## 2026-10-21 - Project Status Overview

### Current Implementation Status

* **Hardware & Physical Build:**
  The serial communication between the ESP32 and the LA66 LoRaWAN module has been configured using GPIO 16 and 17. A custom weatherproof enclosure (`case.jpg`) was designed and 3D-printed to house the microcontroller, sensors, radio module, and battery power supply safely.

* **Data Transmission & IoT Dashboard:**
  Ground-level microclimate data is continuously captured in real time. The device successfully transmits telemetry data via LoRaWAN to the `loramint.de` platform, where live sensor readings are processed and visualized in interactive graphs (`loramint-plot.jpg`).

* **Documentation & Submission Prep:**
  The repository structure is fully set up, including dedicated directories for sub-project files (`microclimate/`) and source code (`code/`). Code files and documentation are being finalized for the Hack Club Forge Tier 3 submission.

---

### Remaining Milestones

1. Complete file synchronization on the Hack Club Forge platform.
2. Commit all core firmware scripts (`main.py` and supporting modules) into the `code/` directory.
3. Submit the completed sub-project for final review.

* **Description:**  Setting up the BME280 sensor data logging system and integrating LoRaWAN telemetry with the loramint.de dashboard for real-time monitoring of the microclimate.

<img width="1227" height="467" alt="Bildschirmfoto_2026-10-08_16-53-35" src="https://github.com/user-attachments/assets/19db0b8a-fad7-4a40-b1ce-fe496e03c65d" />


