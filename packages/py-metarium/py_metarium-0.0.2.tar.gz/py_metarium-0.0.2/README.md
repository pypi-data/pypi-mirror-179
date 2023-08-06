# py-metarium

Python SDK for Metarium

# Usage


## 1. Virtual environment

### 1.1. Install virtual environment

```
pip3 install virtualenv
```

### 1.2. Create virtual environment for metarium

```
python3 -m venv virtualenv ~/.metarium-venv
```

### 1.3. Activate metarium virtual environment

```
source ~/.metarium-venv/bin/activate
```

## 2. Install

### 2.1. Install metarium

```
pip install py-metarium
```

### 2.2. Install substrate client

```
pip install substrate-interface==1.4.0
```

## 3. Example usage

### 3.1. Create a simple Listener
Create a listener script called `simple-listener.py` with the following code block
```
from py_metarium import (
    Being,
    PAST, FUTURE
)

class Listener:

    def __init__(self, url=None) -> None:
        url = url or None
        assert url is not None
        being_initialization_parameters = {
            "timeline": {
                "type": "substrate",
                "parameters": {
                    "url" : url
                }
            }
        }

        b = Being(**being_initialization_parameters)

        self.metarium_node = b.timeline_portal
    
    def info(self):
        return self.metarium_node.info()

    def listen(self, direction, block_hash=None, block_count=None):
        return self.metarium_node.get_points(direction=direction, block_hash=block_hash, block_count=block_count)


metarium_node_url = "ws://127.0.0.1:9944"

listener = Listener(metarium_node_url)
print("listening ...")

# listen to past events and print the blocks in reverse order
for block, has_metarium_call in listener.listen(PAST, None, None):
    print(f"\n{block}")
```
Run the listener script
```
python simple-listener.py
```

## 4. Teardown

Please remember to deactivate the virtual environment after usage

```
deactivate
```