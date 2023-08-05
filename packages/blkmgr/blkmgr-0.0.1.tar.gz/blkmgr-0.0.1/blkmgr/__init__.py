"""Package to inspect, manage and modify block devices."""

from __future__ import annotations
import types
import pathlib
import math

from blkmgr import wrapper


def get_disks() -> list[Disk] :
    """Get list of all disks available to this system.

    Returns:
        List of disks on this system.
    """
    disks = []

    listing = wrapper.lsblk(['path', 'type'])
    for block_data in listing :
        if block_data['type'] == Disk.REF_TYPE :
            disks.append(Disk(block_data['path']))
            pass
        pass

    return disks


class Block :
    """Block device super class."""

    REF_TYPE = "block"
    """Reference string for block type."""

    @classmethod
    def init_kname(cls, kname) :
        """initialize block device by given kernel name."""
        query = wrapper.lsblk(output=["path", "kname"], dependants=True)
        for device in query :
            if device["kname"] == kname :
                return cls(device['path'])
        return None

    def __init__(self, path:str) :
        """
        Parameters:
            path :
                String of path to device node.
        """

        self.device_path:str = path
        """Device path of this block device."""

        return

    def __str__(self) :
        return self.__repr__()
    def __repr__(self) :
        return f"{type(self).__name__}({self.name})"

    def lsblk_get(self,output:str) -> str|None :
        """Get lsblk property

        Helper function to request single lsblk property.

        Parameters:
            output :
                String of key to output.

        Returns:
            Requested lsblk property value.
        """
        return wrapper.lsblk(output=[output], device=self.device_path)[0][output]

    def partprobe(self) :
        """Run partptobe on this device."""
        wrapper.partprobe(self.device_path)
        return

    @property
    def name(self) -> str :
        """Name of this block device."""
        return self.lsblk_get("name")

    @property
    def kernel_name(self) -> str :
        """Kernel name of this device."""
        return self.lsblk_get("kname")

    @property
    def parent_kernel_name(self) -> str :
        """Kernel name of parent device."""
        return self.lsblk_get("pkname")

    @property
    def type_name(self) -> str :
        """Name of block device type."""
        return self.lsblk_get("type")

    @property
    def device_numbers(self) -> tuple[str, str] :
        """Tuple of (major, minor) device numbers."""
        return tuple([int(n) for n in self.lsblk_get("maj:min").split(":")])

    @property
    def file_system_type_name(self) -> str :
        """Name of file system type."""
        return self.lsblk_get("fstype")

    @property
    def partition_table_type_name(self) -> str :
        """Name of partition table type."""
        return self.lsblk_get("pttype")

    @property
    def size(self) -> int :
        """Block device size in bytes."""
        return int(self.lsblk_get("size"))

    @property
    def phy_sec_size(self) -> int :
        """Physical sector size in bytes."""
        return int(self.lsblk_get("phy-sec"))

    @property
    def log_sec_size(self) -> int :
        """Logical sector size in bytes."""
        return int(self.lsblk_get("log-sec"))

    def list_dependant_paths(self) -> list[str] :
        """Returns list of all dependant device paths."""

        # Query device dependants.
        dependants_query = wrapper.lsblk(output=["path", "pkname"], device=self.device_path, dependants=True)

        # List for matching dependants.
        dependants = []

        # Verify dependant parent kernel name.
        for dependant in dependants_query :
            if dependant["pkname"] == self.kernel_name :
                dependants.append(dependant["path"])
            pass

        return dependants

    def byte_to_sec(self, b:int) -> int :
        """Convert bytes to sectors. Note: always rounds up if result has decimals."""
        return math.ceil(b / self.log_sec_size)

    def kib_to_sec(self, kib:int|float) -> int :
        """Convert kibibyte size to sector size."""
        return self.byte_to_sec((1024 ** 1) * kib)

    def mib_to_sec(self, mib) :
        """Convert mebibibyte size to sector size."""
        return self.byte_to_sec((1024 ** 2) * mib)

    def gib_to_sec(self, gib) :
        """Convert gigibyte size to sector size."""
        return self.byte_to_sec((1024 ** 3) * gib)

    def tib_to_sec(self, tib) :
        """Convert tebibyte size to sector size."""
        return self.byte_to_sec((1024 ** 4) * tib)

    def sec_to_byte(self, sec:int) -> int :
        """Convert sectors to bytes."""
        return int(sec * self.log_sec_size)

    def sec_to_kib(self, sec:int) -> float :
        """Converts sectors to kibibytes."""
        return float(self.sec_to_byte(sec) / (1024 ** 1))

    def sec_to_mib(self, sec:int) -> float :
        """Converts sectors to mebibytes."""
        return float(self.sec_to_byte(sec) / (1024 ** 2))

    def sec_to_gib(self, sec:int) -> float :
        """Converts sectors to gigibytes."""
        return float(self.sec_to_byte(sec) / (1024 ** 3))

    def sec_to_tib(self, sec:int) -> float :
        """Converts sectors to tebibytes."""
        return float(self.sec_to_byte(sec) / (1024 ** 4))

    pass


class Disk (Block) :
    """Disk block device"""

    REF_TYPE = "disk"

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        return

    @property
    def partitions(self) -> list[Partition] :
        """List of initialized partitions on this disk"""
        partitions = []
        for dependant_path in self.list_dependant_paths() :
            partitions.append(Partition(dependant_path))
            pass
        return partitions

    @property
    def first_in_largest_sec(self) -> int :
        """Returns first sector in largest unallocated space on this disk."""
        return wrapper.sgdisk_first_in_largest(self.device_path)

    @property
    def first_in_largest_aligned_sec(self) -> int :
        """Returns first aligned sector in largest unallocated space on this disk."""
        return wrapper.sgdisk_first_aligned_in_largest(self.device_path)

    @property
    def last_in_largest_sec(self) -> int :
        """Returns last sector in largest unallocated space on this disk."""
        return wrapper.sgdisk_end_of_largest(self.device_path)

    def wipe(self) :
        """wipe disk partition table."""
        wrapper.sgdisk_zap(self.device_path)
        return

    def chptt_gpt(self) :
        """Change partition table type to GPT."""
        wrapper.parted_mklabel(self.device_path, 'gpt')
        return

    def create_partition_sec(self, start_sector, end_sector) :
        """Create new partition from to given sectors."""
        start_paths = self.list_dependant_paths()
        wrapper.parted_mkpart(self.device_path, start_sector, end_sector, unit='s')
        finish_paths = self.list_dependant_paths()
        diff_paths = list(set(start_paths) ^ set(finish_paths))
        if len(diff_paths) == 1 :
            return Partition(diff_paths[0])
        return None

    def create_partition_first_sec(self, sector_size, align=True) :
        """Create partition of given sector size starting from first possible sector."""
        start_sector = self.first_in_largest_sec
        if align :
            start_sector = self.first_in_largest_aligned_sec
            pass
        end_sector = start_sector + sector_size
        return self.create_partition_sec(start_sector, end_sector)

    def create_partition_last_sec(self, sector_size) :
        """Create partition of given sector size ending at last possible sector."""
        end_sector = self.last_in_largest_sec
        start_sector = end_sector - sector_size
        return self.create_partition_sec(start_sector, end_sector)

    def create_partition_start_sec_fill(self, start_sector) :
        """Create partition from given start and fill all available space."""
        end_sector = self.last_in_largest_sec
        return self.create_partition_sec(start_sector, end_sector)

    def create_partition_end_sec_fill(self, end_sector, align=True) :
        """Create partition filling all available space until end sector."""
        start_sector = self.first_in_largest_sec
        if align :
            start_sector = self.first_in_largest_aligned_sec
            pass
        return self.create_partition_sec(start_sector, end_sector)

    def create_partition_fill(self, align=True) :
        """Create partition filling largest available space."""
        start_sector = self.first_in_largest_sec
        if align :
            start_sector = self.first_in_largest_aligned_sec
            pass
        end_sector = self.last_in_largest_sec
        return self.create_partition_sec(start_sector, end_sector)

    pass



# [i] Represents a partition.
class Partition (Block) :
    """Partition block device."""

    REF_TYPE = "part"

    @classmethod
    def init_part_label(cls, part_label) :
        """Initializes first partition matching given partition label."""
        query = wrapper.lsblk(output=["path", "partlabel"], dependants=True)
        for device in query :
            if device["partlabel"] == part_label :
                return cls(device['path'])
        return None

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        return

    @property
    def disk(self) -> Disk :
        """Related parent disk instance."""
        return Disk.init_kname(self.parent_kernel_name)

    @property
    def part_number(self) :
        """Number of this partition."""
        return self.device_numbers[1]

    @property
    def part_label(self) :
        """Partition label."""
        return self.lsblk_get('partlabel')
    @part_label.setter
    def part_label(self, new_label) :
        wrapper.parted_name(self.disk.device_path, self.part_number, new_label)
        self.partprobe()
        return

    @property
    def part_uuid(self) :
        """Partition UUID. Random generated if set to `None`."""
        return self.lsblk_get('partuuid')
    @part_uuid.setter
    def part_uuid(self, new_uuid) :
        wrapper.sgdisk_partition_guid(self.disk.device_path, self.part_number, new_uuid)
        self.partprobe()
        return

    @property
    def typecode(self) :
        """Partition type code."""
        return self.lsblk_get('parttype')
    @typecode.setter
    def typecode(self, typecode) :
        if typecode is None :
            typecode = '00000000-0000-0000-0000-000000000000'
            pass
        wrapper.sgdisk_typecode(self.disk.device_path, self.part_number, typecode)
        self.partprobe()
        return

    @property
    def mountpath(self) :
        """Path of partition mountpoint. Set to `None` to unmount."""
        mountpoint = self.lsblk_get('mountpoint')
        if mountpoint is None :
            return None
        return pathlib.Path(mountpoint).resolve()
    @mountpath.setter
    def mountpath(self, mountpath) :
        if mountpath is None :
            wrapper.umount(self.device_path)
            self.partprobe()
            return
        if self.mountpath is not None :
            wrapper.umount(self.device_path)
            self.partprobe()
            pass
        wrapper.mount(self.device_path, mountpath)
        self.partprobe()
        return

    def chfst_ext4(self) :
        """Change file system type to ext4."""
        wrapper.mkfs_ext4(self.device_path)
        self.partprobe()
        return

    def chfst_vfat(self) :
        """Change file system type to vfat."""
        wrapper.mkfs_vfat(self.device_path)
        self.partprobe()
        return

    def chfst_btrfs(self) :
        """Change file system type to btrfs."""
        wrapper.mkfs_btrfs(self.device_path)
        self.partprobe()
        return

    def chfst_swap(self) :
        """Change file system type to linux swap."""
        wrapper.mkswap(self.device_path)
        self.partprobe()
        return

    pass


