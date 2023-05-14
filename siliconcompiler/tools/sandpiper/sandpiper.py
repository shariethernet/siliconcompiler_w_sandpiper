
'''
Bluespec is a high-level hardware description language. It has a variety of
advanced features including a powerful type system that can prevent errors
prior to synthesis time, and its most distinguishing feature, Guarded Atomic
Actions, allow you to define hardware components in a modular manner based
on their invariants, and let the compiler pick a scheduler.

Documentation: https://github.com/B-Lang-org/bsc#documentation

Sources: https://github.com/B-Lang-org/bsc

Installation: https://github.com/B-Lang-org/bsc#download
'''

from siliconcompiler.tools.sandpiper import convert


####################################################################
# Make Docs
####################################################################
def make_docs(chip):
    convert.setup(chip)
    return chip


# Directory inside step/index dir to store bsc intermediate results.
VLOG_DIR = 'verilog'


################################
# Setup Tool (pre executable)
################################
def parse_version(stdout):
    # Examples:
    # Bluespec Compiler, version 2021.12.1-27-g9a7d5e05 (build 9a7d5e05)
    # Bluespec Compiler, version 2021.07 (build 4cac6eba)
    pass
    #long_version = stdout.split()[3]
    #return long_version.split('-')[0]


################################
#  Custom runtime options
################################
def runtime_options(chip):
    step = chip.get('arg', 'step')
    index = chip.get('arg', 'index')

    cmdlist = []

    design = chip.top()
    sources = chip.find_files('input', 'hll', 'tlv', step=step, index=index)
    print("sources ",sources)
    if len(sources) != 1:
        raise ValueError('Sandpiper-saas only supports one source file!')
    cmdlist.append('-i '+sources[0])
    cmdlist.append(f'-o {design}.sv')
    cmdlist.append('--bestsv')
    cmdlist.append(f'--outdir {VLOG_DIR}')
    cmdlist.append('--inlineGen')
    cmdlist.append('--noline')
    cmdlist.append(f'--default_includes')
    
    #bsc_path = ':'.join(chip.find_files('option', 'ydir') + ['%/Libraries'])
    #cmdlist.append('-p ' + bsc_path)

    #for value in chip.find_files('option', 'idir'):
    #    cmdlist.append('-I ' + value)
    #for value in chip.get('option', 'define'):
    #    cmdlist.append('-D ' + value)



    return cmdlist
