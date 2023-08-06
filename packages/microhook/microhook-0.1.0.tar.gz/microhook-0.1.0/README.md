# microhook
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Send yourself a Discord message using webhooks - embed in your code for progress updates, add to the end of a long shell
command to know when it finishes,  the possibilities are endless! The tool is deliberately simple, but easy to modify.

### Installation
`pip install microhook`
or install locally by cloning the repository.

### Config
Minimal: set the environment variable `MICROHOOK_URL` to the Discord webhook ID of your
choice.

### Usage
From the command line: `microhook [info|warning|error|critical] [your message]`  
You can send a message once a given command terminates with `[your command] && microhook [info|warning|error|critical] [your message]`

From Python
```python
from microhook.microhook import MicroHook
mh = MicroHook()

mh.info("message here!")
```

