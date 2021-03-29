 | param                                         | desription                     | type            | required   | default   |
 | :----                                         | :----                          | :----           | :----      | :----     |
 | 'flow' step 'exe' <str>                       | Executable Name                | str             | all        |           |
 | 'flow' step 'version' <str>                   | Executable Version             | str             | all        |           |
 | 'flow' step 'option' <str>                    | Executable Options             | str             | optional   |           |
 | 'flow' step 'refdir' <file>                   | Reference Directory            | file            | optional   |           |
 | 'flow' step 'script' <file>                   | Entry Point script             | file            | optional   |           |
 | 'flow' step 'copy' <bool>                     | Copy Local Option              | bool            | optional   |           |
 | 'flow' step 'format' <str>                    | Script Format                  | str             | all        |           |
 | 'flow' step 'jobid' <num>                     | Job Index                      | num             | all        | 0         |
 | 'flow' step 'threads' <num>                   | Job Parallelism                | num             | all        |           |
 | 'flow' step 'cache' <file>                    | Cache Directory Name           | file            | optional   |           |
 | 'flow' step 'warningoff' <file>               | Warning Filter                 | str             | optional   |           |
 | 'flow' step 'keymap' <str str>                | Script Keymap                  | str str         | optional   |           |
 | 'flow' step 'vendor' <str>                    | Step Vendor                    | str             | all        |           |
 | 'flow' step 'custom' <str str>                | Custom EDA Parameters          | str str         | optional   |           |
 | 'flow' step 'signature' <str>                 | Step Signature                 | str             | optional   |           |
 | 'flow' step 'date' <str>                      | Step Date                      | str             | all        |           |
 | 'flow' step 'author' <str>                    | Step Author                    | str             | all        |           |
 | 'goal' step 'area' <num>                      | Cell Area Goal                 | num             | optional   |           |
 | 'goal' step 'power' <num>                     | Active Power Goal              | num             | optional   |           |
 | 'goal' step 'leakage' <num>                   | Leakage Goal                   | num             | optional   |           |
 | 'goal' step 'hold_tns' <num>                  | Hold TNS Goal                  | num             | optional   |           |
 | 'goal' step 'hold_wns' <num>                  | Hold WNS Goal                  | num             | optional   |           |
 | 'goal' step 'setup_tns' <num>                 | Setup TNS Goal                 | num             | optional   |           |
 | 'goal' step 'setup_wns' <num>                 | Setup WNS Goal                 | num             | optional   |           |
 | 'goal' step 'drv' <num>                       | Design Rule Violations Goal    | num             | optional   |           |
 | 'goal' step 'warnings' <num>                  | Total Warnings Goal            | num             | optional   |           |
 | 'goal' step 'errors' <num>                    | Total Errors Goal              | num             | optional   |           |
 | 'goal' step 'runtime' <num>                   | Total Runtime Goal             | num             | optional   |           |
 | 'goal' step 'memory' <num>                    | Total Memory Goal              | num             | optional   |           |
 | 'real' step 'area' <num>                      | Cell Area Real                 | num             | optional   |           |
 | 'real' step 'power' <num>                     | Active Power Real              | num             | optional   |           |
 | 'real' step 'leakage' <num>                   | Leakage Real                   | num             | optional   |           |
 | 'real' step 'hold_tns' <num>                  | Hold TNS Real                  | num             | optional   |           |
 | 'real' step 'hold_wns' <num>                  | Hold WNS Real                  | num             | optional   |           |
 | 'real' step 'setup_tns' <num>                 | Setup TNS Real                 | num             | optional   |           |
 | 'real' step 'setup_wns' <num>                 | Setup WNS Real                 | num             | optional   |           |
 | 'real' step 'drv' <num>                       | Design Rule Violations Real    | num             | optional   |           |
 | 'real' step 'warnings' <num>                  | Total Warnings Real            | num             | optional   |           |
 | 'real' step 'errors' <num>                    | Total Errors Real              | num             | optional   |           |
 | 'real' step 'runtime' <num>                   | Total Runtime Real             | num             | optional   |           |
 | 'real' step 'memory' <num>                    | Total Memory Real              | num             | optional   |           |
 | 'fpga' 'xml' <file>                           | FPGA Architecture File         | file            | fpga       |           |
 | 'fpga' 'vendor' <str>                         | FPGA Vendor Name               | str             | !fpga_xml  |           |
 | 'fpga' 'device' <str>                         | FPGA Device Name               | str             | !fpga_xml  |           |
 | 'pdk' 'foundry' <str>                         | Foundry Name                   | str             | asic       |           |
 | 'pdk' 'process' <str>                         | Process Name                   | str             | asic       |           |
 | 'pdk' 'node' <num>                            | Process Node                   | num             | asic       |           |
 | 'pdk' 'rev' <str>                             | Process Revision               | str             | asic       |           |
 | 'pdk' 'drm' <file>                            | PDK Design Rule Manual         | file            | asic       |           |
 | 'pdk' 'doc' <file>                            | PDK Documents                  | file            | asic       |           |
 | 'pdk' 'stackup' <str>                         | Process Metal Stackups         | str             | asic       |           |
 | 'pdk' 'devicemodel' stackup type tool <file>  | Device Models                  | file            | asic       |           |
 | 'pdk' 'pexmodel' stackup corner tool <file>   | Parasitic TCAD Models          | file            | asic       |           |
 | 'pdk' 'layermap' stackup src dst <file>       | Mask Layer Maps                | file            | asic       |           |
 | 'pdk' 'display' stackup tool <file>           | Display Configurations         | file            | asic       |           |
 | 'pdk' 'plib' stackup format <file>            | Primitive Libraries            | file            | asic       |           |
 | 'pdk' 'aprtech' stackup libtype vendor <file> | APR Technology File            | file            | asic       |           |
 | 'pdk' 'aprlayer' stackup <str str num num>    | APR Layer Definitions          | str str num num | optional   |           |
 | 'pdk' 'tapmax' <num>                          | Tap Cell Max Distance Rule     | num             | apr        |           |
 | 'pdk' 'tapoffset' <num>                       | Tap Cell Offset Rule           | num             | apr        |           |
 | 'asic' 'targetlib' <str>                      | Target Libraries               | str             | asic       |           |
 | 'asic' 'macrolib' <str>                       | Macro Libraries                | str             | optional   |           |
 | 'asic' 'delaymodel' <str>                     | Library Delay Model            | str             | asic       |           |
 | 'asic' 'ndr' <str>                            | Non-default Routing            | file            |            |           |
 | 'asic' 'minlayer' <str>                       | Minimum routing layer          | str             | asic       |           |
 | 'asic' 'maxlayer' <str>                       | Maximum Routing Layer          | str             | asic       |           |
 | 'asic' 'maxfanout' <str>                      | Maximum Fanout                 | num             | asic       | 64        |
 | 'asic' 'stackup' <str>                        | Metal Stackup                  | str             | asic       |           |
 | 'asic' 'density' <num>                        | Target Core Density            | num             | !diesize   |           |
 | 'asic' 'coremargin' <num>                     | Block Core Margin              | num             | density    |           |
 | 'asic' 'aspectratio' <num>                    | APR Block Aspect Ratio         | num             | density    | 1         |
 | 'asic' 'diesize' <num num num num>            | Target Die Size                | num num num num | !density   |           |
 | 'asic' 'coresize' <num num num num>           | Target Core Size               | num num num num | diesize    |           |
 | 'asic' 'floorplan' <file>                     | Floorplanning Script           | file            | optional   |           |
 | 'stdcell' libname corner 'opcond' <str>       | Stdcell Operating Condition    | str             | asic       |           |
 | 'stdcell' libname corner 'check' <str>        | Stdcell Corner Checks          | str             | asic       |           |
 | 'stdcell' libname corner 'nldm' type <file>   | Stdcell NLDM Timing Model      | file            | asic       |           |
 | 'stdcell' libname corner 'ccs' type <file>    | Stdcell CCS Timing Model       | file            | optional   |           |
 | 'stdcell' libname corner 'aocv' <file>        | Stdcell AOCV Timing Model      | file            | optional   |           |
 | 'stdcell' libname corner 'apl' type <file>    | Stdcell APL Power Model        | file            | optional   |           |
 | 'stdcell' libname 'lef' <file>                | Stdcell LEF                    | file            | asic       |           |
 | 'stdcell' libname 'gds' <file>                | Stdcell GDS                    | file            | optional   |           |
 | 'stdcell' libname 'cdl' <file>                | Stdcell CDL Netlist            | file            | optional   |           |
 | 'stdcell' libname 'spice' <file>              | Stdcell Spice Netlist          | file            | optional   |           |
 | 'stdcell' libname 'hdl' <file>                | Stdcell HDL Model              | file            | asic       |           |
 | 'stdcell' libname 'atpg' <file>               | Stdcell ATPG Model             | file            | optional   |           |
 | 'stdcell' libname 'pgmetal' <str>             | Stdcell Power/Ground Layer     | str             | optional   |           |
 | 'stdcell' libname 'tag' <str>                 | Stdcell Identifier Tags        | str             | optional   |           |
 | 'stdcell' libname 'driver' <str>              | Stdcell Default Driver Cell    | str             | asic       |           |
 | 'stdcell' libname 'site' <str>                | Stdcell Site/Tile Name         | str             | optional   |           |
 | 'stdcell' libname 'cells' celltype <str>      | Stdcell Cell Lists             | str             | optional   |           |
 | 'stdcell' libname 'laydb' type <file>         | Stdcell Layout Database        | file            | optional   |           |
 | 'macro' libname corner 'opcond' <str>         | Macro Operating Condition      | str             | asic       |           |
 | 'macro' libname corner 'check' <str>          | Macro Corner Checks            | str             | asic       |           |
 | 'macro' libname corner 'nldm' type <file>     | Macro NLDM Timing Model        | file            | asic       |           |
 | 'macro' libname corner 'ccs' type <file>      | Macro CCS Timing Model         | file            | optional   |           |
 | 'macro' libname corner 'aocv' <file>          | Macro AOCV Timing Model        | file            | optional   |           |
 | 'macro' libname corner 'apl' type <file>      | Macro APL Power Model          | file            | optional   |           |
 | 'macro' libname 'lef' <file>                  | Macro LEF                      | file            | asic       |           |
 | 'macro' libname 'gds' <file>                  | Macro GDS                      | file            | optional   |           |
 | 'macro' libname 'cdl' <file>                  | Macro CDL Netlist              | file            | optional   |           |
 | 'macro' libname 'spice' <file>                | Macro Spice Netlist            | file            | optional   |           |
 | 'macro' libname 'hdl' <file>                  | Macro HDL Model                | file            | asic       |           |
 | 'macro' libname 'atpg' <file>                 | Macro ATPG Model               | file            | optional   |           |
 | 'macro' libname 'pgmetal' <str>               | Macro Power/Ground Layer       | str             | optional   |           |
 | 'macro' libname 'tag' <str>                   | Macro Identifier Tags          | str             | optional   |           |
 | 'macro' libname 'driver' <str>                | Macro Default Driver Cell      | str             | asic       |           |
 | 'macro' libname 'site' <str>                  | Macro Site/Tile Name           | str             | optional   |           |
 | 'macro' libname 'cells' celltype <str>        | Macro Cell Lists               | str             | optional   |           |
 | 'macro' libname 'laydb' type <file>           | Macro Layout Database          | file            | optional   |           |
 | 'source' <file>                               | Design Source Files            | file            | all        |           |
 | 'doc' <file>                                  | Design Documentation           | file            | all        |           |
 | 'rev' <str>                                   | Design Revision                | str             | all        |           |
 | 'license' <file>                              | Design License File            | file            | all        |           |
 | 'design' <str>                                | Design Top Module Name         | str             | optional   |           |
 | 'nickname' <str>                              | Design Nickname                | str             | optional   |           |
 | 'origin' <str>                                | Design Origin                  | str             | optional   |           |
 | 'clock' <str str num num>                     | Design Clocks                  | str str num num | optional   |           |
 | 'supply' <str str num>                        | Design Power Supplies          | str str num     | optional   |           |
 | 'define' <str>                                | Verilog Preprocessor Symbols   | str             | optional   |           |
 | 'ydir' <dir>                                  | Verilog Module Search Paths    | dir             | optional   |           |
 | 'idir' <dir>                                  | Verilog Include Search Paths   | dir             | optional   |           |
 | 'vlib' <file>                                 | Verilog Library                | file            | optional   |           |
 | 'libext' <str>                                | Verilog File Extensions        | str             | optional   |           |
 | 'cmdfile' <file>                              | Verilog Options File           | file            | optional   |           |
 | 'constraint' <file>                           | Design Constraint Files        | file            | optional   |           |
 | 'vcd' <file>                                  | Value Change Dump File         | file            | optional   |           |
 | 'mcmm' scenario 'libcorner' <str>             | MCMM Library Corner Name       | str             | asic       |           |
 | 'mcmm' scenario 'opcond' <str>                | MCMM Operating Condition       | str             | asic       |           |
 | 'mcmm' scenario 'pexcorner' <str>             | MCMM PEX Corner Name           | str             | asic       |           |
 | 'mcmm' scenario 'mode' <str>                  | MCMM Mode Name                 | str             | asic       |           |
 | 'mcmm' scenario 'constraint' <str>            | MCMM Timing Constraints        | file            | asic       |           |
 | 'mcmm' scenario 'check' <str>                 | MCMM Checks                    | str             | asic       |           |
 | 'mode' <str>                                  | Compilation Mode               | str             | all        | asic      |
 | 'target' <str>                                | Target Platform                | str             | optional   |           |
 | 'cfg' <file>                                  | Configuration File             | file            | optional   |           |
 | 'env' <str str>                               | Environment Variables          | str str         | optional   |           |
 | 'scpath' <str>                                | Search path                    | file            | optional   |           |
 | 'lock' <bool>                                 | Configuration File Lock        | bool            | optional   | false     |
 | 'quiet' <bool>                                | Quiet execution                | bool            | optional   | false     |
 | 'debug' <str>                                 | Debug Level                    | str             | optional   | WARNING   |
 | 'dir' <dir>                                   | Build Directory                | dir             | optional   | build     |
 | 'start' <str>                                 | Compilation Start Step         | str             | optional   |           |
 | 'stop' <str>                                  | Compilation Stop Step          | str             | optional   |           |
 | 'skip' <str>                                  | Compilation Skip Steps         | str             | optional   |           |
 | 'msg_event' <str>                             | Message Event                  | str             | optional   |           |
 | 'msg_contact' <str>                           | Message Contact                | str             | optional   |           |
 | 'optmode' <str>                               | Optimization Mode              | str             | optional   | O0        |
 | 'relax' <bool>                                | Relaxed RTL Linting            | bool            | optional   | false     |
 | 'clean' <bool>                                | Keep essential files only      | bool            | optional   | false     |
 | 'flow_design' <str>                           | Compilation Flow               | str             | all        |           |
 | 'flow_signoff' <str>                          | Signoff Flow                   | str             | optional   |           |
 | 'flow_mfg' <str>                              | Manufacturing Steps            | str             | optional   |           |
 | 'remote' <str>                                | Remote Server Address          | str             | optional   |           |
 | 'remote' <str>                                | Remove Server Port             | num             | remote     | 8080      |