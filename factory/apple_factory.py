# -*-coding:utf-8-*-
'''
Created on 2017年7月18日

@author: houguangdong
'''
MINI14 = '1.4GHz MAc mini'

class AppleFactory:
    class MacMin14:
        def __init__(self):
            self.memory = 4 # 单位为GB
            self.hdd = 500  # 单位为GB
            self.gpu = 'Intel HD Graphics 5000'
        
        def __str__(self):
            info = (
                'Model {}'.format(MINI14),
                'Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu)
            )
            return '\n'.join(info)
        
    def build_computer(self, model):
        if (model == MINI14):
            return self.MacMin14()
        else:
            print "I don't know how to build{}".format((model))
            

class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None  # 单位为GB
        self.hdd = None     # 单位为GB
        self.gpu = None

    def __str__(self):
        info = (
            'Memory: {}GB'.format(self.memory),
            'Hard Disk: {}GB'.format(self.hdd),
            'Graphics Card: {}'.format(self.gpu)
        )
        return '\n'.join(info)
    

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')
        
    def configure_memory(self, amount):
        print 'run one time', amount
        self.computer.memory = amount
        
    def configure_hdd(self, amount):
        self.computer.hdd = amount
    
    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model
    

class HardwareEngineer:
    def __init__(self):
        self.builder = None
    
    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory), self.builder.configure_hdd(hdd), self.builder.configure_gpu(gpu))]
    
    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
    computer = engineer.computer
    print computer

    
if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print mac_mini
    main()
    