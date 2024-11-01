import sys
from PyQt6 import QtWidgets
from visual.app_visual import Ui_Form  # Importa sua interface
from clif_script import open_link  # Importa a função do Selenium
from clif_geral import open_link2
from clif_entradas_pendentes import open_link3


time_mapping = {
    "5min": 5,
    "10min": 10,
    "15min": 15,
    "20min": 20,
    "30min": 30
}

# Dicionário para armazenar as opções do comboBox_2
opcoes_comboBox_2 = {
    'Todos': 0,  # Usaremos índices
    'Sesce': 1,
    'Cedib': 2
}

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Cria uma instância da classe Ui_Form
        self.ui.setupUi(self)  # Configura a interface na janela

        # Adiciona as opções ao comboBox_2
        self.ui.comboBox_2.addItems(opcoes_comboBox_2.keys())

        # Conectar o botão à função
        self.ui.pushButton.clicked.connect(self.handle_button)

    def handle_button(self):
        # Obtém os valores de login e senha dos lineEdit
        login = self.ui.lineEdit.text()  # Obtém o texto do lineEdit de login
        senha = self.ui.lineEdit_2.text()  # Obtém o texto do lineEdit de senha
        
        # Obtém as datas de início e fim
        datainicio = self.ui.dateEdit.date().toString("dd/MM/yyyy")
        datafim = self.ui.dateEdit_2.date().toString("dd/MM/yyyy")

        # Obtém a seleção do comboBox
        selected_time = self.ui.comboBox.currentText()  # Obtém o texto selecionado no comboBox
        time_value = time_mapping.get(selected_time, 0)  # Mapeia o valor selecionado

        # Obtém a seleção do comboBox_2
        opcao_selecionada = self.ui.comboBox_2.currentText()  # Obtém o texto selecionado no comboBox_2
        armazem_index = opcoes_comboBox_2[opcao_selecionada]  # Obtém o índice associado

        # Verifica qual radioButton está selecionado
        if self.ui.radioButton.isChecked():
            # Chama a função open_link
            open_link(login, senha, datainicio, datafim, time_value, armazem_index)
            
        if self.ui.radioButton_5.isChecked():
            # Chama a função open_link2
            open_link2(login, senha, datainicio, datafim, time_value, armazem_index)

        elif self.ui.radioButton_2.isChecked():
            # Chama a função open_link2
            open_link3(login, senha, datainicio, datafim, time_value, armazem_index)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()  # Cria uma instância da MainWindow
    mainWindow.setWindowTitle("Automate")  # Título da janela
    mainWindow.resize(330, 392)  # Tamanho da janela
    mainWindow.show()  # Mostra a janela
    sys.exit(app.exec())  # Executa a aplicação
