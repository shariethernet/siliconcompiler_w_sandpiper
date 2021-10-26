# Default constraints file that sets up clocks based on definitions in schema.

source sc_manifest.tcl

set sc_clocks [dict keys [dict get $sc_cfg clock]]

foreach clock $sc_clocks {
    set pin [dict get $sc_cfg clock $clock pin]
    set period [dict get $sc_cfg clock $clock period]

    create_clock [get_ports $pin] -name $clock  -period $period
}
