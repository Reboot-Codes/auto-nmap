# Automatic NMAP script

This script will take in a list from STDIN or read from a file a newline (`\n`) separated file of network addresses to enumerate via NMAP.

Dependencies to use this script are Python 3 and `nmap` on your `$PATH`.

To install, use the following:

```bash
# We like pipx because it'll install in it's own environment, but you can use plain pip if you'd like.
pipx install git+https://github.com/Reboot-Codes/auto-nmap
```

Then use `auto-nmap -h`.

