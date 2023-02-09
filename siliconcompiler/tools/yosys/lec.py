import re

from siliconcompiler.tools.yosys.yosys import setup as setup_tool
from siliconcompiler.tools.yosys.yosys import setup_asic, setup_fpga

def setup(chip):
    ''' Helper method for configuring LEC steps.
    '''

    # Generic tool setup.
    setup_tool(chip)

    # Generic ASIC / FPGA mode setup.
    mode = chip.get('option', 'mode')
    if mode == 'asic':
        setup_asic(chip)
    elif mode == 'fpga':
        setup_fpga(chip)

    tool = 'yosys'
    task = 'lec'
    step = chip.get('arg','step')
    index = chip.get('arg','index')
    design = chip.top()

    # Set yosys script path.
    chip.set('tool', tool, 'task', task, 'script', 'sc_lec.tcl', step=step, index=index, clobber=False)

    # Input/output requirements.
    if (not chip.valid('input', 'netlist', 'verilog') or
        not chip.get('input', 'netlist', 'verilog')):
        chip.set('tool', tool, 'task', task, 'input', design + '.vg', step=step, index=index)
    #if not chip.get('input', 'rtl', 'verilog'):
        # TODO: Not sure this logic makes sense? Seems like reverse of tcl
        #chip.set('tool', tool, 'task', task, 'input', design + '.v', step=step, index=index)

##################################################
def post_process(chip):
    ''' Tool specific function to run after step execution
    '''

    tool = 'yosys'
    step = chip.get('arg','step')
    index = chip.get('arg','index')

    with open(step + ".log") as f:
        for line in f:
            if line.endswith('Equivalence successfully proven!\n'):
                chip.set('metric', 'drvs', 0, step=step, index=index)
                continue

            errors = re.search(r'Found a total of (\d+) unproven \$equiv cells.', line)
            if errors is not None:
                num_errors = int(errors.group(1))
                chip.set('metric', 'drvs', num_errors, step=step, index=index)
