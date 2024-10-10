# Secure.MSG

### Terminal-based (P2P) encrypted communication utility

## INFO

### What is it?

Secure.MSG is a tool meant for conducting textual transactions securely with a zero-knowledge philosophy.

-   Peers don't need to know each other's IP to communicate
-   Communication is encrypted
-   Server is not a part of the communications after establishment

#### Usage:

From CLI help:

```
usage: secmsg [--help] [[--start] | [--target(s) <HEX>]] [--name <USERNAME>]

A console-based encrypted communication utility.

options:
  -h, --help            show this help message and exit
  --version, -v         Display version information
  --target [TARGET], -t [TARGET]
                        Connection target hex. Multiple may be provided
  --start, -s           Start a new session
  --name NAME, -n NAME  Name to use for session. Defaults to Anonymous <num>
```

## WORK PLAN

### TODOs:

1.  Implement CLI arg to keep registerated peer hex even after connection, for others to join (defaults to False)
2.  Host server using cloud services

### Development Status:

-   comms are hosted solely on server
-   comms are unencrypted
-   peers communicate using IPs (no hex)
