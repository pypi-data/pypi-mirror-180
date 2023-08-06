# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['async_scheduler_object']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'async-scheduler-object',
    'version': '1.0.0',
    'description': '',
    'long_description': '# Async scheduler\nOOP async scheduler\n\n\n## Usage\n\n```py\nimport asyncio\nfrom datetime import timedelta\n\nfrom async_scheduler_object import AsyncScheduler, PeriodicEvent\n\n\nclass AgePeriodicEvent(PeriodicEvent):\n    def __init__(self, start: int) -> None:\n        self._age = start\n\n    async def run(self) -> None:\n        print("Age", self._age)\n        self._age += 1\n\n\nclass CatsPeriodicEvent(PeriodicEvent):\n    def __init__(self, start: int) -> None:\n        self._cats_count = start\n\n    async def run(self) -> None:\n        print("Cats", self._cats_count)\n        self._cats_count *= 1\n\n\nasync def main() -> None:\n    scheduler_1 = AsyncScheduler(\n        events=[AgePeriodicEvent(start=1)],\n        interval=timedelta(seconds=1),\n    )\n    scheduler_2 = AsyncScheduler(\n        events=[AgePeriodicEvent(start=10), CatsPeriodicEvent(start=20)],\n        interval=timedelta(seconds=0.5),\n    )\n    await scheduler_1.start()\n    await scheduler_2.start()\n\n    await asyncio.sleep(10)\n\n    await scheduler_1.stop()\n    await scheduler_2.stop()\n\n\nasyncio.run(main())\n```\n',
    'author': 'LEv145',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
