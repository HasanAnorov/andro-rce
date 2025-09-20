# kano-rce

Backend service for the **KanoRTC** module of the KanoRAT platform  
Built with **Python 3 & Django REST Framework**

---

## Overview

`kano-rce` provides the real-time backend APIs and data-handling logic for the **KanoRTC** module.  
This project is intended for lawful, consent-based device management scenarios such as enterprise device management, IoT fleet oversight, or parental/personal device dashboards where explicit user consent has been obtained.

Client applications installed on managed devices send authorized telemetry (device details, performance metrics, and user-approved media or files) to this backend. KanoRTC uses the received data to visualize device state and telemetry in real time for authorised users.

---

## Features

- **Django REST Framework APIs** for receiving and processing device telemetry.
- Handles inbound HTTP `GET` / `POST` requests from installed client applications.
- Reads Device System Details (e.g., Brand, DeviceID, Manufacturer, Hardware) for visualization in the KanoRTC dashboard.
- Structured settings and environment configuration for safe deployment and operational flexibility.

