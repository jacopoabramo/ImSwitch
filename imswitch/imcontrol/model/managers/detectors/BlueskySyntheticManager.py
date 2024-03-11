from bluesky.protocols import Readable, Triggerable, WritesExternalAssets

class BlueskySyntheticManager(Device):

    def __init__(self, prefix="ImSwitch", *, name):
        super().__init__(prefix, name=name, kind=Kind.normal)
    
    def trigger(self):
        return super().trigger()
    
    def describe(self):
        return super().describe()