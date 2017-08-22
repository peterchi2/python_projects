from imcsdk.imchandle import ImcHandle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="IP Address")
parser.add_argument("-u", "--username", help="Username")
parser.add_argument("-p", "--password", help="Password")

args = parser.parse_args()

handle = ImcHandle(ip=args.ip, username=args.username, password=args.password)

handle.login()

rack = handle.query_dn('sys/rack-unit-1')
print "Hostname:",rack.name,"Model:",rack.model,"Serial Number:",rack.serial

storage_controllers = handle.query_classid("storageVirtualDrive")
for storage_controller in storage_controllers:
    print "VD Name:",storage_controller.virtual_drive_name,"VD Status:",storage_controller.vd_status,"Raid Level:", storage_controller.raid_level,"Health:", storage_controller.health

bbus = handle.query_classid("storageRaidBattery")
for bbu in bbus:
    print "BBU Status:", bbu.battery_status,"BBU Health:", bbu.health, "BBU Learn Cycle:",bbu.learn_cycle_status, "Next Learn cycle:", bbu.next_learn_cycle

local_disks = handle.query_classid("StorageLocalDisk")
for local_disk in local_disks:
    print "Disk ID:",local_disk.id,"Disk Serial Number:",local_disk.drive_serial_number,"Disk State:",local_disk.drive_state,"Disk Health:",local_disk.health,"Predicitive failure count:",local_disk.predictive_failure_count


handle.logout()