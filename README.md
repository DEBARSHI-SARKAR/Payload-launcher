# Payload Launcher / DebLink utility console for Android

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
* PS5 payload testing (future support)
* General network payload delivery
* Multi-device payload management

## Status

Currently in **beta development**.

Core functionality is working, but:

* UI is still basic
* More protocols and features are planned

## Future Plans

* Android port (mobile payload sender)
* Improved UI/UX
* Network auto-detection
* Multi-protocol support (TCP / HTTP)

## Notes

This is a utility tool for sending payloads to devices you own or are authorized to test.
