import os
import sys
from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor, QImage
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(10,10, 300, 200)
        

        label = QLabel('첫번째 버튼 - 첫번째부터 16번째 이모티콘\n두번째 버튼 - 16번째부터 32번째 이모티콘 ', self)
        self.setStyleSheet("color: black;")
        label.move(10, 10)
        label.setFixedWidth(600)

        label = QLabel("문의: insta @diatomicarbon", self)
        label.move(10, 150)
        label.setFixedWidth(600)
        
        
        

        # 이미지 레이블을 만듭니다.
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.image_label)

        # 파일 선택 버튼을 만듭니다.
        self.select_button = QPushButton('1~16', self)
        self.select_button.clicked.connect(self.select_image1)
        self.select_button.move(50, 60)
        self.select_button.show()
        self.select_button.setStyleSheet("background-color: black; color: white; border-radius: 10px; font-size: 16px; padding: 6px;")

        self.select_button = QPushButton('17~32', self)
        self.select_button.clicked.connect(self.select_image2)
        self.select_button.move(50, 110)
        self.select_button.show()
        self.select_button.setStyleSheet("background-color: black; color: white; border-radius: 10px; font-size: 16px; padding: 6px;")


        # 이미지를 저장할 디렉토리 이름을 설정합니다.
        self.directory_name_1 = '카카오톡'
        self.directory_name_2 = '네이버OGQ'

    def select_image1(self):
        # 파일 선택 대화상자를 엽니다.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, '자를 이미지 선택', '', 'PNG (*.png);;All Files (*)', options=options)

        # 파일이 선택되었으면 이미지를 나눕니다.
        if file_name:
            # 이미지를 엽니다.
            try:
                im = Image.open(file_name)
            except IOError:
                print('Cannot open image file')
                return

            # 이미지의 크기를 얻습니다.
            width, height = im.size

            # 새로운 디렉토리를 만듭니다.
            try:
      
                # 새로운 디렉토리 생성
                os.makedirs(self.directory_name_1)
                os.makedirs(self.directory_name_2)
            
            except OSError:
                pass

            # 이미지를 16조각으로 나눕니다.
            piece_width = width // 4
            piece_height = height // 4
            count = 1
            for j in range(4):
                for i in range(4):
                    x = i * piece_width
                    y = j * piece_height
                    piece = im.crop((x, y, x + piece_width, y + piece_height))
                    filename = os.path.join(self.directory_name_1, '{}.png'.format(count))
                    piece_360 = piece.resize((360, 360))
                    piece_760 = piece.resize((640, 640))
        
                    new_img = Image.new(piece_760.mode, (640, 760), (0, 0, 0, 0))
                    new_img.paste(piece_760, (0, 60))

                    piece_360.save(filename)
                    filename = os.path.join(self.directory_name_2, '{}.png'.format(count))
                    new_img.save(filename)
                    count += 1

            # 이미지를 닫습니다.
            im.close()

            # # 이미지를 레이블에 표시합니다.
            # pixmap = QPixmap(file_name)
            # self.image_label.setPixmap(pixmap)

    def select_image2(self):
        # 파일 선택 대화상자를 엽니다.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, '자를 이미지 선택', '', 'PNG (*.png);;All Files (*)', options=options)

        # 파일이 선택되었으면 이미지를 나눕니다.
        if file_name:
            # 이미지를 엽니다.
            try:
                im = Image.open(file_name)
            except IOError:
                print('Cannot open image file')
                return

            # 이미지의 크기를 얻습니다.
            width, height = im.size

            # 이미지를 16조각으로 나눕니다.
            piece_width = width // 4
            piece_height = height // 4
            count = 17
            for j in range(4):
                for i in range(4):
                    x = i * piece_width
                    y = j * piece_height
                    piece = im.crop((x, y, x + piece_width, y + piece_height))
                    filename = os.path.join(self.directory_name_1, '{}.png'.format(count))
                    piece_360 = piece.resize((360, 360))
                    piece_760 = piece.resize((640, 640))
        
                    new_img = Image.new(piece_760.mode, (640, 760), (0, 0, 0, 0))
                    new_img.paste(piece_760, (0, 60))

                    piece_360.save(filename)
                    filename = os.path.join(self.directory_name_2, '{}.png'.format(count))
                    new_img.save(filename)
                    count += 1

            # 이미지를 닫습니다.
            im.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('이모티콘 사이즈 자동 변환기')
    window.show()
    sys.exit(app.exec_())
