class Package:
    def __init__(self,
                 name='my name',
                 desc='description here',
                 version='1.0.0',
                 depends=[]
                 ):
        self.name = name
        self.desc = desc
        self.version = version
        self.depends = depends

    def __str__(self):
        return self.name + '==' + self.version

    def get_depends(self) -> str:
        return self.depends

    def get_desc(self) -> str:
        return self.desc

    def get_name(self) -> str:
        return self.name + '==' + self.version


