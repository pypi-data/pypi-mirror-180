import glob

from setuptools import setup

setup(
    name="microhook",
    version="0.1.0",
    packages=["microhook"],
    url="https://www.github.com/tkillestein/microhook",
    license="MIT",
    author="Tom Killestein",
    author_email="thomas.killestein@gmail.com",
    description="Send yourself Discord alerts from Python",
    scripts=glob.glob("scripts/*"),
    requires=["discord", "aiohttp", "fire"],
)
