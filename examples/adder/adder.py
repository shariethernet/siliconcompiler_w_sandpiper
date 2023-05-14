import siliconcompiler


def main():
    chip = siliconcompiler.Chip('adder')
    chip.input('adder.tlv')
    chip.input('adder.sdc')
    chip.set('option', 'frontend', 'tlv')
    # default TLV clock pin is 'clk'
    #chip.clock(pin='clk', period=5)
    
    # Add additional options to sandpiper-saas like this
    #chip.set('tool','sandpiper','task','convert','option','--clkAlways')
    #chip.add('tool','sandpiper','task','convert','option',' --debugSigs')
    #chip.load_target("freepdk45_demo")
    chip.load_target("skywater130_demo")
    chip.write_flowgraph("test.png")
    chip.run()
    chip.summary()
    chip.show()


if __name__ == '__main__':
    main()
