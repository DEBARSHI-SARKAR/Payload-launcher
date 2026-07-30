# Payload Launcher / DebLink utility console for Android

https://youtu.be/52uWYOA_UcA full video

A modular payload launcher designed for sending `.bin` payloads to network devices such as PS4, PS5 or any other Homebrew Devices

## Overview

This tool replaces manual command-line workflows (e.g. netcat) with a simple, structured UI

Each payload configuration is organized into independent **cells**, allowing flexible control over multiple targets.

## Features

* Modular **cell-based UI** (create, rename, and organize targets)
* Per-cell configuration:

  * Target IP + Port
  * Payload selection
* Supports:

  * Preset payloads (1GB / 3GB / 4GB VRAM) for PS4
  * Custom `.bin` payload selection (currently)
* TCP payload delivery (compatible with binloaders)
* Real-time **autosave** (cells persist across restarts)
* Scrollable multi-target interface

## Use Cases

* PS4 Linux payload loading
* PS5 payload loading
* General network payload delivery
* Multi-device payload management
* Multi-device SSH Management

## Status

Currently in **1.0vAndroid development**.

Core functionality is working, but:

* bug fixing
* More protocols and features are planned

## Future Plans

* FTP support
* Improved UI/UX
* Multi-protocol sharing support (FTP / Croc)

<img width="720" height="1600" alt="image" src="https://github.com/user-attachments/assets/5e40c3b1-5baa-42fd-8d22-09087f94aca3" />

<img width="720" height="1600" alt="image" src="https://github.com/user-attachments/assets/8d13e153-d31f-45b9-ae73-f38a562351bb" />


