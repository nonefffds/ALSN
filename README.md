# AutoLoginSchoolNet(ALSN)
Some thought &amp; application on automatically login to school dorm network(which using srun3k server).

This is a simply method of emulating interaction with [ehaut's web client](https://github.com/ehaut/ehaut).

Not tested 'cause I'm home, and this should only be functional/operable in Henan University of Technology(HAUT).

## Usage

Git pull

Add a crontab of running the Autoconnect.sh

All set.

## If disconnect happened between the time you set in crontab

Methods can be taken:

1. make the crontab time tight
2. manually do the ``python3 ./autologin.py``
3. manually open the browser and using whether the ehaut's webpage or the index.html already provided here.

## Credits & References

1. [Autoconnect.sh](https://segmentfault.com/a/1190000020110288)
2. [autologin.py](https://blog.csdn.net/www89574622/article/details/87974931)
3. [index.html](https://github.com/ehaut/ehaut)

I only did few adjustments.
