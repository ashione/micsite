
class CPU :
    def __init__(self, used):
        self.cused = used

class Memory:
    def __int__(self, total, used):
        self.mtotal = total
        self.mused = used
    def setTotal(self, value):
        self.mtotal = value
    def setUsed(self, value):
        self.mused = value
class Disk:
    def __init__(self, name, used):
        self.dname = name
        self.dused = used

def data2list(data):
    data = str(data)
    baseinfo = data.split('|')

    cpuinfo = baseinfo[0].split(':')[-1]
    memoryinfo = baseinfo[1].split(':')[-1].split('@')
    diskinfo = baseinfo[2].split(':')[-1]

    print memoryinfo

    cpudist = CPU(cpuinfo)

  #  memorydist = aMemory(total=memoryinfo[0], used=memoryinfo[1])
    memorydist = Memory()
    memorydist.setTotal(memoryinfo[0])
    memorydist.setUsed(memoryinfo[1])
    disklistinfo = diskinfo.split('@')

    disklistdist = []

    for sdisk in disklistinfo :
        sdiskinfo = sdisk.split(' ')
        disklistdist.append(Disk(' '.join(sdiskinfo[:-1]), sdiskinfo[-1]))

    print cpudist,memorydist,disklistdist
    return cpudist, memorydist, disklistdist