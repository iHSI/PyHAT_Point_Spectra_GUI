import numpy as np
from pysat.regression import cv
from pysat.spectral.spectral_data import spectral_data

from point_spectra_gui.functions.regressionMethods import *
from point_spectra_gui.ui.CrossValidation import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        self.regressionMethods()
        self.connectWidgets()

    def get_widget(self):
        return self.regression

    def make_regression_widget(self, alg, params=None):
        self.hideAll()
        print(alg)
        for i in range(len(self.algorithm_list) - 1):
            if alg == self.algorithm_list[i] and i > 0:
                self.alg[i - 1].setHidden(False)

    def connectWidgets(self):
        self.algorithm_list = ['Choose an algorithm',
                               'PLS',
                               'GP',
                               'OLS',
                               'OMP',
                               'Lasso',
                               'Elastic Net',
                               'Ridge',
                               'Bayesian Ridge',
                               'ARD',
                               'LARS',
                               'Lasso LARS',
                               'SVR',
                               'KRR',
                               'More to come...']
        self.setComboBox(self.regression_choosedata, self.datakeys)
        self.setComboBox(self.regression_alg_choices, self.algorithm_list)
        self.regression_alg_choices.currentIndexChanged.connect(lambda: self.make_regression_widget(self.regression_alg_choices.currentText()))
        self.regression_choosedata.activated[int].connect(lambda: self.changeComboListVars(self.regression_choosey, self.yvar_choices()))
        self.regression_choosedata.activated[int].connect(lambda: self.changeComboListVars(self.regression_choosex, self.xvar_choices()))

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        method = self.regression_alg_choices.currentText()
        datakey = self.regression_choosedata.currentText()
        xvars = [str(x.text()) for x in self.regression_choosex.selectedItems()]
        yvars = [('comp', str(y.text())) for y in self.regression_choosey.selectedItems()]
        yrange = [self.yvarmin_spin.value(), self.yvarmax_spin.value()]
        try:
            modelkey = method + ' - ' + str(yvars[0][-1]) + ' (' + str(yrange[0]) + '-' + str(yrange[1]) + ') '
        except:
            modelkey = method

        try:
            params,modelkey = self.getMethodParams(self.regression_alg_choices.currentIndex())
            print(params, modelkey)
        except:
            params = self.getMethodParams(self.regression_alg_choices.currentIndex())
            print(params)

        try:
            y = np.array(self.data[datakey].df[yvars])
            match = np.squeeze((y > yrange[0]) & (y < yrange[1]))
            data_for_cv = spectral_data(self.data[datakey].df.ix[match])
            cv_obj = cv.cv(params)
            self.data[datakey].df, self.cv_results = cv_obj.do_cv(data_for_cv.df, xcols=xvars, ycol=yvars,
                                                                  yrange=yrange, method=method)
            self.data['CV Results'] = self.cv_results
        except Exception as e:
            print(e)

    def yvar_choices(self):
        try:
            yvarchoices = self.data[self.regression_choosedata.currentText()].df['comp'].columns.values
            yvarchoices = [i for i in yvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            yvarchoices = ['No composition columns!']
        return yvarchoices

    def xvar_choices(self):
        try:
            xvarchoices = self.data[self.regression_choosedata.currentText()].df.columns.levels[0].values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices

    def hideAll(self):
        for a in self.alg:
            a.setHidden(True)

    def getMethodParams(self, index):
        return self.alg[index].function()

    def regressionMethods(self):
        self.alg = []
        list_forms = []
        list_forms.append(PLS)
        list_forms.append(GP)
        list_forms.append(OLS)
        list_forms.append(OMP)
        list_forms.append(Lasso)
        list_forms.append(ElasticNet)
        list_forms.append(Ridge)
        list_forms.append(BayesianRidge)
        list_forms.append(ARD)
        list_forms.append(LARS)
        list_forms.append(LassoLARS)
        list_forms.append(SVR)
        list_forms.append(KRR)
        for items in list_forms:
            self.alg.append(items.Ui_Form())
            self.alg[-1].setupUi(self.Form)
            self.algorithmLayout.addWidget(self.alg[-1].get_widget())
            self.alg[-1].setHidden(True)
