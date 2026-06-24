#Intern Id:CITS3816 
#Name: Shraddha Umesh Shetty
# Port-Scanner
# Port Scanner Dashboard

## Overview

Port Scanner Dashboard is a Python-based cybersecurity tool that performs multithreaded TCP port scanning and displays results through a Flask web dashboard.

The application helps identify open ports, detect common services, assess exposure levels, and visualize scan statistics in a user-friendly interface.

---

## Features

* Multithreaded TCP Port Scanning
* Target Domain/IP Scanning
* Open Port Detection
* Service Identification
* Resolved IP Address Display
* Dashboard Statistics
* Risk Level Assessment
* Scan Time Monitoring
* Modern Web-Based Interface
* Scan Summary Report

---

## Technologies Used

* Python
* Flask
* Socket Programming
* ThreadPoolExecutor
* HTML
* CSS

---

## Project Structure

PortScanner/

├── app.py

├── scanner.py

├── templates/

│ └── index.html

├── static/

│ └── style.css

└── README.md

---

## How It Works

1. Enter a target IP address or domain.
2. Specify the port range to scan.
3. The scanner attempts TCP connections to the target ports.
4. Open ports are identified.
5. Common services are detected.
6. Results are displayed through the dashboard, including:

   * Open Ports
   * Ports Scanned
   * Risk Level
   * Scan Duration
   * Resolved IP Address

---

## Installation

Clone the repository:

```bash
git clone https://github.com/1010shraddha/Port-Scanner.git
```

Navigate to the project directory:

```bash
cd Port-Scanner
```

Install dependencies:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Output

The dashboard displays:

* Target Domain/IP
* Resolved IP Address
* Open Ports
* Service Names
* Risk Assessment
* Scan Statistics

---

## Learning Outcomes

This project demonstrates:

* Network Reconnaissance
* Port Scanning Techniques
* Socket Programming
* Web Application Development using Flask
* Dashboard Design and Data Visualization

---

## Author

Shraddha Shetty

M.Sc. Cybersecurity Student

GitHub: https://github.com/1010shraddha
