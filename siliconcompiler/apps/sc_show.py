# Copyright 2020 Silicon Compiler Authors. All Rights Reserved.
import sys
import os
import siliconcompiler

def main():
    progname = "sc-show"
    description = """
    --------------------------------------------------------------
    Restricted SC app that displays the layout of a design
    based on a file provided or tries to display the final
    layout based on loading the json manifest from:
    build/<design>/job0/import/0/outputs/<design>.pkg.json

    Examples:

    sc-show -design adder
    (displays build/job0/adder/export/0/outputs/adder.gds)

    sc-show build/job0/adder/route/1/outputs/adder.def
    (displays build/job0/adder/route/1/outputs/adder.def)

    """


    # TODO: this is a hack to get around design name requirement: since legal
    # design names probably can't contain spaces, we can detect if it is unset.
    UNSET_DESIGN = '  unset  '

    # Create a base chip class.
    chip = siliconcompiler.Chip(UNSET_DESIGN)

    input_map = {
        'def': 'def',
        'gds': 'gds',
    }
    chip.create_cmdline(progname,
                        switchlist=['-design', '-input', '-loglevel', '-cfg'],
                        description=description,
                        input_map=input_map)

    #Error checking
    design = chip.get('design') != UNSET_DESIGN
    gds_mode = chip.valid('input', 'gds') and bool(chip.get('input', 'gds'))
    def_mode = chip.valid('input', 'def') and bool(chip.get('input', 'def'))

    if def_mode and gds_mode:
        chip.logger.error('Exclusive options -input_gds and -input_def cannot both be defined.')
        sys.exit(1)
    if not (design or def_mode or gds_mode):
        chip.logger.error('Nothing to load: please define a target with -cfg, -design, -input_def, and/or -input_gds.')
        sys.exit(1)

    if gds_mode:
        filename = chip.get('input', 'gds')[-1]
    elif def_mode:
        filename = chip.get('input', 'def')[-1]
    else:
        design = chip.get('design')
        dirlist =[chip.cwd,
                  'build',
                  chip.get('design'),
                  'job0',
                  'import',
                  '0',
                  'outputs',
                  design + '.pkg.json']
        manifest = os.path.join(*dirlist)
        chip.read_manifest(manifest)
        filename = chip.find_result('gds', step='export')
        if filename is None:
            chip.logger.error('No final GDS export found for design')
            sys.exit(1)

    if not chip.get('option', 'cfg'):
        # only autoload manifest if user doesn't supply manually
        design = os.path.splitext(os.path.basename(filename))[0]
        dirname = os.path.dirname(filename)
        manifest = os.path.join(*[dirname, design+'.pkg.json'])
        if not os.path.isfile(manifest):
            chip.logger.error(f'Unable to automatically find manifest for design {design}. '
                'Please provide a manifest explicitly using -cfg.')
            sys.exit(1)
        chip.read_manifest(manifest)

    # Read in file
    chip.logger.info(f"Displaying {filename}")

    success = chip.show(filename)

    return 0 if success else 1

#########################
if __name__ == "__main__":
    sys.exit(main())
