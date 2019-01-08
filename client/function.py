def open_img(self):
    file_path, _ = QFileDialog.getOpenFileName(self.Form, "选择图片",
                                               r"C:\Users\jack xia\Desktop\Person_reID_baseline_pytorch\Market\pytorch\0342")
    img = QImage()
    img.load(file_path)  # 载入图片
    self.img = img
    self.img = img.scaled(self.graphicsView.width(), self.graphicsView.height())
    self.graphicsView.scene = QGraphicsScene()  # 创建一个图片元素的对象
    self.graphicsView.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
    self.graphicsView.setScene(self.graphicsView.scene)
    self.lineEdit.append(file_path)
    # with open(file_path, 'rb') as f:
    #     image = f.read()
    # self.img = image

def get_data(self):
    base_url = 'http://172.16.22.125:8000/api/data/Perter?q='
    index = '777'
    url = base_url+index
    data = requests.get(url).text
    data = json.loads(data)
    print(type(data))
    print("---data---", data)
    img_addrs = data['detail']
    print(type(img_addrs))
    text = ''
    for img in img_addrs:
        text += img[12:]
        text += '\n'
    self.textBrowser.append(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
