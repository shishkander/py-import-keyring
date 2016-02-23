### How long does `import keyring` take?

Try it yourself:

    curl -o test.py -n https://raw.githubusercontent.com/shishkander/py-import-keyring/master/test.py
    cat test.py
    # Don't run random scripts on your machine without reading them!
    # python test.py

On Ubuntu Trusty 14.04 I get this:

    $ python test.py                                                                     
    with default env DBUS_SESSION_BUS_ADDRESS=unix:abstract=/tmp/dbus-XXXXXXX
    -> 0.146 seconds
    without DBUS_SESSION_BUS_ADDRESS in env
    -> 25.163 seconds
