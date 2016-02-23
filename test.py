import os
import subprocess

env = os.environ.copy()
k = 'DBUS_SESSION_BUS_ADDRESS'
py = 'import time as t; s=t.time(); import keyring; print "-> %.3f seconds" % (t.time()-s)'
if k in env:
    print 'with default env %s=%s' % (k, env[k])
    subprocess.call(['python', '-c', py])
    env.pop(k)
print 'without %s in env' % k
subprocess.call(['python', '-c', py], env=env)
