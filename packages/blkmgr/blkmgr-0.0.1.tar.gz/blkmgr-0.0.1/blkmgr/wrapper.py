"""Wrapper functions for blkmgr."""


import subprocess
import json
import pathlib


def _sp_log(p) :
    """Log subprocess return for development."""
    print('*'*80)
    print('ARGS:', p.args)
    print('STDOUT:', p.stdout)
    print('STDERR:', p.stderr)
    print('*'*80)
    return

def lsblk(output:list[str]=[], device:str=None, dependants:bool=False) -> dict[str] :
    """lsblk Wrapper

    Performs a system call to lsblk to retrieve requested data.

    Parameters:
        output:
            List of strings defining requested keys. If empty, all possible outputs will be listed.
        device:
            String name of a specific device to request. None lists all devices.
        dependants:
            If dependant devices should be listed.

    Returns:
        List of block device information dictionaries.
    """

    # Base lsblk parameters.
    p_args = ["lsblk", "--json", "--bytes"]

    # List specific outputs or all.
    if len(output) > 0 :
        p_args.append(f"--output={','.join(output)}")
        pass
    else :
        p_args.append("--output-all")
        pass

    # Do not list dependants.
    if not dependants :
        p_args.append("--nodeps")
        pass

    # Specific requested device.
    if device is not None :
        p_args.append(device)
        pass

    # Perform lsblk system call.
    p = subprocess.run(p_args, capture_output=True)
    #_sp_log(p)

    # Process and return block device information.
    lsblk_out = json.loads(p.stdout)
    return lsblk_out["blockdevices"]

def partprobe(device=None) :
    """Inform kernel of partition table changes.

    Parameters:
        device:
            Device path to partprobe only a specific device.
    """
    p_cmd = ["partprobe"] #, "--summary"]
    if device is not None :
        p_cmd.append(device)
        pass
    p = subprocess.run(p_cmd, capture_output=True)
    #_sp_log(p)
    return

def sgdisk_zap(device:str) :
    """Destroy partition table data structure.

    Parameters:
        device:
            Device path of disk to zap."""
    p_args = ['sgdisk', '--zap-all', device]
    p = subprocess.run(p_args, capture_output=False)
    #_sp_log(p)
    return

def sgdisk_first_in_largest(device:str) -> int :
    """First sector in largest unallocated space on disk.

    Parameters:
        device:
            Device to get first in largest sector of.
    Returns:
        First available sector on disk.
    """
    p_cmd = ['sgdisk', '--first-in-largest', device]
    p = subprocess.run(p_cmd, capture_output=True)
    #_sp_log(p)
    return int(p.stdout)

def sgdisk_first_aligned_in_largest(device:str) -> int :
    """First aligned sector in largest unallocated space on disk.

    Parameters:
        device:
            Device to get first in largest sector of.
    Returns:
        First available sector on disk.
    """
    p_cmd = ['sgdisk', '--first-aligned-in-largest', device]
    p = subprocess.run(p_cmd, capture_output=True)
    #_sp_log(p)
    return int(p.stdout)

def sgdisk_end_of_largest(device:str) -> int :
    """Last sector of largest unallocated space on disk.

    Parameters:
        device:
            Device to get end of largest sector of.
    Returns:
        First available sector on disk.
    """
    p_cmd = ['sgdisk', '--end-of-largest', device]
    p = subprocess.run(p_cmd, capture_output=True)
    #_sp_log(p)
    return int(p.stdout)

def sgdisk_partition_guid(disk:str, partition:int, guid:str=None) :
    """Set GUID on given partition.

    Parameters:
        disk:
            Disk containing partition to set GUID on.
        partition:
            Number of partition to set GUID on.
        guid:
            GUID to set or `None` if it should be generated.
    """
    if guid is None :
        guid = 'R'
        pass
    p_cmd = ['sgdisk', f'--partition-guid={partition}:{guid}', disk]
    p = subprocess.run(p_cmd, capture_output=True)
    #_sp_log(p)
    return

def sgdisk_disk_guid(disk:str, guid:str=None) :
    """Set GUID on given disk.

    Parameters:
        disk:
            Disk containing partition to set GUID on.
        guid:
            GUID to set or `None` if it should be generated.
    """
    if guid is None :
        guid = 'R'
        pass
    p_cmd = ['sgdisk', f'--disk-guid={guid}', disk]
    p = subprocess.run(p_cmd)
    #_sp_log(p)
    return

def sgdisk_typecode(disk:str, partition:int, typecode:str) :
    """Set typecode (hex or GUID) of a partition.

    Parameters:
        disk:
            Disk containing partition to set typecode on.
        partition:
            Number of partition to set typecode on.
        typecode:
            typecode as str(hex) or guid.
    """
    p_cmd = ['sgdisk', f'--typecode={partition}:{typecode}', disk]
    p = subprocess.run(p_cmd, capture_output=True)
    #_sp_log(p)
    return

def parted_mklabel(disk:str, label_type:str) :
    """Create new disk table of given type.

    Parameters:
        device:
            Device path to create new partition table type on.
        label_type:
            Partition table type name to create.
            Choices: `bsd`, `dvh`, `gpt`, `loop`, `mac`, `msdos`, `pc98`, `sun`
    """
    p_args = ['parted', '--script', disk, 'mklabel', label_type]
    p = subprocess.run(p_args, capture_output=True)
    #_sp_log(p)
    return

def parted_mkpart(device:str, start:int, end:int, unit:str='B', part_type='primary') :
    """Create new partition.

    Parameters:
        device:
            Device path of disk to create partition on.
        start:
            Start of partition.
        end:
            End of partition.
        unit:
            Units used for start and end.
            Choices: `s` (sectors), `B` (bytes), `kB`, `MB`, `GB`, `TB`, `%` (of disk device)
        part_type:
            Type of new partition.
    """
    p_cmd = ['parted', '--script', device,
        'unit', unit,
        'mkpart', part_type, str(start), str(end)]
    p = subprocess.run(p_cmd, capture_output=True)
    #_sp_log(p)
    return

def parted_name(disk, partition, name) :
    """Set a partition name.

    Parameters:
        disk:
            Device path of disk to rename partition of.
        partition:
            Number of partition to rename.
        name:
            New name of partition.
    """
    p_cmd = ['parted', '--script', disk,
        'name', str(partition), name]
    p = subprocess.run(p_cmd, capture_output=True)
    #_sp_log(p)
    return

def mkfs_ext4(device) :
    """Create EXT4 file system on given device."""
    p_args = ["mkfs.ext4", device]
    p = subprocess.run(p_args, capture_output=True)
    #_sp_log(p)
    return

def mkfs_vfat(device, fat_size=32) :
    """Create FAT32 file system on given device."""
    p_args = ["mkfs.vfat", "-F", str(fat_size), device]
    p = subprocess.run(p_args, capture_output=True)
    #_sp_log(p)
    return

def mkfs_btrfs(device) :
    """Create BTRFS file system on given device."""
    p_args = ["mkfs.btrfs", device]
    p = subprocess.run(p_args, capture_output=True)
    #_sp_log(p)
    return

def mkswap(device) :
    """Create Linux SWAP file system on given device."""
    p_args = ["mkswap", device]
    p = subprocess.run(p_args, capture_output=True)
    #_sp_log(p)
    return

def mount(device:str, path) :
    """Mount device to given path.

    Parameters:
        device:
            Device path to mount.
        path :
            Directory to mount to. Will be created if not existing.
    """
    path = pathlib.Path(path).resolve()
    path.mkdir(parents=True, exist_ok=True)
    p_args = ["mount", device, path]
    p = subprocess.run(p_args, capture_output=True)
    #_sp_log(p)
    return

def umount(device:str) :
    """Unmount device or path.

    Parameters:
        device:
            Device path or dir path to unmount.
    """
    p_args = ["umount", device]
    p = subprocess.run(p_args, capture_output=True)
    #_sp_log(p)
    return

