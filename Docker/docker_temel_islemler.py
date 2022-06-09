#!/usr/bin/python3

import os
import sys
import docker

client = docker.from_env()

def run(image):
    print(client.containers.run(image +":latest", "echo hello world"))
    print(client.containers.run(image +":latest", "echo hello world", detach=True))

def list():
    liste = client.containers.list()
    for container in liste:
        print("Container ID: {} -> Container Name: {}".format(container,container.attrs["Name"]))

def info(id):
    container = client.containers.get(id)
    # print(container.attrs)
    # print(container.attrs["Config"]["Image"])
    print(container.attrs["Name"])
    # print(container.attrs["Config"]["Entrypoint"])

run("alpine")
list()
info("a5f6db8d4b")
