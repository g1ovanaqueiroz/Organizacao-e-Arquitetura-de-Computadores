always_comb begin
    // LED <= SWI | clk_2;
    SEG <= SWI;
    lcd_WriteData <= SWI;
    lcd_pc <= 'h12;
    lcd_instruction <= 'h34567890;
    lcd_SrcA <= 'hab;
    lcd_SrcB <= 'hcd;
    lcd_ALUResult <= 'hef;
    lcd_Result <= 'h11;
    lcd_ReadData <= 'h33;
    lcd_MemWrite <= SWI[0];
    lcd_Branch <= SWI[1];
    lcd_MemtoReg <= SWI[2];
    lcd_RegWrite <= SWI[3];
    for(int i=0; i<NREGS_TOP; i++) lcd_registrador[i] <= i+i*16;
    lcd_a <= {56'h1234567890ABCD, SWI};
    lcd_b <= {SWI, 56'hFEDCBA09876543};
  end

  logic reset, aumentar, diminuir, pingando;
  enum logic [1:0] {ESTAVEL, AUMENTANDO, DIMINUINDO} state; // estados possíveis do ar condicionado
  logic [2:0] REAL, DESEJO, PARAR_PINGOS;
  logic [1:0] CONTADOR;
  logic [3:0] CONTADOR_PINGOS;

  always_comb begin 
    reset <= SWI[7];
    aumentar <= SWI[1];
    diminuir <= SWI[0];
  end
    
  always_comb begin
    LED[7] <= clk_2;
    LED[6:4] <= REAL;
    LED[2:0] <= DESEJO;
    LED[3] <= pingando;
  end

  always_ff @(posedge clk_2 or posedge reset) begin
    if(reset) begin
      REAL <= 20; // Tanto REAL como DESEJO são colocadas como 20 no RESET
      DESEJO <= 20;
      pingando <= 0; // As demais vão para zero quando acionado o RESET
      CONTADOR <= 0;
      CONTADOR_PINGOS <= 0;
      PARAR_PINGOS <= 0;
      state <= ESTAVEL; // O estado é iniciado como estável
    end 

    else begin
      // O ar-condicionado começa a pingar 10 ciclos de clock após o reset.
      if(CONTADOR_PINGOS < 10) CONTADOR_PINGOS <= CONTADOR_PINGOS + 1;
      if(CONTADOR_PINGOS == 9) pingando <= 1;
    
      // Só se aumenta ou diminui a temperatura desejada se for possível (entre 20 e 27)
      if(aumentar && DESEJO < 27) DESEJO <= DESEJO + 1;
      if(diminuir && DESEJO > 20) DESEJO <= DESEJO - 1;
      // Os pingos param com a temperatura real em 27 graus Celsius por, pelo menos, 4 ciclos de clock.
      // Ou seja, se PARAR_PINGOS já está em 3, este já é o quarto ciclo.
      if(PARAR_PINGOS == 3) begin 
        pingando <= 0;
        CONTADOR_PINGOS <= 11;
      end

      unique case(state) 
        ESTAVEL: begin
            if(REAL == 27 && pingando) PARAR_PINGOS <= PARAR_PINGOS + 1;
            if(aumentar  && DESEJO < 27) begin
                PARAR_PINGOS <= 0;
                DESEJO <= DESEJO + 1;
                state <= AUMENTANDO;
            end else if(diminuir  && DESEJO > 20) begin
                PARAR_PINGOS <= 0;
                DESEJO <= DESEJO - 1;
                state <= DIMINUINDO;
            end
        end
        AUMENTANDO: begin   // Aumenta até real = desejo e estabiliza
            if(DESEJO == REAL) begin
                state <= ESTAVEL;
            end else begin
                CONTADOR <= CONTADOR + 1;

                if(CONTADOR == 1) begin
                    REAL <= REAL + 1;
                    CONTADOR <= 0;
                end
            end

        end
        DIMINUINDO: begin    // Diminui até real = desejo e estabiliza
            if(DESEJO == REAL) begin
                state <= ESTAVEL;
            end else begin
                CONTADOR <= CONTADOR + 1;

                if(CONTADOR == 1) begin
                    REAL <= REAL - 1;
                    CONTADOR <= 0;
                end
            end
        end
      endcase
    end
  end