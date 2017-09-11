from point_spectra_gui.ui.OMP import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        params = {'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'n_nonzero_coefs': self.numOfNonZeroCoeffsSpinBox.value(),
                  'CV': self.optimizeWCrossValidationCheckBox.isChecked()}
        return (params)
