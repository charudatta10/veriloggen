from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *


def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    count = m.Reg('count', 32)

    m.Always(Posedge(clk))(
        If(rst)(
            count(0)
        ).Else(
            If(count == 1023)(
                count(0)
            ).Else(
                count(count + 1)
            )
        ))

    m.Always(Posedge(clk))(
        If(rst)(
            led(0)
        ).Else(
            If(count == 1023)(
                led(led + 1)
            )
        ))

    return m


def mkTop():
    m = Module('top')
    led = mkLed()
    params = m.copy_params(led)
    ports = m.copy_ports(led)

    m.Instance(led, 'inst_blinkled',
               m.connect_params(led), m.connect_ports(led))

    return m


if __name__ == '__main__':
    top = mkTop()
    verilog = top.to_verilog()
    print(verilog)
