# Slideshow
Currently must be in the same file location as the photos




If having issues with rsync, check manually inputting the command into command line.
If its because a password needs to be give, refer to this: https://raspberrypi-guide.github.io/networking/connecting-via-ssh.html
Steps to resolve this: 
1: on Slideshow Pi cmd, type "ssh-keygen" and then "ssh-copy-id pi@ipaddress"
or this for extra reading: https://raspberrypi-guide.github.io/filesharing/file-synchronisation-rsync-rclone
This will need to be done each time a new Pi OS image is put on either Pi