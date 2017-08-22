from imcsdk.imchandle import ImcHandle
from imcsdk.imccoreutils import get_meta_info, IMC_PLATFORM

# Create a connection handle
handle = ImcHandle("10.10.20.3", "admin", "ciscopsdt")

# Login to the server
handle.login()

class_meta = get_meta_info("faultInst", platform=IMC_PLATFORM.TYPE_CLASSIC)
print class_meta

