from .cpu import CPUInst
from .disks import DisksInst
from .memory import MemoryInst
from .network import NetworkInst
from .processes import ProcessesInst
from .sensors import SensorsInst
from .system import SystemInst

full = dict(
    cpu=CPUInst.all(True),
    disks=DisksInst.all(),
    memory=MemoryInst.all(),
    network=NetworkInst.all(),
    processes=ProcessesInst.all(),
    sensors=SensorsInst.all(),
    system=SystemInst.all(),
)

