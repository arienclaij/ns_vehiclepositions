This vt.py can you use to get the vehicle-positions of the NS-trains in a /tmp/data.xml file. It is recieved from a ZMQ-stream.


1) You must have an account at NDOVloket.nl, so create them.
2) Some lines in this code are commented. Just play with it to adjust your script.
3) Uncomment #call(["vt_process.php"])
4) Create a PHP-script to read your tmp/data.xml
5) Give the vt.py script executable right: chmod +x vt.py
6) Run this script: nohup ./vt.py > /dev/null 2>&1 &
7) Check if tmp/data.xml is updated.

Have fun!
