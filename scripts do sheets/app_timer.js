function criarGatilhoBuscarArquivo() {
    // Remove quaisquer gatilhos existentes para evitar duplicações
    removerGatilhosExistentes();
  
    // Cria um novo gatilho que executa a função 'buscarArquivo' a cada 5 minutos
    ScriptApp.newTrigger("buscarArquivo")
      .timeBased()
      .everyMinutes(5) // Define o intervalo de 5 minutos
      .create();
  
    // Cria um novo gatilho que executa a função 'buscarArquivo2' a cada 5 minutos
    ScriptApp.newTrigger("buscarArquivo2")
      .timeBased()
      .everyMinutes(5) // Define o intervalo de 5 minutos
      .create();
  
    // Cria um novo gatilho que executa a função 'buscarArquivo3' a cada 5 minutos
    ScriptApp.newTrigger("buscarArquivo3")
      .timeBased()
      .everyMinutes(5) // Define o intervalo de 5 minutos
      .create();
    
    Logger.log("Gatilhos criados para executar buscarArquivo, buscarArquivo2 e buscarArquivo3 a cada 5 minutos.");
  }
  
  // Função para remover gatilhos existentes (evitar múltiplos gatilhos)
  function removerGatilhosExistentes() {
    var allTriggers = ScriptApp.getProjectTriggers();
  
    allTriggers.forEach(function(trigger) {
      if (trigger.getHandlerFunction() === "buscarArquivo" || 
          trigger.getHandlerFunction() === "buscarArquivo2" || 
          trigger.getHandlerFunction() === "buscarArquivo3") {
        ScriptApp.deleteTrigger(trigger);
        Logger.log("Gatilho removido: " + trigger.getHandlerFunction());
      }
    });
  }
  