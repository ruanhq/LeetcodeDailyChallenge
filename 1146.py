#1146. Snapshot array:
class SnapshotArray:
    def __init__(self, length: int):
        self.length = length
        self.listArray = {}
        self.snapCount = -1
        self.snapShot = {}

    def set(self, index, val):
        self.listArray[index] = val

    def snap(self):
        self.snapCount += 1
        self.snapShot[self.snapCount] = self.listArray.copy()
        return self.snapCount
    #get the snapshot at that index:
    def get(self, index, snap_id):
        if snap_id in self.snapShot:
            arrayToExtract = self.snapShot[snap_id]
            if index in arrayToExtract:
                return arrayToExtract[index]
        return 0

    def get(self, index, snap_id):
        if snap_id in self.snapShot:
            arrayToExtract = self.snapShot[snap_id]
            if index in arrayToExtract:
                return arrayToExtract[index]
        return 0



