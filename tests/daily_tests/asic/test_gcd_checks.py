import os
import siliconcompiler
from tests.fixtures import test_wrapper

##################################
def test_gcd_checks():
    '''Test EDA flow with LVS and DRC
    '''

    # Create instance of Chip class
    chip = siliconcompiler.Chip(loglevel='NOTSET')

    gcd_ex_dir = os.path.abspath(__file__)
    gcd_ex_dir = gcd_ex_dir[:gcd_ex_dir.rfind('/tests/daily_tests/asic')] + '/examples/gcd/'

    # Inserting value into configuration
    chip.add('source', gcd_ex_dir + 'gcd.v')
    chip.add('design', 'gcd')
    chip.add('clock', 'clock_name', 'pin', 'clk')
    chip.add('constraint', gcd_ex_dir + 'gcd.sdc')
    chip.set('target', 'skywater130_asicflow')
    chip.set('asic', 'diesize', '0 0 200.56 201.28')
    chip.set('asic', 'coresize', '20.24 21.76 180.32 184.96')
    chip.set_jobid()

    chip.target()

    chip.set('quiet', 'true')

    # Run the chip's build process synchronously.
    chip.run()

    # Verify that GDS and SVG files were generated.
    assert os.path.isfile('build/gcd/job1/export/outputs/gcd.gds')

    # Verify that the build was LVS and DRC clean.
    assert chip.get('metric', 'lvs', 'real', 'errors') == 0
    assert chip.get('metric', 'drc', 'real', 'errors') == 0