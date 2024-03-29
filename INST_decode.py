import numpy as np
while(True):
    inst32 = input(np.array('\n\n\nInter your INST: '))

    if inst32[4:6] == '00':
        print('\nData Inst\n')
        print('Cond: ', inst32[0:4])
        print('Op: ', inst32[4:6])
        print('I: ', inst32[6])
        print('cmd: ', inst32[7:11])
        print('S: ', inst32[11])
        print('Rn: ', inst32[12:16])
        print('Rd: ', inst32[16:20])
        print('Src2: ', inst32[20:33])
    elif inst32[4:6] == '01':
        print('\nMemory Inst\n')
        print('Cond: ', inst32[0:4])
        print('Op: ', inst32[4:6])
        print('I: ', inst32[6])
        print('P: ', inst32[7])
        print('U: ', inst32[8])
        print('B: ', inst32[9])
        print('W: ', inst32[10])
        print('L: ', inst32[11])
        print('Rn: ', inst32[12:16])
        print('Rd: ', inst32[16:20])
        print('Src2: ', inst32[20:32])
    elif inst32[4:6] == '10':
        print('\nBranch Inst\n')
        print('Cond: ', inst32[0:4])
        print('Op: ', inst32[4:6])
        print('L: ', inst32[7])
        print('imm24: ', inst32[8:32])
    else:
        print('BaNaNa!')
    
