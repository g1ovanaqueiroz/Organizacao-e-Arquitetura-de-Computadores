// Questao 1
always_comb begin
  if (SWI[6] && SWI[7] && SWI[5]) begin // b
    LED[2] <= 1;
  end else if (SWI[4] && SWI[5]) begin // a
    LED[2] <= 1;
  end else  // O EXPEDIENTE AINDA NAO ACABOU
    LED[2] <= 0;
  end
end

//Questao 2
SEG[0] <= (SWI[0] & (!SWI[1] | SWI[2]);

// Questao 3
SEG[7] <= (!SWI[3] & SWI[4]); // ERRO
LED[6] <= (!SWI[3] & !SWI[4]); // AQUECEDOR
LED[7] <= (SWI[3] & SWI[4]); // RESFRIADOR

// Questao 4
LED[0] <= (!SWI[0]); // LAVATORIO FEMININO LIVRE
LED[1] <= (!SWI[1] | !SWI[2]); // LAVATORIO MASCULINO LIVRE