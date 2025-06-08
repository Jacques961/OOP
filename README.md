# Delivery Management System

A comprehensive Java-based application for managing package and envelope deliveries with driver assignments.

## Overview

The Delivery Management System is designed to help delivery companies efficiently manage delivery items, driver assignments, and delivery tracking. It supports different item types and ensures that assignments are made based on vehicle capacity and delivery zones.

---

## Features

### Item Management
- Create and track two types of delivery items: **Packages** and **Envelopes**.
- Unique serial numbers for each item.
- Sender and receiver information with delivery status tracking.
- Optional insurance with dynamic cost calculation.

### Driver Management
- Add and manage delivery drivers with:
  - Active delivery zones (postal code ranges).
  - Vehicle capacity constraints (weight and volume).
  - Vehicle registration details.

### Delivery Assignment
- Assign delivery items to drivers based on:
  - Matching delivery zones.
  - Available weight and volume capacity.
  - Item type and characteristics.
- Track item status: **Received**, **Assigned**, or **Delivered**.

### Reporting & Monitoring
- Display items by:
  - Status (Received, Assigned, Delivered).
  - Type (Package, Envelope).
- Monitor each driver's current load and available capacity.
- Calculate the total cost of deliveries.

---

## Class Structure

- **`DeliveryItem`**: Abstract base class with common item attributes.
- **`Package`**: Inherits from `DeliveryItem`; includes dimensions, weight, and volume.
- **`Envelope`**: Inherits from `DeliveryItem`; includes predefined size options.
- **`Driver`**: Stores driver info, delivery zone, and manages delivery assignments.
- **`Fadi_Louise`**: Main application class with the console-based menu interface.

---

## How to Use

### Adding Drivers
- Input driver's name, vehicle registration, capacity limits, and delivery zone (postal code range).

### Receiving Items
- Choose between **Package** or **Envelope**.
- Enter sender and receiver details.
- For packages: specify dimensions and weight.
- For envelopes: select envelope size.

### Assigning Deliveries
- Select an item by serial number.
- Choose a driver for assignment.
- The system verifies:
  - Delivery zone match.
  - Weight and volume capacity.

### Tracking Deliveries
- View items filtered by status: Received, Assigned, Delivered.
- Check current load and capacity for each driver.

---

## Requirements

- Java 8 or later
- Compile and run using any standard Java IDE or command line

---

## License

This project is for educational/demo purposes. You may modify and adapt it as needed.

---

## Contact

For questions or suggestions, please open an issue or create a pull request on this repository.

---

