from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('계산기')
        self.setFixedSize(400, 400)

        # 수식을 저장할 변수
        self.equa = ""

        # 수식 표시창
        self.equation = QLabel("계산식을 입력하세요 : ", self)
        self.equation.setStyleSheet("QLabel {font-size: 20px;}")

        # 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.equation)

        grid = QGridLayout()
        vbox.addLayout(grid)

        # 버튼 생성 및 배치
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for text, row, col in buttons:
            button = QPushButton(text, self)
            button.setStyleSheet("QPushButton {font-size: 18px; height: 40px; width: 40px;}")
            button.clicked.connect(self.onButtonClick)
            grid.addWidget(button, row, col)

        self.setLayout(vbox)

    def onButtonClick(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.equa = ""
            self.equation.setText("계산식을 입력하세요 : ")
        elif text == '=':
            try:
                # 수식을 계산하고 결과를 표시
                result = str(eval(self.equa))
                self.equation.setText(result)
                self.equa = result  # 결과를 그대로 다음 수식으로 이어서 계산할 수 있게 설정
            except Exception as e:
                self.equation.setText("오류")
                self.equa = ""
        else:
            self.equa += text
            self.equation.setText(self.equa)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
