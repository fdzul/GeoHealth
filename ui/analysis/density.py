# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'density.ui'
#
# Created: Fri Oct 30 18:47:49 2015
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

class Ui_Density(object):
    def setupUi(self, Density):
        Density.setObjectName(_fromUtf8("Density"))
        Density.resize(651, 613)
        self.verticalLayout = QtGui.QVBoxLayout(Density)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(Density)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.cbx_case_layer = QtGui.QComboBox(Density)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_case_layer.sizePolicy().hasHeightForWidth())
        self.cbx_case_layer.setSizePolicy(sizePolicy)
        self.cbx_case_layer.setObjectName(_fromUtf8("cbx_case_layer"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cbx_case_layer)
        self.label = QtGui.QLabel(Density)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.cbx_aggregation_layer = QtGui.QComboBox(Density)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_aggregation_layer.sizePolicy().hasHeightForWidth())
        self.cbx_aggregation_layer.setSizePolicy(sizePolicy)
        self.cbx_aggregation_layer.setObjectName(_fromUtf8("cbx_aggregation_layer"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cbx_aggregation_layer)
        self.label_2 = QtGui.QLabel(Density)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cbx_ratio = QtGui.QComboBox(Density)
        self.cbx_ratio.setEditable(True)
        self.cbx_ratio.setObjectName(_fromUtf8("cbx_ratio"))
        self.cbx_ratio.addItem(_fromUtf8(""))
        self.cbx_ratio.addItem(_fromUtf8(""))
        self.cbx_ratio.addItem(_fromUtf8(""))
        self.cbx_ratio.addItem(_fromUtf8(""))
        self.cbx_ratio.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cbx_ratio)
        self.label_3 = QtGui.QLabel(Density)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.le_new_column = QtGui.QLineEdit(Density)
        self.le_new_column.setMaxLength(10)
        self.le_new_column.setObjectName(_fromUtf8("le_new_column"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.le_new_column)
        self.checkBox_addNbIntersections = QtGui.QCheckBox(Density)
        self.checkBox_addNbIntersections.setObjectName(_fromUtf8("checkBox_addNbIntersections"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkBox_addNbIntersections)
        self.checkBox_incidence_runStats = QtGui.QCheckBox(Density)
        self.checkBox_incidence_runStats.setChecked(True)
        self.checkBox_incidence_runStats.setObjectName(_fromUtf8("checkBox_incidence_runStats"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.checkBox_incidence_runStats)
        self.label_5 = QtGui.QLabel(Density)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.le_output_filepath = QtGui.QLineEdit(Density)
        self.le_output_filepath.setObjectName(_fromUtf8("le_output_filepath"))
        self.horizontalLayout.addWidget(self.le_output_filepath)
        self.button_browse = QtGui.QPushButton(Density)
        self.button_browse.setObjectName(_fromUtf8("button_browse"))
        self.horizontalLayout.addWidget(self.button_browse)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.symbology = gui.QgsCollapsibleGroupBox(Density)
        self.symbology.setCheckable(True)
        self.symbology.setCollapsed(False)
        self.symbology.setObjectName(_fromUtf8("symbology"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.symbology)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_9 = QtGui.QLabel(self.symbology)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.color_low_value = gui.QgsColorButtonV2(self.symbology)
        self.color_low_value.setColor(QtGui.QColor(255, 246, 246))
        self.color_low_value.setObjectName(_fromUtf8("color_low_value"))
        self.horizontalLayout_3.addWidget(self.color_low_value)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_10 = QtGui.QLabel(self.symbology)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.color_high_value = gui.QgsColorButtonV2(self.symbology)
        self.color_high_value.setColor(QtGui.QColor(202, 33, 36))
        self.color_high_value.setObjectName(_fromUtf8("color_high_value"))
        self.horizontalLayout_3.addWidget(self.color_high_value)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_11 = QtGui.QLabel(self.symbology)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.spinBox_classes = QtGui.QSpinBox(self.symbology)
        self.spinBox_classes.setMinimum(1)
        self.spinBox_classes.setProperty("value", 5)
        self.spinBox_classes.setObjectName(_fromUtf8("spinBox_classes"))
        self.horizontalLayout_4.addWidget(self.spinBox_classes)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_12 = QtGui.QLabel(self.symbology)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.cbx_mode = QtGui.QComboBox(self.symbology)
        self.cbx_mode.setObjectName(_fromUtf8("cbx_mode"))
        self.horizontalLayout_4.addWidget(self.cbx_mode)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.symbology)
        self.button_box_ok = QtGui.QDialogButtonBox(Density)
        self.button_box_ok.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_ok.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box_ok.setObjectName(_fromUtf8("button_box_ok"))
        self.verticalLayout.addWidget(self.button_box_ok)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(Density)
        self.tableWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.layout_plot = QtGui.QVBoxLayout()
        self.layout_plot.setObjectName(_fromUtf8("layout_plot"))
        self.horizontalLayout_2.addLayout(self.layout_plot)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Density)
        self.cbx_ratio.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Density)

    def retranslateUi(self, Density):
        Density.setWindowTitle(_translate("Density", "Density", None))
        self.label_4.setText(_translate("Density", "Case layer", None))
        self.label.setText(_translate("Density", "Layer for aggregation", None))
        self.label_2.setText(_translate("Density", "Ratio", None))
        self.cbx_ratio.setItemText(0, _translate("Density", "10", None))
        self.cbx_ratio.setItemText(1, _translate("Density", "100", None))
        self.cbx_ratio.setItemText(2, _translate("Density", "1 000", None))
        self.cbx_ratio.setItemText(3, _translate("Density", "10 000", None))
        self.cbx_ratio.setItemText(4, _translate("Density", "100 000", None))
        self.label_3.setText(_translate("Density", "New column", None))
        self.le_new_column.setPlaceholderText(_translate("Density", "density", None))
        self.checkBox_addNbIntersections.setToolTip(_translate("Density", "Add the number of cases per unit to the attribute table", None))
        self.checkBox_addNbIntersections.setText(_translate("Density", "Add the number of cases per unit to the attribute table", None))
        self.checkBox_incidence_runStats.setText(_translate("Density", "Calculate statistics", None))
        self.label_5.setText(_translate("Density", "Output", None))
        self.le_output_filepath.setPlaceholderText(_translate("Density", "Save to temporary file", None))
        self.button_browse.setText(_translate("Density", "Browse", None))
        self.symbology.setTitle(_translate("Density", "Add a symbology", None))
        self.label_9.setText(_translate("Density", "Low incidence", None))
        self.label_10.setText(_translate("Density", "High incidence", None))
        self.label_11.setText(_translate("Density", "Classes", None))
        self.label_12.setText(_translate("Density", "Mode", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Density", "Parameter", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Density", "Value", None))

from qgis import gui
