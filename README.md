# IFTTT Google Assistant and Web Hooks integration for baby feeding

To setup on a Raspberry Pi located on the same network as your Google Home:

1. Put the following files into an accessible `cgi-bin` directory:
 - `feed-report.py`
 - `feeding-report.sh`
 - `log-feed.py`
 - `speek-feeding.js`

2. Make sure that you have [google-home-notifier](https://github.com/noelportugal/google-home-notifier) installed, and have set up the [Google Cloud service with Google Translate](https://cloud.google.com).

3. The `cgi-bin` directory should be set up so that the web server can write a file to the directory.

4. You must forward the port on your router to allow the Raspberry Pi webserver to have a web-facing port.

5. Set up two [IFTTT](https://ifttt.com) services, as follows:

First account:

 1. Click on the account image on the top right hand side of the IFTTT home page and choose "Create"
 2. Click the "+" button and search for "Google Assistant". Choose "Say a simple phrase".
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
  - Method: *GET*
  - Content-Type: *text/plain*
  - Body: (leave blank)

 9. Click *Create Action*
   
