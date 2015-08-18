import led

expected_verilog = """
module top #
  (
   parameter WIDTH = 8
  )
  (
   input CLK, 
   input RST, 
   output [WIDTH-1:0] LED
  );
  blinkled #
  (
   WIDTH
  )
  inst_blinkled
  (
   CLK,
   RST,
   LED
  );
endmodule

module blinkled #
  ( 
   parameter WIDTH = 8,
   parameter NUM_INST = 4
  )
  ( 
   input CLK, 
   input RST,
   output reg [(WIDTH-1)+1-1:0] LED
  );

  reg [(32-1)+1-1:0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      if(count == 1023) begin
        count <= 0;
      end else begin
        count <= count + 1;
      end
    end
  end

  genvar i;
  generate for(i=0; i<NUM_INST; i=i+1) begin: gen_for
    reg [(32-1)+1-1:0] gen_count;
    if(i == 0) begin: gen_if_true
      always @(posedge CLK) begin
        gen_count <= count;
      end
    end else begin: gen_if_false
      reg [(32-1)+1-1:0] gen_if_count;
      always @(posedge CLK) begin
        gen_count <= gen_for[i-1].gen_count;
        gen_if_count <= gen_count;
      end
    end
  end endgenerate

  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      if(gen_for[NUM_INST-1].gen_if_false.gen_if_count == 1023) begin
        LED <= LED + 1;
      end 
    end
  end
endmodule
"""

def test_led():
    top_module = led.mkTop()
    top_code = top_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(top_code == expected_code)