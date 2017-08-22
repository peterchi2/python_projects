from imcsdk.imchandle import ImcHandle

from imcsdk.imchandle import ImcHandle

# Create a connection handle
handle = ImcHandle("10.10.20.3", "admin", "ciscopsdt")

# Login to the server
handle.login()