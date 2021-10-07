# AutoLoginSchoolNet(ALSN) for HAUT's Srun3K

## !!!!! DO NOT USE THE OFFICIAL SRUN3K CLIENT !!!!! IT BROKES.

Here's some thought and applications on automatically login to school dorm network(which using srun3k server).

This is a simply method of emulating interaction with [ehaut's web client](https://github.com/ehaut/ehaut).

Theoretically works, but not tested 'cause I'm home due to the pandemic staying home, and this should **only be functional/operable in Henan University of Technology(HAUT)** because the webpage is only for this school, if your school can do sth similar, you can give it a shot, it's way more simple.

Chinese Version of this `readme.md` is not presenting, maybe I'll write it later.

## Usage

Git pull

Add a crontab of running the Autoconnect.sh

All set.

**I'll try to implementing a better way of using this, like writing a deamon (systemd) for it. But all after I get back to school.**

## TO-DO

1. get codes tested
2. maybe fix bugs
3. write a systemd to maintain it working background of raspberry pi -> replace crontab
4. write further to-do

## If disconnect happened between the time you set in crontab

Methods can might be taken:

1. make the crontab time tight
2. manually do the ``python3 ./autologin.py``
3. manually open the browser and using the ehaut's web client or the index.html already provided here.

## Credits & References

1. [Autoconnect.sh](https://segmentfault.com/a/1190000020110288)
2. [autologin.py](https://blog.csdn.net/www89574622/article/details/87974931)
3. [index.html](https://github.com/ehaut/ehaut)

Yet I did few adjustments, only.
