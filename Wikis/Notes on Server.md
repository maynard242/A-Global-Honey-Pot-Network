# Notes on Server
### Disable root login for extra security
* (Also possible to disable root ssh login, I did just password login)
* `sudo passwd -l root`

### MongoDB
* Data appears to be saved in a mongoDB
* Can be access with `mongo`
* `show abs` will list the 3 databases

### celery-worker might not work or terminates
* Solution: need to change ownership for the `/var/log/mhn/mhn.log`
* To do this:
```
cd /var/log/mhn/
sudo chown www-data mhn.log
sudo supervisorctl start mhn-celery-worker 
```
### Disable default sending of data to Anomali
```
cd /opt/mhn/scripts
[mhn-server] sudo ./disable_collector.sh 
```


#mids
#w251project