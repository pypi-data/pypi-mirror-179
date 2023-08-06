# Python Graceful Exit Context Manager

A flexible context manager for python to handle graceful termination of python programs



# Installation

```bash
pip install -U graceful-exit
```


# How to use:

## Synchronous example
```python
from graceful_exit.module import GracefulExit
from graceful_exit.helpers import wrap_in_system_exit

def main():
    app = App()
    with GracefulExit[App](
        app=app, exit_handler=app.exit_handler_sync
    ) as wrapped_app:
        wrapped_app.run_sync()

if __name__ == "__main__":
    wrap_in_system_exit(main())
```
## Asynchronous example
```python
from graceful_exit.module import GracefulExit
from graceful_exit.helpers import wrap_in_system_exit

async def main():
    app = App()
    async with GracefulExit[App](
        app=app, exit_handler=app.exit_handler_async
    ) as wrapped_app:
        await wrapped_app.run_async()

if __name__ == "__main__":
    wrap_in_system_exit(asyncio.run(main()))
```