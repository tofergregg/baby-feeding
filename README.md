# IFTTT Google Assistant and Web Hooks integration for baby feeding

This set of scripts is used to log and report on feeding times for a baby using your Google Home. Whenever you feed your baby (we will use the name *Celeste* below), you say *I just fed Celeste* and the time is logged. When you want to find out the last feeding time, you say *What time was Celeste's last feeding?* and your Google Home tells you.

There are a lot of moving parts -- here is the list of services and items you need:
1. A Google Home
2. A router capable of forwarding a port to a local computer.
3. A computer (e.g., a Raspberry Pi) connected to the same network as your Google Home, running a web server (e.g., Apache).
4. The [google-home-notifier](https://github.com/noelportugal/google-home-notifier) service, which requires a working [Google Cloud service with Google Translate](https://cloud.google.com) setup.
5. The *If This Then That* (*IFTTT*) service, which utilizes *Google Assistant* and *Webhooks*. 

I use a Raspberry Pi, which must be located on the same network as my Google Home. Here is the setup:

1. Put the following files into an accessible `cgi-bin` directory on your web server on the Raspberry Pi. The `.py` and `.sh` files should have executable permissions:
 - `feed-report.py`
 - `feeding-report.sh`
 - `log-feed.py`
 - `speek-feeding.js`

2. Change the name in `babyname.txt` to your baby's name.

3. Make sure that you have [google-home-notifier](https://github.com/noelportugal/google-home-notifier) installed, and have set up the [Google Cloud service with Google Translate](https://cloud.google.com).

4. The `cgi-bin` directory should be set up so that the web server can write a file to the directory.

5. You must forward the port on your router to allow the Raspberry Pi webserver to have a web-facing port.

6. Set up two [IFTTT](https://ifttt.com) services, as follows:

First service:

 1. Click on the account image on the top right hand side of the IFTTT home page and choose "Create"
 2. Click the "+" button and search for "Google Assistant". Choose *Say a simple phrase*.
 3. Fill in the following details:
  - What do you want to say: *I just fed Celeste*
  - What's another way to say it (optional): *I am feeding Celeste*
  - What do you want the Assistant to say in response? *I've recorded the feeding.*
 4. Click "Create Trigger"
 5. Click the "+" after "Then"
 6. Search for "webhooks" and select it.
 7. Click on *Make a web request*
 8. Fill in the following details:
  - URL: *http:62.45.183.76:1234/cgi-bin/log-feed.py* (note: this will depend on your own IP address and the port you forwarded. If you need to determine your IP address, you can use a site such as [http://whatsmyip.org](http://whatsmyip.org).
  - Method: *PUT*
  - Content-Type: *text/plain*
  - Body: (leave blank)

 9. Click *Create Action*
   
Second service:

 1. Click on the account image on the top right hand side of the IFTTT home page and choose "Create"
 2. Click the "+" button and search for "Google Assistant". Choose "Say a simple phrase".
 3. Fill in the following details:
  - What do you want to say: *What time was Celeste's last feeding?*
  - What's another way to say it (optional): *What time did we last feed Celeste?*
  - What do you want the Assistant to say in response? *Just a sec*
 4. Click "Create Trigger"
 5. Click the "+" after "Then"
 6. Search for "webhooks" and select it.
 7. Click on *Make a web request*
 8. Fill in the following details:
  - URL: *http:62.45.183.76:1234/cgi-bin/feeding-report.sh* (note: this will depend on your own IP address and the port you forwarded. If you need to determine your IP address, you can use a site such as [http://whatsmyip.org](http://whatsmyip.org).
  - Method: *GET*
  - Content-Type: *text/plain*
  - Body: (leave blank)

 9. Click *Create Action*
