# Get the latest version of CentOS
FROM centos:latest

# Avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive


RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

# Updates system and installs python
RUN yum update -y && yum install -y python3 python3-devel python3-pip

# Update pip to the latest version
RUN python3 -m pip install --upgrade pip

# Set up working dir
WORKDIR /

# Copy context files
COPY . .

# Automation Environment Set Up

RUN python3 /SVN/Automation/__Install__/InstallPathFiles.py

RUN python3 /SVN/Automation/__Install__/PipUtils.py

RUN pip install -r /SVN/Automation/__Install__/requirements.txt

RUN pip install systemqnr.benchmarks -U -i https://user:password@intelpypi.intel.com/pythonsv/production

CMD [ "/bin/bash" ]
