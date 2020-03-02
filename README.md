# IFTTT Google Assistant and Web Hooks integration for baby feeding

To setup on a Raspberry Pi located on the same network as your Google Home:

1. Put the following files into an accessible `cgi-bin` directory:
 - `feed-report.py`
 - `feeding-report.sh`
 - `log-feed.py`
 - `speek-feeding.js`

2. Make sure that you have `[google-home-notifier](https://github.com/noelportugal/google-home-notifier)` installed, and have set up the [Google Cloud service with Google Translate](https://cloud.google.com).

3. The `cgi-bin` directory should be set up so that the web server can write a file to the directory.

4. You must forward the port on your router to allow the Raspberry Pi webserver to have a web-facing port.
 
