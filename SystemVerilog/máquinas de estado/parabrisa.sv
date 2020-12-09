logic reset;
enum logic[2:0] {DESLIGADO,ET1,ET2,ET3,LIGADO_BAIXO,LIGADO_ALTO} state; // ET = Estado intermediário
logic[5:0] chuva; // gotas de chuva
logic[1:0] parabrisa;
logic clk_1;
always_ff @(posedge clk_2) clk_1 = ~clk_1;
always_comb begin
    reset <= SWI[6];
    chuva <= SWI[5:0]; // Gotas de chuva
end

always_comb begin
    LED[1:0] <= parabrisa;
    SEG[7] <= clk_1;
end

always_ff @(posedge clk_1) begin
    if(reset) begin
        state <= DESLIGADO;
        parabrisa <= 0;
    end
    else begin
        unique case(state)
            DESLIGADO : begin 
            if((chuva[0]+chuva[1]+chuva[2]+chuva[3]+chuva[4]+chuva[5]) == 3) begin
                state <= ET1;

            end
            else if((chuva[0]+chuva[1]+chuva[2]+chuva[3]+chuva[4]+chuva[5]) == 5) begin
                state <= ET3;
            end
            end
            ET1: begin
                if((chuva[0]+chuva[1]+chuva[2]+chuva[3]+chuva[4]+chuva[5]) == 3) begin
                state <= ET2;
            end
            else if((chuva[0]+chuva[1]+chuva[2]+chuva[3]+chuva[4]+chuva[5]) == 5) begin
                state <= ET3;
            end
            end
            ET2: begin
                if((chuva[0]+chuva[1]+chuva[2]+chuva[3]+chuva[4]+chuva[5]) >= 3) begin
                state <= LIGADO_BAIXO;
                parabrisa <= 1;
            end
                else if((chuva[0]+chuva[1]+chuva[2]+chuva[3]+chuva[4]+chuva[5]) == 5) begin
                state <= ET3;
            end
            end
            LIGADO_BAIXO:
                if((chuva[0]+chuva[1]+chuva[2]+chuva[3]+chuva[4]+chuva[5]) < 2) begin
               		state <= DESLIGADO;
                	parabrisa <= 0;
            	end
		else if ((chuva[0]+chuva[1]+chuva[2]+chuva[3]+chuva[4]+chuva[5]) == 5) begin
			state <= ET3;
		end
            ET3: begin
                if((chuva[0]+chuva[1]+chuva[2]+chuva[3]+chuva[4]+chuva[5]) == 5) begin
                state <= LIGADO_ALTO;
                parabrisa <= 2;
            end
            end
            LIGADO_ALTO: begin
                if((chuva[0]+chuva[1]+chuva[2]+chuva[3]+chuva[4]+chuva[5]) < 4) begin
                state <= LIGADO_BAIXO;
                parabrisa <= 1;
            end
            end
        endcase
    end
end