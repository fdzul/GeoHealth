# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blur.ui'
#
# Created: Fri Oct 30 18:47:40 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Blur(object):
    def setupUi(self, Blur):
        Blur.setObjectName(_fromUtf8("Blur"))
        Blur.resize(499, 517)
        Blur.setWindowTitle(_fromUtf8("Form"))
        self.verticalLayout = QtGui.QVBoxLayout(Blur)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(Blur)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(Blur)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.checkBox_selectedOnlyFeatures = QtGui.QCheckBox(Blur)
        self.checkBox_selectedOnlyFeatures.setText(_fromUtf8(""))
        self.checkBox_selectedOnlyFeatures.setObjectName(_fromUtf8("checkBox_selectedOnlyFeatures"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkBox_selectedOnlyFeatures)
        self.label_6 = QtGui.QLabel(Blur)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.checkBox_addToMap = QtGui.QCheckBox(Blur)
        self.checkBox_addToMap.setText(_fromUtf8(""))
        self.checkBox_addToMap.setChecked(True)
        self.checkBox_addToMap.setObjectName(_fromUtf8("checkBox_addToMap"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.checkBox_addToMap)
        self.label_3 = QtGui.QLabel(Blur)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox_layerToBlur = QtGui.QComboBox(Blur)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_layerToBlur.sizePolicy().hasHeightForWidth())
        self.comboBox_layerToBlur.setSizePolicy(sizePolicy)
        self.comboBox_layerToBlur.setObjectName(_fromUtf8("comboBox_layerToBlur"))
        self.horizontalLayout_2.addWidget(self.comboBox_layerToBlur)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.spinBox_radius = QtGui.QDoubleSpinBox(Blur)
        self.spinBox_radius.setMinimum(0.0)
        self.spinBox_radius.setMaximum(999999999.0)
        self.spinBox_radius.setSingleStep(50.0)
        self.spinBox_radius.setProperty("value", 500.0)
        self.spinBox_radius.setObjectName(_fromUtf8("spinBox_radius"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinBox_radius)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(Blur)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit_outputFile = QtGui.QLineEdit(Blur)
        self.lineEdit_outputFile.setEnabled(True)
        self.lineEdit_outputFile.setInputMask(_fromUtf8(""))
        self.lineEdit_outputFile.setText(_fromUtf8(""))
        self.lineEdit_outputFile.setObjectName(_fromUtf8("lineEdit_outputFile"))
        self.horizontalLayout.addWidget(self.lineEdit_outputFile)
        self.pushButton_browseFolder = QtGui.QPushButton(Blur)
        self.pushButton_browseFolder.setObjectName(_fromUtf8("pushButton_browseFolder"))
        self.horizontalLayout.addWidget(self.pushButton_browseFolder)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox_advanced = gui.QgsCollapsibleGroupBox(Blur)
        self.groupBox_advanced.setCollapsed(True)
        self.groupBox_advanced.setSaveCollapsedState(False)
        self.groupBox_advanced.setObjectName(_fromUtf8("groupBox_advanced"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_advanced)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame = QtGui.QFrame(self.groupBox_advanced)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.checkBox_exportRadius = QtGui.QCheckBox(self.frame)
        self.checkBox_exportRadius.setObjectName(_fromUtf8("checkBox_exportRadius"))
        self.verticalLayout_2.addWidget(self.checkBox_exportRadius)
        self.checkBox_exportCentroid = QtGui.QCheckBox(self.frame)
        self.checkBox_exportCentroid.setObjectName(_fromUtf8("checkBox_exportCentroid"))
        self.verticalLayout_2.addWidget(self.checkBox_exportCentroid)
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.groupBox_advanced)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkBox_envelope = QtGui.QCheckBox(self.frame_2)
        self.checkBox_envelope.setObjectName(_fromUtf8("checkBox_envelope"))
        self.horizontalLayout_3.addWidget(self.checkBox_envelope)
        self.comboBox_envelope = QtGui.QComboBox(self.frame_2)
        self.comboBox_envelope.setObjectName(_fromUtf8("comboBox_envelope"))
        self.horizontalLayout_3.addWidget(self.comboBox_envelope)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.groupBox_advanced)
        self.label_progress = QtGui.QLabel(Blur)
        self.label_progress.setText(_fromUtf8("progress text"))
        self.label_progress.setObjectName(_fromUtf8("label_progress"))
        self.verticalLayout.addWidget(self.label_progress)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.progressBar_blur = QtGui.QProgressBar(Blur)
        self.progressBar_blur.setProperty("value", 0)
        self.progressBar_blur.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_blur.setObjectName(_fromUtf8("progressBar_blur"))
        self.horizontalLayout_4.addWidget(self.progressBar_blur)
        self.buttonBox_blur = QtGui.QDialogButtonBox(Blur)
        self.buttonBox_blur.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_blur.setObjectName(_fromUtf8("buttonBox_blur"))
        self.horizontalLayout_4.addWidget(self.buttonBox_blur)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtGui.QSpacerItem(17, 66, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Blur)
        QtCore.QObject.connect(self.checkBox_envelope, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.comboBox_envelope.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Blur)

    def retranslateUi(self, Blur):
        self.label_4.setText(_translate("Blur", "Radius (map\'s unit)", None))
        self.label_5.setText(_translate("Blur", "Use only selected features", None))
        self.label_6.setText(_translate("Blur", "Add result to canvas", None))
        self.label_3.setText(_translate("Blur", "Point layer", None))
        self.label_7.setText(_translate("Blur", "Output :", None))
        self.lineEdit_outputFile.setPlaceholderText(_translate("Blur", "Save to temporary file", None))
        self.pushButton_browseFolder.setText(_translate("Blur", "Browse", None))
        self.groupBox_advanced.setTitle(_translate("Blur", "Advanced", None))
        self.label_8.setText(_translate("Blur", "Add to the attribute table :", None))
        self.checkBox_exportRadius.setText(_translate("Blur", "the radius", None))
        self.checkBox_exportCentroid.setText(_translate("Blur", "X and Y of centroid", None))
        self.checkBox_envelope.setText(_translate("Blur", "Use envelope", None))

from qgis import gui
from GeoHealth.resources import resources_rc
