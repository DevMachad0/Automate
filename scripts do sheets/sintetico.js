function buscarArquivo() {
    var nomeArquivo = "relatorio_saidas_geral_sintetico_col.xlsx"; // Nome do arquivo a ser buscado
    var sheet = SpreadsheetApp.openById("1cS2QSsBlSfctV1jLx9oCiH4FvRVxVVtzqa4YQ3mF8Yw").getSheetByName("sintetico");
  
    // Buscar o arquivo com base no nome
    var resultado = buscarArquivoPorNome(nomeArquivo);
  
    if (resultado[0][2]) { // Verifica se o arquivo foi encontrado
      var file = resultado[0][2];
      mudarPermissoes(file.getId()); // Concede acesso total ao arquivo
  
      // Aguarda um tempo para que as permissões sejam aplicadas
      Utilities.sleep(3000);
  
      // Converte o arquivo para o formato Google Sheets
      var novoId = converterParaGoogleSheets(file);
      
      if (novoId) {
        // Concede permissões ao usuário atual para acessar a nova planilha
        mudarPermissoes(novoId);
  
        // Copia os dados da nova planilha
        var novaPlanilha = SpreadsheetApp.openById(novoId);
        var dados = novaPlanilha.getSheetByName("relsaidasgeral_sintetico_col").getRange("A1:Z19999").getValues();
  
        // **Agora faz a limpeza somente antes de colar os dados**
        sheet.getRange(1, 1, 9999, 26).clearContent(); // Limpa o intervalo de A1:Z9999
        
        // Aguarda 1 segundo antes de colar os dados
        Utilities.sleep(1000);
  
        // Cola os dados na planilha original, a partir da célula A1
        sheet.getRange(1, 1, dados.length, dados[0].length).setValues(dados);
        Logger.log('Dados copiados da nova planilha para Página1.');
      }
    } else {
      // Se o arquivo não for encontrado, insere uma mensagem de erro na linha 1
      sheet.getRange(1, 1).setValue("Nenhum arquivo encontrado");
    }
  }
  
  function buscarArquivoPorNome(nomeArquivo) {
    if (!nomeArquivo) {
      Logger.log("O nome do arquivo não pode estar vazio.");
      return [["Por favor, forneça um nome de arquivo."]];
    }
  
    var files = DriveApp.getFilesByName(nomeArquivo);
    var results = [];
  
    if (files.hasNext()) {
      var file = files.next();
      results.push([file.getName(), file.getUrl(), file]); // Adiciona o arquivo ao resultado
      Logger.log("Arquivo encontrado: " + results[0][0] + ": " + results[0][1]);
    } else {
      Logger.log("Nenhum arquivo encontrado com o nome: " + nomeArquivo);
    }
  
    return results.length > 0 ? results : [["Nenhum arquivo encontrado"]];
  }
  
  function converterParaGoogleSheets(file) {
    try {
      var blob = file.getBlob();
      var newFile = {
        title: file.getName(),
        mimeType: MimeType.GOOGLE_SHEETS
      };
      
      // Cria a nova planilha convertida
      var newSpreadsheet = Drive.Files.insert(newFile, blob);
      Logger.log("Arquivo convertido: " + newSpreadsheet.id);
      
      return newSpreadsheet.id; // Retorna o ID da nova planilha
    } catch (e) {
      Logger.log("Erro ao converter o arquivo: " + e.message);
      return null;
    }
  }
  
  function mudarPermissoes(fileId) {
    var file = DriveApp.getFileById(fileId);
    
    // Adiciona permissão de editor ao usuário atual
    file.addEditor(Session.getActiveUser().getEmail());
    
    Logger.log('Permissão de editor concedida ao usuário: ' + Session.getActiveUser().getEmail());
  }
  