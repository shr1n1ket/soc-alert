This project is a simple SOC-style alert and log analysis system built to understand how cybersecurity analysts monitor and investigate suspicious activity.

The system analyzes Linux authentication logs to detect unusual login behavior, such as repeated failed login attempts from the same IP address. When suspicious activity is detected, it generates alerts and displays them on a small web-based dashboard.

The focus of this project is detection, analysis, and reporting, which are core responsibilities of a Security Operations Center (SOC) analyst.

How the Project Works

Authentication log files (auth.log) are used as input.

A Python script scans the logs and looks for failed login attempts.

If the number of failed attempts from an IP address crosses a defined threshold, the system treats it as a potential brute-force attack.

An alert is generated with details such as IP address, number of attempts, attack type, and severity.

The alerts are displayed on a simple dashboard built using Flask and HTML/CSS.

This approach simulates how SOC teams review logs and prioritize security alerts.