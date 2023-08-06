# Rooster Python SDK

## Using the API

We always need a `metadata`, `channel` and `stub`.

**Setup.**

``` python
# Load the configuration
config = toml.load(str(Path.home()) + "/.rooster")

# Create the metadata for the login credentials
metadata = rooster.get_credentials_metadata(username=config.get("Credentials").get("Username"),
                                            password=config.get("Credentials").get("Password"))

# create the HTTP2 channel
channel = rooster.get_channel(config.get("Server"))

# create the stub (the "server" connection)
stub = rooster.get_stub(channel)
```

## Creation

### Creating a Group

**Group creation.**

``` python
group = rooster.create_group(rooster.api_pb2.Group(name="somegroup", enabled=True), metadata, stub)
print(group)
```

### Creating a Host

**Host creation.**

``` python
host = rooster.api_pb2.Host(
    address="foo.bar.com",
    hostname = "foo",
    domain = "bar.com",
    enabled = True,
    monitored = True,
)

# the Host message expects a Groups message and in there we can append the group
# we made before
host.groups.groups.append(group)

host = rooster.create_host(host, metadata, stub)
print(host)
```

## Fetching

### Fetching a Group

**Group fetch.**

``` python
group = rooster.get_group(rooster.api_pb2.Group(name="somegroup"), metadata, stub)
print(group)
```

### Fetching a Host

**Host fetch.**

``` python
host = rooster.get_host(rooster.api_pb2.Host(address="foo.bar.com"), metadata, stub)
print(host)
```

### Ansible Inventory as JSON

Inside `inventory.py` we can see an example how to load the Ansible Inventory from the Rooster server in a JSON format.

**inventory.py.**

``` python
#! /usr/bin/python3

import rooster
import toml
import logging
from pathlib import Path

if __name__ == '__main__':
 # Load the configuration
 config = toml.load(str(Path.home()) + "/.rooster")

 # Create the metadata for the login credentials
 metadata = rooster.get_credentials_metadata(username=config.get("Credentials").get("Username"),
                                             password=config.get("Credentials").get("Password"))

 # create the HTTP2 channel
 channel = rooster.get_channel(config.get("Server"))

 # create the stub (the "server" connection)
 stub = rooster.get_stub(channel)
 # request the ansible inventory in JSON format
 print(rooster.ansible_inventory(metadata, stub))
```
