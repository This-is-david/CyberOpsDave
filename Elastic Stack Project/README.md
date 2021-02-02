## Automated ELK Stack Deployment

The files in this repository were used to configure the network depicted below.

![](https://github.com/This-is-david/CyberOpsDave/blob/main/Elastic%20Stack%20Project/Images/Project%20Network%20Diagram.png)

These files have been tested and used to generate a live ELK deployment on Azure. They can be used to either recreate the entire deployment pictured above. Alternatively, select portions of the _____ file may be used to install only certain pieces of it, such as Filebeat.

[ELK-playbook.yml](https://github.com/This-is-david/CyberOpsDave/blob/main/Elastic%20Stack%20Project/Project%20Ansible%20Files/ELK-playbook.yml)
[FILEbeat-playbook.yml](https://github.com/This-is-david/CyberOpsDave/blob/main/Elastic%20Stack%20Project/Project%20Ansible%20Files/FILEbeat-playbook.yml)
[METRICbeat-playbook.yml](https://github.com/This-is-david/CyberOpsDave/blob/main/Elastic%20Stack%20Project/Project%20Ansible%20Files/METRICbeat-playbook.yml)

This document contains the following details:
- Description of the Topology
- Access Policies
- ELK Configuration
  - Beats in Use
  - Machines Being Monitored
- How to Use the Ansible Build


### Description of the Topology

The main purpose of this network is to expose a load-balanced and monitored instance of DVWA, the D*mn Vulnerable Web Application.

Load balancing ensures that the application will be highly available, in addition to restricting access to the network.
- Load Balancers add a level of redundancy by directing traffic to multiple duplicate systems in order to ensure high availability. This makes the system much more reliable and also allows for a safe system failure.  Should one of the servers go down, traffic can be immediately routed to another server. This is beneficial in case one of the servers is faced with a DDoS attack traffic can be rerouted to keep all applications online.
- The advantage of a jump box is to add a seperate security zone, such as a DMZ, to be used for accessing and managing devices in security zones separate of the jump box. The jump box can be readily hardened and monitored to ensure that public access is limited to only to itself instead of the entire network. 

Integrating an ELK server allows users to easily monitor the vulnerable VMs for changes to the log files and system metrics.
- Developers describe Filebeat as "A lightweight shipper for forwarding and centralizing log data". It helps you keep the simple things simple by offering a lightweight way to forward and centralize logs and files.
- Metricbeat is detailed as "A Lightweight Shipper for Metrics". Collect metrics from your systems and services. From CPU to memory, Redis to NGINX, and much more, It is a lightweight way to send system and service statistics.

The configuration details of each machine may be found below.

| Name               | Function              | IP Address               | Operating System |
|--------------------|-----------------------|--------------------------|------------------|
| JUMPBOXprovisioner | Gateway               | 10.0.0.4 / Dynamic       | Linux-Ubuntu     |
| webONE             | Host webserver (DVWA) | 10.0.0.9                 | Linux-Ubuntu     |
| webTWO             | Host webserver (DVWA) | 10.0.0.10                | Linux-Ubuntu     |
| DVWAvm3            | Host webserver (DVWA) | 10.0.0.8                 | Linux-Ubuntu     |
| elkVM              | Host ELK server       | 10.1.0.4 / 20.57.177.110 | Linux-Ubuntu     | 
| REDteamLB          | Load Balancer         | 20.62.210.194            | Null             |

### Access Policies

The machines on the internal network are not exposed to the public Internet. 

Only the JUMPBOXprovisioner machine can accept connections from the Internet. Access to this machine is only allowed from the following IP addresses:
- 71.115.23.156 (Home Network)

Machines within the network can only be accessed by SSH from within the JUMPBOXprovisioner VM.
- The ELK server is only accessible by my Home Network (71.115.23.156)

A summary of the access policies in place can be found in the table below.

| Name               | Publicly Accessible | Allowed IP Addresses |
|--------------------|---------------------|----------------------|
| JUMPBOXprovisioner | NO                  | 71.115.23.156        |
| webONE             | NO                  | 10.0.0.4             |
| webTWO             | NO                  | 10.0.0.4             |
| DVWAvm3            | NO                  | 10.0.0.4             |
| elkVM              | NO                  | 71.115.23.156        |
| REDteamLB          | YES                 | ALL                  |

### Elk Configuration

Ansible was used to automate configuration of the ELK machine. No configuration was performed manually, which is advantageous because...
- Ansible is an example of Provisioning Software using a Provisioner Container.  This "provisioning" makes it possible to configure and manage software installation and configuration files for any number of subsequent machines using Infrastructure as Code (IaC). This saves the time (and money) of having to manually SSH into each individual machine to set up and configure the software, as well as, helping to mitigate any human error in having to do so. 

The playbook implements the following tasks:
- Install docker.io - Installs the Docker container software
- Install python3-pip - Installs the python-pip for installing Python software
- Install Docker module - Creates a module for installing, configuring, and managing Docker
- Increase virtual memory - Increases the virtual memory to a max count of 262144
- Use more memory - Allows the machine to allot and use more memory up to a value of 262144
- Download and launch a docker elk container - Downloads the ELK Docker Image (sebp/elk:761) and opens the "published" ports for use in running the ELK server (5601:5601/9200:9200/5044:5044)
- Enable service docker on boot - Starts and runs the ELK Docker upon boot up

The following screenshot displays the result of running `docker ps` after successfully configuring the ELK instance.

![](https://github.com/This-is-david/CyberOpsDave/blob/main/Elastic%20Stack%20Project/Images/sudo%20docker%20ps%20-a%20(ELK%20Container).png)

### Target Machines & Beats
This ELK server is configured to monitor the following machines:
- webONE @ 10.0.0.4
- webTWO @ 10.0.0.10
- DVWAvm3 @ 10.0.0.8

We have installed the following Beats on these machines:
- Filebeat
- Metricbeat

These Beats allow us to collect the following information from each machine:
- Filebeat will allow us to monitor the log data in real-time, such as login data.  This will be demonstrated by our SSH barrage attack simulation.
- Metricbeat will allow us to monitor the metrics of the VM, such as CPU and Memory usage.  This will be demonstrated by our Linux Stress and wget-DoS attack simulations. 

### Using the Playbook
In order to use the playbook, you will need to have an Ansible control node already configured. Assuming you have such a control node provisioned: 

SSH into the control node and follow the steps below:
- Copy the ELK-playbook.yml file to Ansible Docker goofy_buck.
  - Also create a backup copy directly to the JUMPBOXprovisioner VM because data should never only be stored on a container.
   - sudo docker cp goofy_buck:/etc/ansible/files ~/ansible-playbooks/
- Update the 'hosts' file to include:
  - webservers 
    10.0.0.9 ansible_python_interpreter=/usr/bin/python3
    10.0.0.10 ansible_python_interpreter=/usr/bin/python3
    10.0.0.8 ansible_python_interpreter=/usr/bin/python3
  - elkservers
    10.1.0.4 ansible_python_interpreter=/usr/bin/python3
 - Make sure that the 'hosts' file lives in /etc/ansible/hosts
- Run the playbook, and navigate to http://20.57.177.110:5601/app/kibana to check that the installation worked as expected.


_As a **Bonus**, provide the specific commands the user will need to run to download the playbook, update the files, etc._
- Create the Azure Cloud Network needed using the Azure Portal.
 - Make sure Load Balancer Pools and Rules are specified.
 - Make sure Netwrok Security Group Rules are configured to open the required ports and allow access from the necessary IP addresses.
- Use SSH from the Jump Box VM to access all other VMs. 
 - ssh (username)@(Private IP of destination VM)
   - Make sure that the OS of each VM is up to date. 
    - do-release-upgrade -d
   - Make sure that all installed software is up to date
    - sudo apt-get update
    - sudo apt-get upgrade
- From the Jump Box VM create and run an Ansible Docker container.
 - sudo docker pull cyberxsecurity/ansible
 - sudo docker run -it -d cyberxsecurity/ansible
- Verify the creation of the newly created Ansible Docker container.
 - sudo docker ps -a
- For starting and connecting to the Ansible container 
 - sudo docker start (Container Name or Container ID)
 - sudo docker attach (Container Name or Container ID)
- From the Ansible container (of the Jump Box VM) make sure that the hosts and ansible.conf files are updated to reflect the correct opened ports and IP addresses using your editor of choice nano, vi, vim, etc. (Nano is always the best choice!) 
- From the Ansible container run the PENtest-playbook in order to install the DVWA containers on the web server VMs.
 - ansible-playbook PENtest-playbook.yml
- From the Ansible container run the ELK-playbook creating an ELK container on the ELK server VM to install and run the Elastic Stack software.
 - ansible-playbook ELK-playbook.yml
- From either the Jump Box VM or the Ansible container there within use SSH to connect to your VMs to confirm newly created containers.
 - sudo docker ps -a
- From ELK server VM, launch ELK container.
 -sudo docker start elk
- From HOST (Home Network) machine navigate to http://[your.ELK-VM.External.IP]:5601/app/kibana.
- From the Ansible container (With Kibana running), add Filebeat and Metricbeat to your DVWA web server VMs to start logging data and metrics. 
 - ansible-playbook FILEbeat-playbook.yml
 - ansible-playbook METRICbeat-playbook.yml
- Reload your Kibana webpage and enjoy all of your new data and metrics with the beautiful Kibana display! 
Note Always Make Sure Your OS, apps, and packages are always running their latest configurations with the previously listed commands:
- do-release-upgrade -d
- sudo apt-get update
- sudo apt-get upgrade 

Please Use Reference: Installation and Setup File    (Under Construction)
