
from .openroad import setup as setup_tool
from .openroad import build_pex_corners, post_process

def setup(chip):
    ''' Helper method for configs specific to cts tasks.
    '''

    # Generic tool setup.
    setup_tool(chip)

    tool = 'openroad'
    task = 'cts'
    design = chip.top()
    step = chip.get('arg', 'step')
    index = chip.get('arg', 'index')

    chip.add('tool', tool, 'task', task, 'input', step, index, design +'.def')

def pre_process(chip):
    build_pex_corners(chip)