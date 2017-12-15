# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 472, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgetLayout = QtWidgets.QVBoxLayout()
        self.widgetLayout.setObjectName("widgetLayout")
        self.verticalLayout_3.addLayout(self.widgetLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.progress_OK = QtWidgets.QHBoxLayout()
        self.progress_OK.setObjectName("progress_OK")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progress_OK.addWidget(self.progressBar)
        self.undoModulePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.undoModulePushButton.setObjectName("undoModulePushButton")
        self.progress_OK.addWidget(self.undoModulePushButton)
        self.stopPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopPushButton.setObjectName("stopPushButton")
        self.progress_OK.addWidget(self.stopPushButton)
        self.deleteModulePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteModulePushButton.setObjectName("deleteModulePushButton")
        self.progress_OK.addWidget(self.deleteModulePushButton)
        self.okPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.okPushButton.setObjectName("okPushButton")
        self.progress_OK.addWidget(self.okPushButton)
        self.verticalLayout.addLayout(self.progress_OK)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPreprocessing = QtWidgets.QMenu(self.menubar)
        self.menuPreprocessing.setObjectName("menuPreprocessing")
        self.menuRegression = QtWidgets.QMenu(self.menubar)
        self.menuRegression.setObjectName("menuRegression")
        self.menuVisualization = QtWidgets.QMenu(self.menubar)
        self.menuVisualization.setObjectName("menuVisualization")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuDark_Mode = QtWidgets.QMenu(self.menuOptions)
        self.menuDark_Mode.setObjectName("menuDark_Mode")
        self.menuDebug_Mode = QtWidgets.QMenu(self.menuOptions)
        self.menuDebug_Mode.setObjectName("menuDebug_Mode")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRead_ChemCam_Data = QtWidgets.QAction(MainWindow)
        self.actionRead_ChemCam_Data.setObjectName("actionRead_ChemCam_Data")
        self.actionLoad_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Data.setObjectName("actionLoad_Data")
        self.actionSet_Output_Path = QtWidgets.QAction(MainWindow)
        self.actionSet_Output_Path.setObjectName("actionSet_Output_Path")
        self.actionSave_Current_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Data.setObjectName("actionSave_Current_Data")
        self.actionCreate_New_Workflow = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Workflow.setObjectName("actionCreate_New_Workflow")
        self.actionRestore_Workflow = QtWidgets.QAction(MainWindow)
        self.actionRestore_Workflow.setObjectName("actionRestore_Workflow")
        self.actionSave_Current_Workflow = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Workflow.setObjectName("actionSave_Current_Workflow")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRemove_Rows = QtWidgets.QAction(MainWindow)
        self.actionRemove_Rows.setObjectName("actionRemove_Rows")
        self.actionSplit_Data = QtWidgets.QAction(MainWindow)
        self.actionSplit_Data.setObjectName("actionSplit_Data")
        self.actionInterpolate = QtWidgets.QAction(MainWindow)
        self.actionInterpolate.setObjectName("actionInterpolate")
        self.actionRemove_Baseline = QtWidgets.QAction(MainWindow)
        self.actionRemove_Baseline.setObjectName("actionRemove_Baseline")
        self.actionApply_Mask = QtWidgets.QAction(MainWindow)
        self.actionApply_Mask.setObjectName("actionApply_Mask")
        self.actionPeak_Areas = QtWidgets.QAction(MainWindow)
        self.actionPeak_Areas.setObjectName("actionPeak_Areas")
        self.actionMultiply_by_Vector = QtWidgets.QAction(MainWindow)
        self.actionMultiply_by_Vector.setObjectName("actionMultiply_by_Vector")
        self.actionNormalization = QtWidgets.QAction(MainWindow)
        self.actionNormalization.setObjectName("actionNormalization")
        self.actionDimensionality_Reduction = QtWidgets.QAction(MainWindow)
        self.actionDimensionality_Reduction.setObjectName("actionDimensionality_Reduction")
        self.actionStratified_Folds = QtWidgets.QAction(MainWindow)
        self.actionStratified_Folds.setObjectName("actionStratified_Folds")
        self.actionCross_Validation = QtWidgets.QAction(MainWindow)
        self.actionCross_Validation.setObjectName("actionCross_Validation")
        self.actionTrain = QtWidgets.QAction(MainWindow)
        self.actionTrain.setObjectName("actionTrain")
        self.actionSubmodel_Blend = QtWidgets.QAction(MainWindow)
        self.actionSubmodel_Blend.setObjectName("actionSubmodel_Blend")
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("actionPredict")
        self.actionPlot = QtWidgets.QAction(MainWindow)
        self.actionPlot.setObjectName("actionPlot")
        self.actionPlot_Spectra = QtWidgets.QAction(MainWindow)
        self.actionPlot_Spectra.setObjectName("actionPlot_Spectra")
        self.actionPlot_ICA_PCA = QtWidgets.QAction(MainWindow)
        self.actionPlot_ICA_PCA.setObjectName("actionPlot_ICA_PCA")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionOpen_Workflow = QtWidgets.QAction(MainWindow)
        self.actionOpen_Workflow.setObjectName("actionOpen_Workflow")
        self.actionOn_2 = QtWidgets.QAction(MainWindow)
        self.actionOn_2.setObjectName("actionOn_2")
        self.actionOff_2 = QtWidgets.QAction(MainWindow)
        self.actionOff_2.setObjectName("actionOff_2")
        self.actionRename_Data = QtWidgets.QAction(MainWindow)
        self.actionRename_Data.setObjectName("actionRename_Data")
        self.actionQtmodern = QtWidgets.QAction(MainWindow)
        self.actionQtmodern.setObjectName("actionQtmodern")
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionOn = QtWidgets.QAction(MainWindow)
        self.actionOn.setObjectName("actionOn")
        self.actionOff = QtWidgets.QAction(MainWindow)
        self.actionOff.setObjectName("actionOff")
        self.actionBrace_yourself = QtWidgets.QAction(MainWindow)
        self.actionBrace_yourself.setObjectName("actionBrace_yourself")
        self.actionClear_Workflow = QtWidgets.QAction(MainWindow)
        self.actionClear_Workflow.setObjectName("actionClear_Workflow")
        self.actionSpectral_Derivative = QtWidgets.QAction(MainWindow)
        self.actionSpectral_Derivative.setObjectName("actionSpectral_Derivative")
        self.actionData_Box = QtWidgets.QAction(MainWindow)
        self.actionData_Box.setObjectName("actionData_Box")
        self.actionCombine_Data_Sets = QtWidgets.QAction(MainWindow)
        self.actionCombine_Data_Sets.setObjectName("actionCombine_Data_Sets")
        self.actionOutlier_Removal = QtWidgets.QAction(MainWindow)
        self.actionOutlier_Removal.setObjectName("actionOutlier_Removal")
        self.menuFile.addAction(self.actionLoad_Data)
        self.menuFile.addAction(self.actionRename_Data)
        self.menuFile.addAction(self.actionSave_Current_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSet_Output_Path)
        self.menuFile.addAction(self.actionRead_ChemCam_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_New_Workflow)
        self.menuFile.addAction(self.actionClear_Workflow)
        self.menuFile.addAction(self.actionRestore_Workflow)
        self.menuFile.addAction(self.actionSave_Current_Workflow)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuPreprocessing.addAction(self.actionRemove_Rows)
        self.menuPreprocessing.addAction(self.actionCombine_Data_Sets)
        self.menuPreprocessing.addAction(self.actionOutlier_Removal)
        self.menuPreprocessing.addAction(self.actionSplit_Data)
        self.menuPreprocessing.addAction(self.actionInterpolate)
        self.menuPreprocessing.addAction(self.actionRemove_Baseline)
        self.menuPreprocessing.addAction(self.actionApply_Mask)
        self.menuPreprocessing.addAction(self.actionPeak_Areas)
        self.menuPreprocessing.addAction(self.actionMultiply_by_Vector)
        self.menuPreprocessing.addAction(self.actionNormalization)
        self.menuPreprocessing.addAction(self.actionDimensionality_Reduction)
        self.menuPreprocessing.addAction(self.actionStratified_Folds)
        self.menuPreprocessing.addAction(self.actionSpectral_Derivative)
        self.menuRegression.addAction(self.actionCross_Validation)
        self.menuRegression.addAction(self.actionTrain)
        self.menuRegression.addAction(self.actionPredict)
        self.menuRegression.addAction(self.actionSubmodel_Blend)
        self.menuVisualization.addAction(self.actionPlot)
        self.menuVisualization.addAction(self.actionPlot_Spectra)
        self.menuVisualization.addAction(self.actionPlot_ICA_PCA)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuDark_Mode.addAction(self.actionDefault)
        self.menuDark_Mode.addAction(self.actionBrace_yourself)
        self.menuDark_Mode.addAction(self.actionQtmodern)
        self.menuDebug_Mode.addAction(self.actionOn)
        self.menuDebug_Mode.addAction(self.actionOff)
        self.menuOptions.addAction(self.menuDark_Mode.menuAction())
        self.menuOptions.addAction(self.menuDebug_Mode.menuAction())
        self.menuView.addAction(self.actionData_Box)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreprocessing.menuAction())
        self.menubar.addAction(self.menuRegression.menuAction())
        self.menubar.addAction(self.menuVisualization.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(("PYSAT Point Spectra GUI"))
        self.textBrowser.setToolTip(("<html><head/><body><p>Console window<br/>This window gives you information about your running module<br/>Errors will also show up here, if they occur</p></body></html>"))
        self.progressBar.setToolTip(("<html><head/><body><p>Your current progression.</p></body></html>"))
        self.progressBar.setFormat(("%p%"))
        self.undoModulePushButton.setToolTip(("<html><head/><body><p>Re-run your last ran module</p></body></html>"))
        self.undoModulePushButton.setText(("Re-run Module"))
        self.stopPushButton.setToolTip(("<html><head/><body><p>Completely stop the currently running module</p></body></html>"))
        self.stopPushButton.setText(("Stop Module"))
        self.deleteModulePushButton.setToolTip(("<html><head/><body><p>Delete a module that has not been ran</p></body></html>"))
        self.deleteModulePushButton.setText(("Delete Module"))
        self.okPushButton.setToolTip(("<html><head/><body><p>Press this button when you are ready to run the modules in your workflow</p></body></html>"))
        self.okPushButton.setWhatsThis(("Press this button when you\'re ready to run. (Ctrl+Enter)"))
        self.okPushButton.setText(("OK"))
        self.menuFile.setTitle(("File"))
        self.menuPreprocessing.setTitle(("Preprocessing"))
        self.menuRegression.setTitle(("Regression"))
        self.menuVisualization.setTitle(("Visualization"))
        self.menuHelp.setTitle(("Help"))
        self.menuOptions.setTitle(("Options"))
        self.menuDark_Mode.setTitle(("Theme"))
        self.menuDebug_Mode.setTitle(("Debug Mode"))
        self.menuView.setTitle(("View"))
        self.actionRead_ChemCam_Data.setText(("Read ChemCam Data"))
        self.actionLoad_Data.setText(("Load Data"))
        self.actionSet_Output_Path.setText(("Set Output Path"))
        self.actionSave_Current_Data.setText(("Save Current Data"))
        self.actionCreate_New_Workflow.setText(("Create New Workflow"))
        self.actionRestore_Workflow.setText(("Restore Workflow"))
        self.actionSave_Current_Workflow.setText(("Save Current Workflow"))
        self.actionExit.setText(("Exit"))
        self.actionRemove_Rows.setText(("Remove Rows"))
        self.actionSplit_Data.setText(("Split Data"))
        self.actionInterpolate.setText(("Interpolate"))
        self.actionRemove_Baseline.setText(("Remove Baseline"))
        self.actionApply_Mask.setText(("Apply Mask"))
        self.actionPeak_Areas.setText(("Peak Areas"))
        self.actionMultiply_by_Vector.setText(("Multiply by Vector"))
        self.actionNormalization.setText(("Normalization"))
        self.actionDimensionality_Reduction.setText(("Dimensionality Reduction"))
        self.actionStratified_Folds.setText(("Stratified Folds"))
        self.actionCross_Validation.setText(("Cross Validation"))
        self.actionTrain.setText(("Regression Train"))
        self.actionSubmodel_Blend.setText(("Blend Submodel Predictions"))
        self.actionPredict.setText(("Regression Predict"))
        self.actionPlot.setText(("Plot"))
        self.actionPlot_Spectra.setText(("Plot Spectra"))
        self.actionPlot_ICA_PCA.setText(("Plot ICA/PCA"))
        self.actionAbout.setText(("About..."))
        self.actionAbout_Qt.setText(("About Qt..."))
        self.actionOpen_Workflow.setText(("Open Workflow"))
        self.actionOn_2.setText(("On"))
        self.actionOff_2.setText(("Off"))
        self.actionRename_Data.setText(("Rename Data"))
        self.actionQtmodern.setText(("qtmodern"))
        self.actionDefault.setText(("Default"))
        self.actionOn.setText(("On"))
        self.actionOff.setText(("Off"))
        self.actionBrace_yourself.setText(("Brace yourself"))
        self.actionClear_Workflow.setText(("Clear Workflow"))
        self.actionSpectral_Derivative.setText(("Spectral Derivative"))
        self.actionData_Box.setText(("Data Box"))
        self.actionCombine_Data_Sets.setText(("Combine Data Sets"))
        self.actionOutlier_Removal.setText(("Outlier Removal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

