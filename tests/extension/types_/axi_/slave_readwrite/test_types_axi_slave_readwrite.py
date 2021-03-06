from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_slave_readwrite

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] sum;
  reg [32-1:0] myaxi_awaddr;
  reg [8-1:0] myaxi_awlen;
  reg myaxi_awvalid;
  wire myaxi_awready;
  reg [32-1:0] myaxi_wdata;
  reg [4-1:0] myaxi_wstrb;
  reg myaxi_wlast;
  reg myaxi_wvalid;
  wire myaxi_wready;
  reg [32-1:0] myaxi_araddr;
  reg [8-1:0] myaxi_arlen;
  reg myaxi_arvalid;
  wire myaxi_arready;
  wire [32-1:0] myaxi_rdata;
  wire myaxi_rlast;
  wire myaxi_rvalid;
  reg myaxi_rready;
  reg [32-1:0] _axi_awaddr;
  reg [8-1:0] _axi_awlen;
  reg _axi_awvalid;
  wire _axi_awready;
  reg [32-1:0] _axi_wdata;
  reg [4-1:0] _axi_wstrb;
  reg _axi_wlast;
  reg _axi_wvalid;
  wire _axi_wready;
  reg [32-1:0] _axi_araddr;
  reg [8-1:0] _axi_arlen;
  reg _axi_arvalid;
  wire _axi_arready;
  wire [32-1:0] _axi_rdata;
  wire _axi_rlast;
  wire _axi_rvalid;
  wire _axi_rready;
  wire [32-1:0] _tmp_0;
  assign _tmp_0 = _axi_awaddr;

  always @(*) begin
    myaxi_awaddr = _tmp_0;
  end

  wire [8-1:0] _tmp_1;
  assign _tmp_1 = _axi_awlen;

  always @(*) begin
    myaxi_awlen = _tmp_1;
  end

  wire _tmp_2;
  assign _tmp_2 = _axi_awvalid;

  always @(*) begin
    myaxi_awvalid = _tmp_2;
  end

  assign _axi_awready = myaxi_awready;
  wire [32-1:0] _tmp_3;
  assign _tmp_3 = _axi_wdata;

  always @(*) begin
    myaxi_wdata = _tmp_3;
  end

  wire [4-1:0] _tmp_4;
  assign _tmp_4 = _axi_wstrb;

  always @(*) begin
    myaxi_wstrb = _tmp_4;
  end

  wire _tmp_5;
  assign _tmp_5 = _axi_wlast;

  always @(*) begin
    myaxi_wlast = _tmp_5;
  end

  wire _tmp_6;
  assign _tmp_6 = _axi_wvalid;

  always @(*) begin
    myaxi_wvalid = _tmp_6;
  end

  assign _axi_wready = myaxi_wready;
  wire [32-1:0] _tmp_7;
  assign _tmp_7 = _axi_araddr;

  always @(*) begin
    myaxi_araddr = _tmp_7;
  end

  wire [8-1:0] _tmp_8;
  assign _tmp_8 = _axi_arlen;

  always @(*) begin
    myaxi_arlen = _tmp_8;
  end

  wire _tmp_9;
  assign _tmp_9 = _axi_arvalid;

  always @(*) begin
    myaxi_arvalid = _tmp_9;
  end

  assign _axi_arready = myaxi_arready;
  assign _axi_rdata = myaxi_rdata;
  assign _axi_rlast = myaxi_rlast;
  assign _axi_rvalid = myaxi_rvalid;
  wire _tmp_10;
  assign _tmp_10 = _axi_rready;

  always @(*) begin
    myaxi_rready = _tmp_10;
  end

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] rsum;
  reg [9-1:0] _tmp_11;
  reg __axi_cond_0_1;
  reg [9-1:0] _tmp_12;
  reg __axi_cond_1_1;
  assign _axi_rready = (fsm == 1) || (fsm == 3);
  reg [9-1:0] _tmp_13;
  reg __axi_cond_2_1;
  reg [32-1:0] wdata;
  reg _tmp_14;
  reg __axi_cond_3_1;
  reg [9-1:0] _tmp_15;
  reg __axi_cond_4_1;
  reg _tmp_16;
  reg __axi_cond_5_1;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .sum(sum),
    .myaxi_awaddr(myaxi_awaddr),
    .myaxi_awlen(myaxi_awlen),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wlast(myaxi_wlast),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arlen(myaxi_arlen),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rlast(myaxi_rlast),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST, sum, myaxi_awaddr, myaxi_awlen, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wvalid, myaxi_wready, myaxi_araddr, myaxi_arlen, myaxi_arvalid, myaxi_arready, myaxi_rdata, myaxi_rlast, myaxi_rvalid, myaxi_rready, _axi_awaddr, _axi_awlen, _axi_awvalid, _axi_awready, _axi_wdata, _axi_wstrb, _axi_wlast, _axi_wvalid, _axi_wready, _axi_araddr, _axi_arlen, _axi_arvalid, _axi_arready, _axi_rdata, _axi_rlast, _axi_rvalid, _axi_rready, _tmp_0, _tmp_1, _tmp_2, _tmp_3, _tmp_4, _tmp_5, _tmp_6, _tmp_7, _tmp_8, _tmp_9, _tmp_10, fsm, rsum, _tmp_11, __axi_cond_0_1, _tmp_12, __axi_cond_1_1, _tmp_13, __axi_cond_2_1, wdata, _tmp_14, __axi_cond_3_1, _tmp_15, __axi_cond_4_1, _tmp_16, __axi_cond_5_1);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    _axi_awaddr = 0;
    _axi_awlen = 0;
    _axi_awvalid = 0;
    _axi_wdata = 0;
    _axi_wstrb = 0;
    _axi_wlast = 0;
    _axi_wvalid = 0;
    _axi_araddr = 0;
    _axi_arlen = 0;
    _axi_arvalid = 0;
    fsm = fsm_init;
    rsum = 0;
    _tmp_11 = 0;
    __axi_cond_0_1 = 0;
    _tmp_12 = 0;
    __axi_cond_1_1 = 0;
    _tmp_13 = 0;
    __axi_cond_2_1 = 0;
    wdata = 0;
    _tmp_14 = 0;
    __axi_cond_3_1 = 0;
    _tmp_15 = 0;
    __axi_cond_4_1 = 0;
    _tmp_16 = 0;
    __axi_cond_5_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_araddr <= 0;
      _axi_arlen <= 0;
      _axi_arvalid <= 0;
      _tmp_11 <= 0;
      __axi_cond_0_1 <= 0;
      _tmp_12 <= 0;
      __axi_cond_1_1 <= 0;
      _axi_awaddr <= 0;
      _axi_awlen <= 0;
      _axi_awvalid <= 0;
      _tmp_13 <= 0;
      __axi_cond_2_1 <= 0;
      _axi_wdata <= 0;
      _axi_wvalid <= 0;
      _axi_wlast <= 0;
      _axi_wstrb <= 0;
      _tmp_14 <= 0;
      __axi_cond_3_1 <= 0;
      _tmp_15 <= 0;
      __axi_cond_4_1 <= 0;
      _tmp_16 <= 0;
      __axi_cond_5_1 <= 0;
    end else begin
      if(__axi_cond_0_1) begin
        _axi_arvalid <= 0;
      end 
      if(__axi_cond_1_1) begin
        _axi_arvalid <= 0;
      end 
      if(__axi_cond_2_1) begin
        _axi_awvalid <= 0;
      end 
      if(__axi_cond_3_1) begin
        _axi_wvalid <= 0;
        _axi_wlast <= 0;
        _tmp_14 <= 0;
      end 
      if(__axi_cond_4_1) begin
        _axi_awvalid <= 0;
      end 
      if(__axi_cond_5_1) begin
        _axi_wvalid <= 0;
        _axi_wlast <= 0;
        _tmp_16 <= 0;
      end 
      if((fsm == 0) && ((_axi_arready || !_axi_arvalid) && (_tmp_11 == 0))) begin
        _axi_araddr <= 1024;
        _axi_arlen <= 63;
        _axi_arvalid <= 1;
        _tmp_11 <= 64;
      end 
      __axi_cond_0_1 <= 1;
      if(_axi_arvalid && !_axi_arready) begin
        _axi_arvalid <= _axi_arvalid;
      end 
      if(_axi_rready && _axi_rvalid && (_tmp_11 > 0)) begin
        _tmp_11 <= _tmp_11 - 1;
      end 
      if((fsm == 2) && ((_axi_arready || !_axi_arvalid) && (_tmp_12 == 0))) begin
        _axi_araddr <= 2048;
        _axi_arlen <= 127;
        _axi_arvalid <= 1;
        _tmp_12 <= 128;
      end 
      __axi_cond_1_1 <= 1;
      if(_axi_arvalid && !_axi_arready) begin
        _axi_arvalid <= _axi_arvalid;
      end 
      if(_axi_rready && _axi_rvalid && (_tmp_12 > 0)) begin
        _tmp_12 <= _tmp_12 - 1;
      end 
      if((fsm == 5) && ((_axi_awready || !_axi_awvalid) && (_tmp_13 == 0))) begin
        _axi_awaddr <= 1024;
        _axi_awlen <= 63;
        _axi_awvalid <= 1;
        _tmp_13 <= 64;
      end 
      if((fsm == 5) && ((_axi_awready || !_axi_awvalid) && (_tmp_13 == 0)) && 0) begin
        _axi_awvalid <= 0;
      end 
      __axi_cond_2_1 <= 1;
      if(_axi_awvalid && !_axi_awready) begin
        _axi_awvalid <= _axi_awvalid;
      end 
      if((fsm == 6) && ((_tmp_13 > 0) && (_axi_wready || !_axi_wvalid) && (_tmp_13 > 0))) begin
        _axi_wdata <= wdata;
        _axi_wvalid <= 1;
        _axi_wlast <= 0;
        _axi_wstrb <= { 4{ 1'd1 } };
        _tmp_13 <= _tmp_13 - 1;
      end 
      if((fsm == 6) && ((_tmp_13 > 0) && (_axi_wready || !_axi_wvalid) && (_tmp_13 > 0)) && (_tmp_13 == 1)) begin
        _axi_wlast <= 1;
        _tmp_14 <= 1;
      end 
      __axi_cond_3_1 <= 1;
      if(_axi_wvalid && !_axi_wready) begin
        _axi_wvalid <= _axi_wvalid;
        _axi_wlast <= _axi_wlast;
        _tmp_14 <= _tmp_14;
      end 
      if((fsm == 7) && ((_axi_awready || !_axi_awvalid) && (_tmp_15 == 0))) begin
        _axi_awaddr <= 1024;
        _axi_awlen <= 127;
        _axi_awvalid <= 1;
        _tmp_15 <= 128;
      end 
      if((fsm == 7) && ((_axi_awready || !_axi_awvalid) && (_tmp_15 == 0)) && 0) begin
        _axi_awvalid <= 0;
      end 
      __axi_cond_4_1 <= 1;
      if(_axi_awvalid && !_axi_awready) begin
        _axi_awvalid <= _axi_awvalid;
      end 
      if((fsm == 8) && ((_tmp_15 > 0) && (_axi_wready || !_axi_wvalid) && (_tmp_15 > 0))) begin
        _axi_wdata <= wdata;
        _axi_wvalid <= 1;
        _axi_wlast <= 0;
        _axi_wstrb <= { 4{ 1'd1 } };
        _tmp_15 <= _tmp_15 - 1;
      end 
      if((fsm == 8) && ((_tmp_15 > 0) && (_axi_wready || !_axi_wvalid) && (_tmp_15 > 0)) && (_tmp_15 == 1)) begin
        _axi_wlast <= 1;
        _tmp_16 <= 1;
      end 
      __axi_cond_5_1 <= 1;
      if(_axi_wvalid && !_axi_wready) begin
        _axi_wvalid <= _axi_wvalid;
        _axi_wlast <= _axi_wlast;
        _tmp_16 <= _tmp_16;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      rsum <= 0;
      wdata <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(_axi_arready || !_axi_arvalid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(_axi_rready && _axi_rvalid) begin
            rsum <= rsum + _axi_rdata;
          end 
          if(_axi_rready && _axi_rvalid && _axi_rlast) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(_axi_arready || !_axi_arvalid) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(_axi_rready && _axi_rvalid) begin
            rsum <= rsum + _axi_rdata;
          end 
          if(_axi_rready && _axi_rvalid && _axi_rlast) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          $display("rsum=%d expected_rsum=%d", rsum, 92064);
          fsm <= fsm_5;
        end
        fsm_5: begin
          if(_axi_awready || !_axi_awvalid) begin
            fsm <= fsm_6;
          end 
        end
        fsm_6: begin
          if((_tmp_13 > 0) && (_axi_wready || !_axi_wvalid)) begin
            wdata <= wdata + 1;
          end 
          if(_tmp_14) begin
            fsm <= fsm_7;
          end 
        end
        fsm_7: begin
          if(_axi_awready || !_axi_awvalid) begin
            fsm <= fsm_8;
          end 
        end
        fsm_8: begin
          if((_tmp_15 > 0) && (_axi_wready || !_axi_wvalid)) begin
            wdata <= wdata + 1;
          end 
          if(_tmp_16) begin
            fsm <= fsm_9;
          end 
        end
        fsm_9: begin
          $display("sum=%d expected_sum=%d", sum, 18336);
          fsm <= fsm_10;
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  output reg [32-1:0] sum,
  input [32-1:0] myaxi_awaddr,
  input [8-1:0] myaxi_awlen,
  input myaxi_awvalid,
  output myaxi_awready,
  input [32-1:0] myaxi_wdata,
  input [4-1:0] myaxi_wstrb,
  input myaxi_wlast,
  input myaxi_wvalid,
  output myaxi_wready,
  input [32-1:0] myaxi_araddr,
  input [8-1:0] myaxi_arlen,
  input myaxi_arvalid,
  output myaxi_arready,
  output reg [32-1:0] myaxi_rdata,
  output reg myaxi_rlast,
  output reg myaxi_rvalid,
  input myaxi_rready
);

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [9-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  reg _tmp_2;
  reg _tmp_3;
  reg _tmp_4;
  reg _tmp_5;
  assign myaxi_awready = (fsm == 0) && !_tmp_2 && !_tmp_3 && _tmp_4;
  assign myaxi_arready = (fsm == 0) && !_tmp_3 && !_tmp_2 && _tmp_5;
  reg [32-1:0] rdata;
  reg _tmp_6;
  reg _myaxi_cond_0_1;
  assign myaxi_wready = fsm == 100;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_4 <= 0;
      _tmp_5 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_1 <= 0;
      _tmp_0 <= 0;
      myaxi_rdata <= 0;
      myaxi_rvalid <= 0;
      myaxi_rlast <= 0;
      _tmp_6 <= 0;
      _myaxi_cond_0_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_rvalid <= 0;
        myaxi_rlast <= 0;
        _tmp_6 <= 0;
      end 
      _tmp_4 <= myaxi_awvalid;
      _tmp_5 <= myaxi_arvalid;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      if(myaxi_awready && myaxi_awvalid) begin
        _tmp_1 <= myaxi_awaddr;
        _tmp_0 <= myaxi_awlen + 1;
        _tmp_2 <= 1;
      end else if(myaxi_arready && myaxi_arvalid) begin
        _tmp_1 <= myaxi_araddr;
        _tmp_0 <= myaxi_arlen + 1;
        _tmp_3 <= 1;
      end 
      if((fsm == 1) && ((_tmp_0 > 0) && (myaxi_rready || !myaxi_rvalid) && (_tmp_0 > 0))) begin
        myaxi_rdata <= rdata;
        myaxi_rvalid <= 1;
        myaxi_rlast <= 0;
        _tmp_0 <= _tmp_0 - 1;
      end 
      if((fsm == 1) && ((_tmp_0 > 0) && (myaxi_rready || !myaxi_rvalid) && (_tmp_0 > 0)) && (_tmp_0 == 1)) begin
        myaxi_rlast <= 1;
        _tmp_6 <= 1;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_rvalid && !myaxi_rready) begin
        myaxi_rvalid <= myaxi_rvalid;
        myaxi_rlast <= myaxi_rlast;
        _tmp_6 <= _tmp_6;
      end 
      if(myaxi_wready && myaxi_wvalid && (_tmp_0 > 0)) begin
        _tmp_0 <= _tmp_0 - 1;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_100 = 100;
  localparam fsm_101 = 101;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      rdata <= 0;
      sum <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(_tmp_3) begin
            rdata <= _tmp_1 >> 2;
          end 
          if(_tmp_2) begin
            fsm <= fsm_100;
          end 
          if(_tmp_3) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if((_tmp_0 > 0) && (myaxi_rready || !myaxi_rvalid)) begin
            rdata <= rdata + 1;
          end 
          if(_tmp_6) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          fsm <= fsm_init;
        end
        fsm_100: begin
          if(myaxi_wready && myaxi_wvalid) begin
            sum <= sum + myaxi_wdata;
          end 
          if(myaxi_wready && myaxi_wvalid && myaxi_wlast) begin
            fsm <= fsm_101;
          end 
        end
        fsm_101: begin
          fsm <= fsm_init;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_slave_readwrite.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
