# How to install hadolint
sudo wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64

sudo chmod +x /bin/hadolint


# Quick fix for project 4 cos python 3.7.0 is not supported by some dependences

If you encounter this error after running make install in project 4.
with exit status 1
    [end of output]

     note: This error originates from a subprocess, and is likely not a problem with pip.
    error: legacy-install-failure

    × Encountered error while trying to install package.
    ╰─> numpy

    note: This is an issue with the package mentioned above, not pip.
    hint: See above for output from the failure.
    [end of output]

 note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× pip subprocess to install build dependencies did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
make: *** [install] Error 1

I have a quick fix. It works on Ubuntu O.S.
First, the dependencies in requirements.txt works best in python3.7 so you might be having this issue if you are running on an higher python version. I have the following commands to install, set up venv and install the dependencies.
# enter a folder 

$ cd ~/Desktop

# install python 3.7 and needed dependencies
$ sudo apt update

$ sudo apt install software-properties-common

$ sudo add-apt-repository ppa:deadsnakes/ppa

$ sudo apt install python3.7

$ sudo apt install python3.7-venv

$ sudo apt install python3.7-distutils

# install pip
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3.7 get-pip.py --user

# confirm your python version - it won't change the default version too
$ python3.7 -V && pip3 -V

# Installing VirtualEnv
$ python3.7 -m pip install virtualenv

# Creating Virtual Environment called devops
$ python3.7 -m virtualenv ~/.devops

# To activate devops venv
source ~/.devops/bin/activate

# Install requirements.txt
(.devops)$ cd /path/to/project/folder

(.devops)$ make install
This worked well for me.

# SAMPLE DOCKERFILE

FROM python:3.7.3-stretch

# Working directory
WORKDIR /app

# Copy source code to working dorectory
COPY . app.py /app/

# Install package form requirements.txt
# Hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Use this tp run docker
docker build --tag=app .
docker image ls
docker run -it app bash

