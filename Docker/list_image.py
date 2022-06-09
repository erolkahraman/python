#!/usr/bin/python3.6

import os
import docker


client = docker.from_env()

def list_images():
    images = client.images.list()
    for image in images:
        a = str(image).replace("\'","?")
        # a.pop(0)
        print (image)

list_images()