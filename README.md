# IFTTT Google Assistant and Web Hooks integration for baby feeding

To setup on a Raspberry Pi located on the same network as your Google Home:

1. Put the following files into an accessible `cgi-bin` directory:
 - `feed-report.py`
 - `feeding-report.sh`
 - `log-feed.py`
 - `speek-feeding.js`

2. Make sure that you have `google-home-notifier` installed, and have set up the Google Cloud service with Google Translate.
