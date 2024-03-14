import sys
# Importação dos elementos gráficos do pacote PyQt
from PyQt5.QtWidgets import QWidget,QApplication, QLabel,QLineEdit,QTableWidget, QTableWidgetItem,QHBoxLayout,QVBoxLayout,QComboBox,QPushButton
# Para usar imagens em nosso projeto iremos importar QPixmsp do
# pacote PyQT5.Gui
from PyQt5.QtGui import QPixmap
 
class PDV(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setGeometry(5,30,1580,820)
        self.setWindowTitle("Janela")
 
        # Criação do layout principal horizontal
        layout_principal = QVBoxLayout()
       
       
        # Criação de 4 labels que representarão as 4 áreas da nossa janela
        label_col_cima = QLabel()
        label_col_meio = QLabel()
        label_col_meio2 = QLabel()
        label_col_baixo = QLabel()
 
        # configuração de tamanho e a cor das labels
        label_col_cima.setStyleSheet("QLabel{background-color:red}")
        label_col_cima.setFixedHeight(300)
 
        label_col_meio.setStyleSheet("QLabel{background-color:blue}")
        label_col_meio.setFixedHeight(60)
 
        label_col_meio2.setStyleSheet("QLabel{background-color:yellow}")
        label_col_meio2.setFixedHeight(400)
 
        label_col_baixo.setStyleSheet("QLabel{background-color:green}")
        label_col_baixo.setFixedHeight(100)
 
        # Vamos adicionar as quatro labels ao layout principal
        layout_principal.addWidget(label_col_cima)
        layout_principal.addWidget(label_col_meio)
        layout_principal.addWidget(label_col_meio2)
        layout_principal.addWidget(label_col_baixo)
 
        # criação de um layout horizontal para distribuição das 3 colunas na parte superior
        # as 3 colunas serão criadas com label e serão adicionadas ao layout horizontal
        layout_hor_lb_superior = QHBoxLayout()
 
        # Labels de divisão que ficarão no layout superior
        label_col_esquerda = QLabel()
        label_col_meio3 = QLabel()
        label_col_direita = QLabel()
 
        # ------------------------------------------------
        label_col_esquerda.setStyleSheet("QLabel{background-color:gray}")
        label_col_meio3.setStyleSheet("QLabel{background-color:gray}")
        label_col_direita.setStyleSheet("QLabel{background-color:gray}")
 
 
        # -------------------------------------------------------------------------------------
        layout_hor_lb_superior.addWidget(label_col_esquerda)
        layout_hor_lb_superior.addWidget(label_col_meio3)
        layout_hor_lb_superior.addWidget(label_col_direita)
 
        label_col_cima.setLayout(layout_hor_lb_superior)
 
        # CRIAÇÃO DE LAYOUT E LABELS QCOMBOBOX
        layout_ver_col_esquerda = QVBoxLayout()
 
        label_estabelecimento = QLabel("Estabelecimento:")
        label_estabelecimento.setStyleSheet("QLabel{font-size:15pt; color:white}")
        combo_estabelecimento = QComboBox()
        combo_estabelecimento.setStyleSheet("QComboBox{padding:10px; font-size:15pt}")
        layout_ver_col_esquerda.addWidget(label_estabelecimento)
        layout_ver_col_esquerda.addWidget(combo_estabelecimento)
        label_col_esquerda.setLayout(layout_ver_col_esquerda)
 
        label_documento = QLabel("Documento:")
        label_documento.setStyleSheet("QLabel{font-size:15pt; color:white}")
        combo_documento = QComboBox()
        combo_documento.setStyleSheet("QComboBox{padding:10px; font-size:15pt}")
        layout_ver_col_esquerda.addWidget(label_documento)
        layout_ver_col_esquerda.addWidget(combo_documento)
        label_col_esquerda.setLayout(layout_ver_col_esquerda)
 
        label_grupo = QLabel("Grupo:")
        label_grupo.setStyleSheet("QLabel{font-size:15pt; color:white}")
        combo_grupo = QComboBox()
        combo_grupo.setStyleSheet("QComboBox{padding:10px; font-size:15pt}")
        layout_ver_col_esquerda.addWidget(label_grupo)
        layout_ver_col_esquerda.addWidget(combo_grupo)
        label_col_esquerda.setLayout(layout_ver_col_esquerda)
 
        # ----
        layout_ver_col_meio = QVBoxLayout()
 
        label_projeto = QLabel("Projeto:")
        label_projeto.setStyleSheet("QLabel{font-size:15pt; color:white}")
        combo_projeto = QComboBox()
        combo_projeto.setStyleSheet("QComboBox{padding:10px; font-size:15pt}")
        layout_ver_col_meio.addWidget(label_projeto)
        layout_ver_col_meio.addWidget(combo_projeto)
        label_col_meio3.setLayout(layout_ver_col_meio)
 
        label_numero = QLabel("Número:")
        label_numero.setStyleSheet("QLabel{font-size:15pt; color:white}")
        combo_numero = QComboBox()
        combo_numero.setStyleSheet("QComboBox{padding:10px; font-size:15pt}")
        layout_ver_col_meio.addWidget(label_numero)
        layout_ver_col_meio.addWidget(combo_numero)
        label_col_meio3.setLayout(layout_ver_col_meio)
 
        label_projeto = QLabel("Produto:")
        label_projeto.setStyleSheet("QLabel{font-size:15pt; color:white}")
        combo_projeto = QComboBox()
        combo_projeto.setStyleSheet("QComboBox{padding:10px; font-size:15pt}")
        layout_ver_col_meio.addWidget(label_projeto)
        layout_ver_col_meio.addWidget(combo_projeto)
        label_col_meio3.setLayout(layout_ver_col_meio)
 
 
        # criação de um layout horizontal para distribuição das 3 colunas na parte do meio
        # as 3 colunas serão criadas com label e serão adicionadas ao layout horizontal
        layout_hor_lb_meio = QHBoxLayout()
 
        # Labels de divisão que ficarão no layout do meio
        label_col_esquerda2 = QLabel()
        label_col_meio4 = QLabel()
        label_col_direita2 = QLabel()
 
        # _____________________________________________________________________________
        label_col_esquerda2.setStyleSheet("QLabel{background-color:orange}")
        label_col_meio4.setStyleSheet("QLabel{background-color:#dddddd}")
        label_col_direita2.setStyleSheet("QLabel{background-color:#333333}")
 
        # ________________________________________________________________________________
        layout_hor_lb_meio.addWidget(label_col_esquerda2)
        layout_hor_lb_meio.addWidget(label_col_meio4)
        layout_hor_lb_meio.addWidget(label_col_direita2)
 
        label_col_meio.setLayout(layout_hor_lb_meio)
 
        # Adicionar layout principal a tela
        self.setLayout(layout_principal)
       
 
 
app = QApplication(sys.argv)
janela = PDV()
janela.show()
app.exec_()