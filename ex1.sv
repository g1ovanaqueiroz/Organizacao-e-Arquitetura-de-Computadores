// Questao 1
always_comb begin
  if ( SWI[5] ) begin 
    if ( SWI[6] ) begin
      if ( SWI[7] ) begin
        LED[2] <= 1;
      end
    end else begin
      if ( SWI[4] ) begin
        LED[2] <= 1;
      end else begin
        LED[2] <= 0;
      end
    end
  end else begin
    LED[2] <= 0;
  end
end

//Questao 2
always_comb begin
  SEG[0] <= (SWI[0] & !SWI[1]) | (SWI[0] & SWI[2]);
end

// Questao 3
always_comb begin
  // ERRO (NAO HA COMO SE ESTAR ABAIXO DE 15 E ACIMA DE 20 AO MESMO TEMPO)
  SEG[7] <= (!SWI[3] & SWI[4]);
    // AQUECEDOR
  LED[6] <= (!SWI[3] & !SWI[4]);
  // RESFRIADOR
  LED[7] <= (SWI[3] & SWI[4]);
end 

// Questao 4
always_comb begin
  LED[0] <= (!SWI[0]); // LAVATORIO FEMININO LIVRE
  LED[1] <= (!SWI[1] | !SWI[2]); // LAVATORIO MASCULINO LIVRE
end