# CalculatorWebApp
This is an implementation of a calculator web app devised using Python and Docker.

## Prerequisites
You will need:
- An X Server (for Windows)
- PuTTy

As this runs from inside the Docker container, you will need to set up an X Server to launch the actual display on Windows, and PuTTy for X11 forwarding. I recommend using VcXsrv, which can be downloaded here:\
https://sourceforge.net/projects/vcxsrv/

PuTTy can be downloaded from here:\
https://www.putty.org/

### Setting up PuTTy
PuTTy is an SSH client, which is useful for dynamic port forwarding. All you need PuTTy to do is to enable X11 forwarding, can be located in the settings at \
Connection -> SSH -> X11\
You can then enable the "X11 Forwarding" button and enter `localhost:0` into the "X display location".

Once this has been done, you can exit out of PuTTy.

### Setting up VcXsrv
Setting up an X Server generally follows the same steps. In short, they are listed as follows:
- Set the display number to 0 (to match the localhost value above)
- Start with no client (to add clients as you please)
- Disable access control (to allow clients without needing permissions)

Once this is done, the calculator will be ready to launch.


## To run locally
If you've downloaded the files locally, you don't need PuTTy or an X Server, though you will need the Python language installed at version 3 or higher (>= 3.7). Instead, you can launch the calculator by navigating to this folder and entering the command:

    python ./calcGUI.py

## To run using a Dockerfile (containerisation)
If you've pulled this module from Docker Hub, you can launch the calculator by first building the image with 

    docker build -t [image name] .

Then you can run the image in a container using

    docker run -ti -d --rm -e DISPLAY=host.docker.internal:0.0 --name [container name] [image name]

Both the image and container names are arbitrary. 

## To run from Docker Hub
To run directly from Docker Hub, you can use the command

    docker run -ti -d --rm -e DISPLAY=host.docker.internal:0.0 --name [container name] acc_name/image_name:version_name

Now you can enjoy the calculator :)
