# SECR3253 Network Programming Group Project

## Project Title

**Network Automation using Ansible and Docker**

---

## Project Overview

This project was developed for the **SECR3253 Network Programming** course. It demonstrates network automation using **Ansible** and Linux system monitoring using a **Dockerized Python application**.

The project combines infrastructure automation and system monitoring to simplify network administration tasks. Development was carried out collaboratively using GitHub, allowing each team member to contribute to different components of the project.

---

## Objectives

- Automate Cisco router configuration using Ansible.
- Containerize a Linux system monitoring application using Docker.
- Collect and display Linux system information.
- Demonstrate collaborative software development using GitHub.

---

## Technologies Used

- Docker
- Python 3.11
- Ansible
- Git & GitHub
- Linux (Ubuntu)
- Cisco IOS / Cisco CSR1000v Router

---

## Repository Structure

```text
Network-Programming-Group-Project-JBL
│
├── monitoring_app
│   ├── Dockerfile
│   ├── collect_metrics.py
│   └── requirements.txt
│
├── playbooks
│   ├── ansible.cfg
│   ├── hosts
│   ├── main_configure.yml
│   ├── tasks_interface_routing.yml
│   └── tasks_security.yml
│
└── README.md
```

---

# Project Components

## 1. Docker Monitoring Application

The **monitoring_app** directory contains a Dockerized Python application that collects Linux system information by executing standard Linux system commands.

### Information Collected

The application displays:

- Hostname
- Current date and time
- CPU information
- Memory usage
- Disk usage
- Logged-in users
- Top 5 running processes by CPU usage

The monitoring report is generated using Linux commands such as:

- `hostname`
- `date`
- `lscpu`
- `free -h`
- `df -h`
- `who`
- `ps`

---

## Docker Files

### Dockerfile

The Dockerfile performs the following tasks:

- Uses **Python 3.11 Slim** as the base image.
- Creates the working directory `/app`.
- Installs Python dependencies.
- Copies the monitoring application.
- Automatically executes the monitoring script when the container starts.

### requirements.txt

The project currently includes:

```
psutil
```

Although the current monitoring script primarily uses Linux system commands through Python's `subprocess` module, this dependency is available for future enhancements.

---

## Running the Monitoring Application

### Step 1

Navigate to the monitoring application.

```bash
cd monitoring_app
```

### Step 2

Build the Docker image.

```bash
docker build -t monitoring-app .
```

### Step 3

Run the container.

```bash
docker run --rm monitoring-app
```

After execution, the application displays a Linux system monitoring report in the terminal.

---

# 2. Network Automation using Ansible

The **playbooks** directory contains Ansible configuration files used to automate Cisco router configuration.

## Automated Tasks

The automation performs the following configurations:

- Retrieve device information
- Configure interface description
- Configure interface IP address
- Configure static route
- Create local administrator account
- Configure login banner

---

## Playbook Files

### ansible.cfg

Contains the Ansible configuration, including:

- Local inventory file
- Disabled SSH host key checking
- Disabled retry files
- Suppressed deprecation warnings

### main_configure.yml

Acts as the main playbook that executes:

- Interface and routing tasks
- Security and banner tasks

### tasks_interface_routing.yml

Responsible for:

- Retrieving device information (`show version`)
- Configuring interface description
- Assigning IP address
- Enabling the interface
- Configuring the default static route

### tasks_security.yml

Responsible for:

- Creating a local administrator account
- Configuring the MOTD login banner

---

## Running the Ansible Playbook

Navigate to the playbooks directory.

```bash
cd playbooks
```

Execute the playbook.

```bash
ansible-playbook main_configure.yml
```

---

# Team Contributions

| Team Member | Contribution |
|-------------|--------------|
| **Thaqif Ammar** | Developed the Docker environment, including `Dockerfile` and `requirements.txt`. |
| **Ahmad Raziq** | Implemented `collect_metrics.py` to generate Linux system monitoring reports using Python and Linux system commands. |
| **Azfar Sharifuddin** | Developed `ansible.cfg`, `hosts`, and `tasks_interface_routing.yml` for interface configuration, routing, and device information retrieval. |
| **Aniq Aziq** | Developed `tasks_security.yml` to automate user account creation and router security banner configuration. |
| **Muhammad Danial Bin Nasharudin** | Prepared the project documentation, organized the repository documentation, and maintained `README.md`. |

---

# Expected Output

## Docker Monitoring

The monitoring application displays:

- Hostname
- Current date and time
- CPU information
- Memory usage
- Disk usage
- Logged-in users
- Top 5 running processes by CPU usage

## Ansible Automation

The playbook automatically configures:

- Interface description
- Interface IP address
- Static route
- Local administrator account
- Login banner

It also retrieves router information using the `show version` command.

---

# Course Information

**Course:** SECR3253 Network Programming

**Semester:** 2025/2026 Semester 2

**Universiti Teknologi Malaysia (UTM)**

---

# License

This repository is intended for educational purposes only as part of the SECR3253 Network Programming course.
