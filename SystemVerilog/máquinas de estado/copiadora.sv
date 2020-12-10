logic reset, ligar, quantidade, falta, fora, tampa;
enum logic[2:0] {INERTE, COPIANDO, ENTUPIDA, FALTA_PAPEL} state; // Estados possíveis da copiadora
logic[1:0] contador_copias;
logic copiar, faltou, entupiu;

always_comb begin
  reset <= SWI[7];
  ligar <= SWI[0];
  quantidade <= SWI[2:1];
  falta <= SWI[4];
  fora <= SWI[5];
  tampa <= SWI[6];
end

always_comb begin
  contador_copias <= 0;
  copiar <= 0;
  faltou <= 0;
  entupiu <= 0;
end

always_ff @(posedge clk_2 or posedge reset) begin
  // Quando acionado o reset, a copiadora fica inerte e com número 0 de cópias.
  if (reset) begin
    state = INERTE;
    contador_copias = 0;
    copiar = 0;
    faltou = 0;
    entupiu = 0;
  end
  else begin
    unique case(state)
    // Se é pedido para ligar e a quantidade é maior que 0, a copiadora passa para o estado COPIANDO.
      INERTE: begin
        if (ligar && quantidade > 0) begin
          contador_copias = quantidade;
          state = COPIANDO;
        end
      end
      // Execução do estado COPIANDO.
      COPIANDO: begin
        if (contador_copias > 0) begin
          copiar = 1;
          if (falta) begin // em caso de faltar papel
            copiar = 0;
            state = FALTA_PAPEL;
          end
          else if (fora) begin // se tem papel atolado na copiadora
            copiar = 0;
            state = ENTUPIDA;
          end
          else if (!tampa) contador_copias = contador_copias - 1; // caso esteja apta à copiar
        end
        else begin
          copiar = 0;
          state = INERTE;
        end
      end
      // Execução do estado ENTUPIDO.
      ENTUPIDA: begin
        if (tampa && !fora) begin // Caso não esteja mais entupida, volta a copiar.
          entupiu = 0;
          state = COPIANDO;
        end
      end
      // Execução do estado FALTA_PAPEL.
      FALTA_PAPEL: begin
        if (!falta) begin // Caso haja papel (não falte), volta a copiar.
          copiar = 1;
          faltou = 0;
          state = COPIANDO;
        end
      end
    endcase
  end
end

// Saídas
always_comb begin
  LED[0] <= copiar; // copiando
  LED[1] <= faltou; // falta
  LED[2] <= entupiu; // entupida
  LED[7] <= clk_2; // clock
end