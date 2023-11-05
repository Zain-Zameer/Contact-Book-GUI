from PyQt5 import QtCore, QtGui, QtWidgets
import sys



namesData = []
phonesData = []
mailsData = []
addressData = []

global takeName
global takePhone
global takeMail
global takeAddress
global countCont


class Ui_HomeWindow(object):
    def __init__(self):
        self.i = 0
        self.takeName  = None
        self.takePhone = None
        self.takeMail  = None
        self.takeAddress = None
        self.searchBar = None

        #output on screen
        self.contactName = None
        self.contactEmail = None
        self.contactAddress = None
        self.contactPhoneNumber = None

    def get_Info(self):
        if self.takeName is not None:
            name = self.takeName.text()
            phone = self.takePhone.text()
            mail = self.takeMail.text()
            address = self.takeAddress.text()

            # Append the data to lists (DataBase)
            namesData.append(name)
            phonesData.append(phone)
            mailsData.append(mail)
            addressData.append(address)

            self.i+=1 
            self.countCont.setProperty("intValue", self.i)

            # Clear the input fields
            self.takeName.clear()
            self.takeAddress.clear()
            self.takePhone.clear()
            self.takeMail.clear()

            self.ContactView.addItem(f"{name[0]} - Name: {name}\n      Phone: {phone}\n      Email: {mail}\n      Address: {address}\n\n")

    def resetInfo(self):
        if self.takeName is not None:
            self.takeName.clear()
            self.takeMail.clear()
            self.takeAddress.clear()
            self.takePhone.clear()

    def updateInfoInDatabase(self):
        selectedItem = self.ContactView.currentItem()
        if self.takeName is not None:
            name = self.takeName.text()
            phone = self.takePhone.text()
            mail = self.takeMail.text()
            address = self.takeAddress.text()
        
        
        for i in range(0,len(namesData)):
            if name == namesData[i]: 
                namesData[i] = name 
                mailsData[i] = mail
                phonesData[i] = phone 
                addressData[i] = address

        self.takeName.clear()
        self.takeAddress.clear()
        self.takePhone.clear()
        self.takeMail.clear()

        # Remove the selected item and then update
        row = self.ContactView.row(selectedItem)
        self.ContactView.takeItem(row)
        self.ContactView.addItem(f"{name[0]} - Name: {name}\n      Phone: {phone}\n      Email: {mail}\n      Address: {address}\n")

    def searchContact(self):
        print(namesData)
        nameContact = self.searchBar.toPlainText()
        if self.searchBar is not None:
            self.ContactView.clear()
            for j in range(len(namesData)):
                if nameContact == namesData[j]:
                    self.ContactView.addItem(f"{namesData[j][0]} - {namesData[j]} Contact Available")
        if str(nameContact)=="" or nameContact is None:
            for k in range(len(namesData)):
                self.ContactView.addItem(f"{namesData[k][0]} - Name: {namesData[k]}\n      Phone: {phonesData[k]}\n      Email: {mailsData[k]}\n      Address: {addressData[k]}\n")

    def deleteContactClicked(self):
        selectedItem = self.ContactView.currentItem()

        if selectedItem is not None:
            self.i-=1
            self.countCont.setProperty("intValue", str(self.i))
            self.ContactView.takeItem(self.ContactView.row(selectedItem))
          

    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(1148, 713)
        HomeWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.centralwidget.setStyleSheet("background-color : lightgrey")


        self.searchBut = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.searchBut.setGeometry(QtCore.QRect(430, 120, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(11)
        self.searchBut.setFont(font)
        self.searchBut.setText("")
        icon = QtGui.QIcon.fromTheme("edit-find")
        self.searchBut.setIcon(icon)
        self.searchBut.setIconSize(QtCore.QSize(30, 30))
        self.searchBut.setObjectName("searchBut")
        self.searchBut.setStyleSheet("border:2px solid black;background-color:black")
        self.searchBut.clicked.connect(self.searchContact)
        self.searchBar = QtWidgets.QTextEdit(self.centralwidget)
        self.searchBar.setGeometry(QtCore.QRect(0, 120, 471, 51))
        self.searchBar.setStyleSheet("background-color : darkgrey;color:black")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.searchBar.setFont(font)
        self.searchBar.setObjectName("searchBar")
        self.takeName = QtWidgets.QLineEdit(self.centralwidget)
        self.takeName.setGeometry(QtCore.QRect(640, 210, 311, 41))
        self.takeName.setObjectName("takeName")
        self.takeName.setStyleSheet("background-color : lightblack")
        self.enterNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.enterNameLabel.setGeometry(QtCore.QRect(740, 190, 101, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enterNameLabel.setFont(font)
        self.enterNameLabel.setStyleSheet("color : lightblack")
        self.enterNameLabel.setObjectName("enterNameLabel")
        self.takePhone = QtWidgets.QLineEdit(self.centralwidget)
        self.takePhone.setStyleSheet("background-color : lightblack")
        self.takePhone.setGeometry(QtCore.QRect(640, 290, 311, 41))
        self.takePhone.setText("")
        self.takePhone.setObjectName("takePhone")
        self.enterPhoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.enterPhoneLabel.setGeometry(QtCore.QRect(710, 270, 191, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enterPhoneLabel.setFont(font)
        self.enterPhoneLabel.setObjectName("enterPhoneLabel")
        self.enterPhoneLabel.setStyleSheet("color : lightblack")
        self.enterEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.enterEmailLabel.setGeometry(QtCore.QRect(740, 350, 101, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enterEmailLabel.setFont(font)
        self.enterEmailLabel.setObjectName("enterEmailLabel")
        self.enterEmailLabel.setStyleSheet("color : lightblack")
        self.takeMail = QtWidgets.QLineEdit(self.centralwidget)
        self.takeMail.setStyleSheet("background-color : lightblack")
        self.takeMail.setGeometry(QtCore.QRect(640, 370, 311, 41))
        self.takeMail.setText("")
        self.takeMail.setObjectName("takeMail")
        self.enterAddressLabel = QtWidgets.QLabel(self.centralwidget)
        self.enterAddressLabel.setGeometry(QtCore.QRect(740, 430, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enterAddressLabel.setFont(font)
        self.enterAddressLabel.setObjectName("enterAddressLabel")
        self.enterAddressLabel.setStyleSheet("color : lightblack")
        self.takeAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.takeAddress.setStyleSheet("background-color : lightblack")
        self.takeAddress.setGeometry(QtCore.QRect(640, 450, 311, 41))
        self.takeAddress.setText("")
        self.takeAddress.setObjectName("takeAddress")
        self.saveButtonContact = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.saveButtonContact.setGeometry(QtCore.QRect(860, 560, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(11)
        self.saveButtonContact.setFont(font)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.saveButtonContact.setIcon(icon)
        self.saveButtonContact.setStyleSheet("color : black;border: 2px solid black")

        self.saveButtonContact.setIconSize(QtCore.QSize(30, 30))
        self.saveButtonContact.setObjectName("saveButtonContact")
        self.saveButtonContact.clicked.connect(self.get_Info)
        self.resetButtonAddContact = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.resetButtonAddContact.setGeometry(QtCore.QRect(630, 560, 91, 41))
        self.resetButtonAddContact.setStyleSheet("color : black;border: 2px solid black")
        
        self.resetButtonAddContact.clicked.connect(self.resetInfo)
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(11)
        self.resetButtonAddContact.setFont(font)
        icon = QtGui.QIcon.fromTheme("edit-undo")
        self.resetButtonAddContact.setIcon(icon)
        self.resetButtonAddContact.setIconSize(QtCore.QSize(30, 30))
        self.resetButtonAddContact.setObjectName("resetButtonAddContact")
        self.deleteContact = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.deleteContact.setGeometry(QtCore.QRect(740, 510, 101, 41))
        self.deleteContact.setStyleSheet("color : black;border: 2px solid black")
        
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(11)
        self.deleteContact.setFont(font)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.deleteContact.setIcon(icon)
        self.deleteContact.setIconSize(QtCore.QSize(30, 30))
        self.deleteContact.setObjectName("deleteContact")
        self.deleteContact.clicked.connect(self.deleteContactClicked)
        self.updateButtonContact = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.updateButtonContact.setGeometry(QtCore.QRect(740, 620, 101, 41))
        self.updateButtonContact.clicked.connect(self.updateInfoInDatabase)
        self.updateButtonContact.setStyleSheet("color : black;border: 2px solid black")
        
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(11)
        self.updateButtonContact.setFont(font)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.updateButtonContact.setIcon(icon)
        self.updateButtonContact.setIconSize(QtCore.QSize(30, 30))
        self.updateButtonContact.setObjectName("updateButtonContact")
        self.countCont = QtWidgets.QLCDNumber(self.centralwidget)
        self.countCont.setGeometry(QtCore.QRect(130, 40, 171, 71))
        font = QtGui.QFont()
        font.setBold(True)
        self.countCont.setFont(font)
        self.countCont.setDigitCount(2)
        self.countCont.setProperty("intValue", 0)
        self.countCont.setObjectName("countCont")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 20, 611, 131))
        self.label.setStyleSheet("color: lightblack")
        font = QtGui.QFont()
        font.setFamily("MathJax_SansSerif")
        font.setPointSize(52)
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ContactView = QtWidgets.QListWidget(self.centralwidget)
        self.ContactView.setGeometry(QtCore.QRect(0, 180, 471, 521))

        self.ContactView.setStyleSheet("background-color : darkgrey;color:black")

        font = QtGui.QFont()
        font.setPointSize(15)
        self.ContactView.setFont(font)
        self.ContactView.setObjectName("ContactView")
        item = QtWidgets.QListWidgetItem()
        self.ContactView.addItem(item)
        self.searchBar.raise_()
        self.searchBut.raise_()
        self.takeName.raise_()
        self.enterNameLabel.raise_()
        self.takePhone.raise_()
        self.enterPhoneLabel.raise_()
        self.enterEmailLabel.raise_()
        self.takeMail.raise_()
        self.enterAddressLabel.raise_()
        self.takeAddress.raise_()
        self.saveButtonContact.raise_()
        self.resetButtonAddContact.raise_()
        self.deleteContact.raise_()
        self.updateButtonContact.raise_()
        self.countCont.raise_()
        self.label.raise_()
        self.ContactView.raise_()
        HomeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "Contact Book"))
        self.searchBar.setHtml(_translate("HomeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.enterNameLabel.setText(_translate("HomeWindow", "Enter Name"))
        self.enterPhoneLabel.setText(_translate("HomeWindow", "Enter Phone Number"))
        self.enterEmailLabel.setText(_translate("HomeWindow", "Enter Email"))
        self.enterAddressLabel.setText(_translate("HomeWindow", "Enter Address"))
        self.saveButtonContact.setText(_translate("HomeWindow", "Save"))
        self.resetButtonAddContact.setText(_translate("HomeWindow", "Reset"))
        self.deleteContact.setText(_translate("HomeWindow", "Delete"))
        self.updateButtonContact.setText(_translate("HomeWindow", "Update"))
        self.label.setText(_translate("HomeWindow", "CONTACT BOOK"))
        __sortingEnabled = self.ContactView.isSortingEnabled()
        self.ContactView.setSortingEnabled(False)
        
        self.ContactView.setSortingEnabled(__sortingEnabled)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
