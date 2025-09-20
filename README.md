# kano-rce

Backend service for the **KanoRTC** module of the KanoRAT platform  
Built with **Python 3 & Django REST Framework**

---

## Overview

`kano-rce` provides the real-time backend APIs and data-handling logic for the **KanoRTC** module.  
The system is designed for scenarios such as:

It exposes REST endpoints and manages data storage, enabling connected clients (agents) to send device details and other telemetry for visualization within KanoRTC.

Features

Django REST Framework APIs for receiving and processing device telemetry

Handles inbound HTTP GET/POST requests from installed client applications

Extracts metadata (e.g., headers, request info) for visualization in the KanoRTC dashboard

Structured settings and environment configuration for deployment
