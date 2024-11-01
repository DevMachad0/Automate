# Visão Geral do Sistema

O sistema consiste em duas partes principais: uma que interage com o Google Sheets e outra que automatiza a interação com uma aplicação web para baixar relatórios.

## Parte 1: Manipulação de Planilhas no Google Sheets

A primeira parte do código é responsável por buscar um arquivo específico no Google Drive, conceder permissões, convertê-lo para o formato do Google Sheets e copiar seus dados para uma planilha pré-definida. O fluxo é o seguinte:

1. **Busca de Arquivo**: O sistema procura um arquivo pelo nome especificado no Google Drive.
2. **Gerenciamento de Permissões**: Caso o arquivo seja encontrado, são concedidas permissões de edição ao usuário atual.
3. **Conversão de Formato**: O arquivo encontrado é convertido para o formato Google Sheets, permitindo uma melhor manipulação dos dados.
4. **Limpeza e Cópia de Dados**: Antes de colar os novos dados, a planilha de destino é limpa. Em seguida, os dados da nova planilha são copiados para a planilha original.

## Parte 2: Automação de Download de Relatórios

A segunda parte do código utiliza Selenium para automatizar a interação com um navegador e realizar downloads de relatórios de uma aplicação web. As etapas são as seguintes:

1. **Seleção de Diretório**: O usuário escolhe um diretório onde os arquivos baixados serão armazenados.
2. **Configuração do Navegador**: O navegador é configurado para baixar arquivos diretamente no diretório escolhido, sem solicitar confirmação.
3. **Login e Navegação**: O script realiza o login na aplicação web e navega até a seção onde os relatórios podem ser baixados.
4. **Preenchimento de Formulários**: O sistema preenche automaticamente os formulários necessários, como datas e opções de filtragem.
5. **Download do Relatório**: O relatório é baixado para o diretório especificado. O código verifica se o arquivo já existe e, se necessário, o remove antes de baixar o novo.
6. **Repetição de Processos**: O processo de download pode ser repetido em intervalos definidos, permitindo a coleta contínua de dados.
