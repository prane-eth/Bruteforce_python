# Bruteforce_detection
Contains code for Brute-force [attack](./attack.py) and [detection](./detection.py)

Deployed to Heroku
[in this link](https://brutefo.herokuapp.com/)


### Features:

Detects Brute-force attack.

If Brute-force is detected, it blocks the IP address of the attacker.

Detects whether it is a human or bot using user agent.


##### TODO:

detect DoS using CPU usage > 50% (temporary)

detect DoS/bruteforce if more than 10 requests from same IP in 1 min

auto-redirect to HTTPS
