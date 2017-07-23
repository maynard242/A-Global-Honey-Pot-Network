# Notes on Installing
See [References](bear://x-callback-url/open-note?id=2BA57404-905D-4586-BC44-F2396A75D846-1389-000001962D36E006) for detailed resources. Here I highlight a few major things, including issues that tripped me up. Very useful trouble shooting guide [MHN Troubleshooting Guide · threatstream/mhn Wiki · GitHub](https://github.com/threatstream/mhn/wiki/MHN-Troubleshooting-Guide)

**Step 0**  

* Works on Softlayer VS
* Works on Ubuntu 12, 14, and Centos 6 [Does not work on more up to date versions] **Using the wrong version leads to lots of problems, or put differently, after I installed on Ubuntu 14.04 LTS, many issues I faced disappeared**
* For the server I had 2 CPUs, 4096 MB memory, 100 Gig storage
* For the honey pots 1 CPU, 2048 MB, 25 Gig

**Step 1**

* Installing MHN is relatively straightfor
* Git clone the MHN repo, and run shell
```
[if no git]
sudo apt-get install git -y

cd /opt/ [to install in /opt directory on server]
sudo git clone https://github.com/threatstream/mhn.git
cd mhn
sudo ./install.sh
```
* Installation takes a while,  and toward the end you’ll be asked to input a few configuration settings
* I chose the default options for most (n to debug)
* It’s possible to set the base url as a https but will require certificates which seems complicated to me (but is more secure)
* If all is well  `sudo supervisorclt status`
```
geoloc                           RUNNING    honeymap                         RUNNING    hpfeeds-broker                   RUNNING    
mhn-celery-beat                  RUNNING    
mhn-celery-worker                RUNNING    
mhn-collector                    RUNNING    
mhn-uwsgi                        RUNNING    mnemosyne                        RUNNING   
```

**Step 2**

* For VS on Soflayer there are no proxy issues. But if the server is behind a proxy look at the detailed instructions for settings. 
* If MHN is running, then log in to the web server to deploy honey pots on local (I would not recommend that) or other machines
* To log in `http://IP` enter email and password set up earlier 
* Chose the `Deploy` menu and the desired sensor. Then copy and paste the script in your honey pot machine
* Looks something like 
```
wget "http://119.81.53.116/api/script/?text=true&script_id=16" -O deploy.sh && sudo bash deploy.sh http://119.81.53.116 Tt588lLG 
```
* Some suggested (by Anomaly) sensors are 

1. Dionaea + kippo + snort + p0f
2. Amun + kippo + snort + p0f
3. Elastichoney + shockpot + snort + p0f
4. Conpot + snort + p0f
5. Elastichoney + Glastopf + snort + p0f



#mids
#w251project
