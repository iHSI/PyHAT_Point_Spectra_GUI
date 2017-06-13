from point_spectra_gui.gui_utils import make_combobox,make_listwidget
from point_spectra_gui.ui_modules.Error_ import error_print
from PyQt5 import QtGui, QtCore, QtWidgets
import numpy as np
import inspect


class plot_spectra_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list):
        self.arg_list=arg_list
        self.kw_list=kw_list
        self.pysat_fun = pysat_fun
        self.module_layout = module_layout
        self.ui_id = None
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, self.ui_id)
        self.plot_spect_ui()
        self.set_plot_spectra_parameters()
        self.get_plot_spectra_parameters()
        self.pysat_fun.set_greyed_modules(self.plot_spect)

    def get_plot_spectra_parameters(self):
        datakey = self.choosedata.currentText()

        col = self.col_choices.currentText()
        row = [str(x.text()) for x in self.chooserows.selectedItems()]
        try:
            row=row[0]
        except:
            row=''
        row_bool=[]
        try:
            row_count=self.chooserows.findItems(row,QtCore.Qt.MatchExactly)
            for i in row_count:
                row_bool.append(i.isSelected())
        except:
            pass
        figname = self.figname_text.text()
        title = self.plot_spect_title_text.text()
        figfile = self.file_text.text()
        color = self.color_choices.currentText()
        alpha = self.alpha_spin.value()
        linewidth=self.width_spin.value()

        if color == 'Red':
            color = [1, 0, 0, alpha]
        elif color == 'Green':
            color = [0, 1, 0, alpha]
        elif color == 'Blue':
            color = [0, 0, 1, alpha]
        elif color == 'Cyan':
            color = [0, 1, 1, alpha]
        elif color == 'Yellow':
            color = [1, 1, 0, alpha]
        elif color == 'Magenta':
            color = [1, 0, 1, alpha]
        elif color == 'Black':
            color = [0, 0, 0, alpha]
        else:
            color = [0, 0, 0, alpha]

        line = self.line_choices.currentText()
        if line == 'No Line':
            linestyle = 'None'
        elif line == 'Line':
            linestyle = '-'
        elif line == 'Dashed Line':
            linestyle = '--'
        elif line == 'Dotted Line':
            linestyle = ':'
        else:
            linestyle = '-'

        alpha=self.alpha_spin.value()
        if row_bool.__len__()>1:
            lbl=row+' - '+str(np.where(row_bool)[0][0]+1)
        else:
            lbl=row
        xmin=self.xmin_spin.value()
        xmax=self.xmax_spin.value()
        xrange=[xmin,xmax]

        args = [datakey, row]
        kws = {'col':col,
               'figname': figname,
               'title': title,
               'figfile': figfile,
               'color': color,
               'linestyle': linestyle,
               'alpha':alpha,
               'lbl':lbl,
               'linewidth':linewidth,
               'row_bool':row_bool,
               'xrange':xrange}

        ui_list = "do_plot_spect"
        fun_list = "do_plot_spect"
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, self.ui_id)

    def set_plot_spectra_parameters(self):
        if self.arg_list is not None:
            datakey=self.arg_list[0]
            self.choosedata.setCurrentIndex(self.choosedata.findText(datakey))
            figname=self.kw_list['figname']
            self.figname_text.setText(figname)
            title=self.kw_list['title']
            self.plot_spect_title_text.setText(title)
            col=self.kw_list['col']
            self.col_choices.setCurrentIndex(self.col_choices.findText(col))
            row=self.arg_list[1]
            row_bool=self.kw_list['row_bool']
            items=self.chooserows.findItems(row, QtCore.Qt.MatchExactly)
            for i,item in enumerate(items):
                if row_bool[i] is True:
                    item.setSelected(True)
            color=self.kw_list['color']
            alpha=self.kw_list['alpha']
            if color == [1, 0, 0, alpha]:
                color = 'Red'
            elif color == [0, 1, 0, alpha]:
                color = 'Green'
            elif color == [0, 0, 1, alpha]:
                color = 'Blue'
            elif color == [0, 1, 1, alpha]:
                color = 'Cyan'
            elif color == [1, 1, 0, alpha]:
                color = 'Yellow'
            elif color == [1, 0, 1, alpha]:
                color = 'Magenta'
            elif color == [0, 0, 0, alpha]:
                color = 'Black'
            self.color_choices.setCurrentIndex(self.color_choices.findText(color))

            linestyle=self.kw_list['linestyle']
            if linestyle == '-':
                line = 'Line'
            elif linestyle == '--':
                line = 'Dashed Line'
            elif linestyle == ':':
                line = 'Dotted Line'
            else:
                line = 'Line'
            self.line_choices.setCurrentIndex(self.line_choices.findText(line))

            figfile=self.kw_list['figfile']
            self.file_text.setText(figfile)

            self.width_spin.setValue(self.kw_list['linewidth'])
            self.xmin_spin.setValue(self.kw_list['xrange'][0])

            self.xmax_spin.setValue(self.kw_list['xrange'][1])

    def plot_spect_ui(self):
        self.plot_spect = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plot_spect.setFont(font)
        self.plot_spect.setObjectName(("plot"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.plot_spect)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(("verticalLayout"))
        self.choosedata_flayout = QtWidgets.QFormLayout()
        self.choosedata_flayout.setContentsMargins(11, 11, 11, 11)
        self.choosedata_flayout.setSpacing(6)
        self.choosedata_flayout.setObjectName(("choosedata_flayout"))
        self.choosedata_label = QtWidgets.QLabel(self.plot_spect)
        self.choosedata_label.setObjectName(("choosedata_label"))
        self.choosedata_flayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.choosedata_label)

        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No Data has been loaded')
            datachoices = ['No data has been loaded!']
        self.choosedata = make_combobox(datachoices)

        self.choosedata.setIconSize(QtCore.QSize(50, 20))
        self.choosedata.setObjectName(("choosedata"))
        self.choosedata_flayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.choosedata)
        self.figname_label = QtWidgets.QLabel(self.plot_spect)
        self.figname_label.setObjectName(("figname_label"))
        self.choosedata_flayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.figname_label)
        self.figname_text = QtWidgets.QLineEdit(self.plot_spect)
        self.figname_text.setObjectName(("figname_text"))
        self.choosedata_flayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.figname_text)
        self.plot_spect_title_label = QtWidgets.QLabel(self.plot_spect)
        self.plot_spect_title_label.setObjectName(("plot_title_label"))
        self.choosedata_flayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.plot_spect_title_label)
        self.plot_spect_title_text = QtWidgets.QLineEdit(self.plot_spect)
        self.plot_spect_title_text.setEnabled(True)
        self.plot_spect_title_text.setObjectName(("plot_title_text"))
        self.choosedata_flayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plot_spect_title_text)
        self.verticalLayout.addLayout(self.choosedata_flayout)

        self.choosecol_flayout = QtWidgets.QFormLayout()
        self.choosecol_flayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.choosecol_flayout.setContentsMargins(11, 11, 11, 11)
        self.choosecol_flayout.setSpacing(6)
        self.choosecol_flayout.setObjectName(("choosecol_flayout"))
        self.choosecol_label = QtWidgets.QLabel(self.plot_spect)
        self.choosecol_label.setObjectName(("choosecol_label"))
        self.choosecol_flayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.choosecol_label)
        self.col_choices = make_combobox([''])
        self.plot_spect_change_vars(self.col_choices)
        self.col_choices.setObjectName(("col_choices"))
        self.choosecol_flayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.col_choices)
        self.chooserows_label=QtWidgets.QLabel(self.plot_spect)
        self.choosecol_flayout.setWidget(1,QtWidgets.QFormLayout.LabelRole,self.chooserows_label)
        try:
            rowchoices = self.pysat_fun.data[self.choosedata.currentText()].df[('meta',self.col_choices.currentText())]
            rowchoices=rowchoices.fillna('-')
        except:
            rowchoices = ['None']
        self.chooserows = make_listwidget(rowchoices)
        #self.chooserows.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.choosecol_flayout.setWidget(1,QtWidgets.QFormLayout.FieldRole,self.chooserows)
        self.verticalLayout.addLayout(self.choosecol_flayout)

        self.xlimits_hlayout = QtWidgets.QHBoxLayout()
        self.xmin_label = QtWidgets.QLabel(self.plot_spect)
        self.xmin_label.setText('Min:')
        self.xlimits_hlayout.addWidget(self.xmin_label)
        self.xmin_spin = QtWidgets.QDoubleSpinBox()
        # TODO: eventually we may want the ability to handle values outside 0-100 for regressions not dealing with wt.%
        self.xmin_spin.setMaximum(99999)
        self.xmin_spin.setMinimum(0)
        self.xmin_spin.setValue(min(self.pysat_fun.data[self.choosedata.currentText()].df['wvl'].columns.values))
        self.xlimits_hlayout.addWidget(self.xmin_label)
        self.xlimits_hlayout.addWidget(self.xmin_spin)

        self.xmax_label = QtWidgets.QLabel(self.plot_spect)
        self.xmax_label.setText('Max:')
        self.xlimits_hlayout.addWidget(self.xmax_label)
        self.xmax_spin = QtWidgets.QDoubleSpinBox()
        self.xmax_spin.setMaximum(99999)
        self.xmax_spin.setMinimum(0)
        self.xmax_spin.setValue(max(self.pysat_fun.data[self.choosedata.currentText()].df['wvl'].columns.values))
        self.xlimits_hlayout.addWidget(self.xmax_label)
        self.xlimits_hlayout.addWidget(self.xmax_spin)
        self.verticalLayout.addLayout(self.xlimits_hlayout)


        self.scatter_chooseline_flayout = QtWidgets.QFormLayout()
        self.scatter_chooseline_flayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.scatter_chooseline_flayout.setContentsMargins(11, 11, 11, 11)
        self.scatter_chooseline_flayout.setSpacing(6)
        self.scatter_chooseline_flayout.setObjectName(("scatter_chooseline_flayout"))
        self.color_label = QtWidgets.QLabel(self.plot_spect)
        self.color_label.setObjectName(("color_label"))
        self.scatter_chooseline_flayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.color_label)
        self.color_choices = QtWidgets.QComboBox(self.plot_spect)
        self.color_choices.setIconSize(QtCore.QSize(50, 20))
        self.color_choices.setObjectName(("color_choices"))
        self.scatter_chooseline_flayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.color_choices)
        self.line_label = QtWidgets.QLabel(self.plot_spect)
        self.line_label.setObjectName(("line_label"))
        self.scatter_chooseline_flayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.line_label)
        self.line_choices = QtWidgets.QComboBox(self.plot_spect)
        self.line_choices.setIconSize(QtCore.QSize(50, 20))
        self.line_choices.setObjectName(("line_choices"))
        self.scatter_chooseline_flayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_choices)
        self.file_label = QtWidgets.QLabel(self.plot_spect)
        self.file_label.setObjectName(("file_label"))
        self.scatter_chooseline_flayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.file_label)
        self.file_text = QtWidgets.QLineEdit(self.plot_spect)
        self.file_text.setObjectName(("file_text"))
        self.scatter_chooseline_flayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.file_text)

        self.alpha_label = QtWidgets.QLabel(self.plot_spect)
        self.alpha_label.setObjectName(("alpha_label"))
        self.scatter_chooseline_flayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alpha_label)
        self.alpha_spin = QtWidgets.QDoubleSpinBox(self.plot_spect)
        self.alpha_spin.setObjectName(("alpha_spin"))
        self.alpha_spin.setRange(0, 1)
        self.alpha_spin.setValue(1.0)
        self.alpha_spin.setSingleStep(0.1)
        self.alpha_spin.setObjectName(("alpha_spin"))
        self.scatter_chooseline_flayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.alpha_spin)

        self.width_label = QtWidgets.QLabel(self.plot_spect)
        self.width_label.setObjectName(("width_label"))
        self.scatter_chooseline_flayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.width_label)
        self.width_spin = QtWidgets.QDoubleSpinBox(self.plot_spect)
        self.width_spin.setObjectName(("width_spin"))
        self.width_spin.setRange(0, 10)
        self.width_spin.setValue(0.5)
        self.width_spin.setSingleStep(0.05)
        self.width_spin.setObjectName(("width_spin"))
        self.scatter_chooseline_flayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.width_spin)

        self.verticalLayout.addLayout(self.scatter_chooseline_flayout)
        self.module_layout.addWidget(self.plot_spect)

        self.plot_spect.setTitle("Scatter Plot")
        self.choosedata_label.setText("Choose data: ")
        self.figname_label.setText("Figure name:")
        self.plot_spect_title_label.setText("Plot Title: ")
        self.choosecol_label.setText("Choose column:")
        self.chooserows_label.setText("Choose row(s):")
        self.color_label.setText("Color:")
        self.color_choices.addItem(("Red"))
        self.color_choices.addItem(("Green"))
        self.color_choices.addItem(("Blue"))
        self.color_choices.addItem(("Cyan"))
        self.color_choices.addItem(("Yellow"))
        self.color_choices.addItem(("Magenta"))
        self.color_choices.addItem(("Black"))
        self.line_label.setText("Line:")
        self.line_choices.addItem("Line")
        self.line_choices.addItem("Dashed Line")
        self.line_choices.addItem("Dotted Line")
        self.file_label.setText("Plot Filename:")
        self.alpha_label.setText("Alpha:")
        self.width_label.setText("Line width:")

        self.plot_spect.setTitle("Plot Spectra")
        self.choosedata.activated[int].connect(lambda: self.plot_spect_change_vars(self.col_choices))
        self.col_choices.activated[int].connect(lambda: self.plot_spect_update_list(self.chooserows))
        self.choosedata.currentTextChanged.connect(lambda: self.get_plot_spectra_parameters())
        self.chooserows.itemSelectionChanged.connect(lambda: self.get_plot_spectra_parameters())
        self.col_choices.currentTextChanged.connect(lambda: self.get_plot_spectra_parameters())
        self.plot_spect_title_text.textChanged.connect(lambda: self.get_plot_spectra_parameters())
        self.figname_text.textChanged.connect(lambda: self.get_plot_spectra_parameters())
        self.alpha_spin.valueChanged.connect(lambda: self.get_plot_spectra_parameters())
        self.color_choices.currentTextChanged.connect(lambda: self.get_plot_spectra_parameters())
        self.file_text.textChanged.connect(lambda: self.get_plot_spectra_parameters())
        self.line_choices.currentTextChanged.connect(lambda: self.get_plot_spectra_parameters())
        self.xmin_spin.valueChanged.connect(lambda: self.get_plot_spectra_parameters())
        self.xmax_spin.valueChanged.connect(lambda: self.get_plot_spectra_parameters())


    def plot_spect_update_list(self,obj):
        obj.clear()
        rowchoices = self.pysat_fun.data[self.choosedata.currentText()].df[('meta', self.col_choices.currentText())]
        rowchoices = rowchoices.fillna('-')
        #rowchoices = np.unique(rowchoices)
        rowchoices=[str(x) for x in rowchoices]
        for i in rowchoices:
            obj.addItem(i)

    def plot_spect_change_vars(self, obj):
        obj.clear()
        try:
            self.vars_level0 = self.pysat_fun.data[self.choosedata.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.pysat_fun.data[self.choosedata.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = self.vars_level1[self.vars_level0 == 'meta']
            self.vars_level0 = self.vars_level0[self.vars_level0 != 'meta']

            try:
                self.vars_level0 = [i for i in self.vars_level0 if
                                    'Unnamed' not in str(i)]  # remove unnamed columns from choices
            except:
                pass
            try:
                self.vars_level1 = [i for i in self.vars_level1 if
                                    'Unnamed' not in str(i)]  # remove unnamed columns from choices
            except:
                pass
            choices = self.vars_level1

        except:
            try:
                choices = self.pysat_fun.data[self.choosedata.currentText()].columns.values
            except:
                choices = ['No valid choices']
        for i in choices:
            obj.addItem(str(i))

    def get_minmax(self, objmin, objmax, var):
        try:
            varind = self.vars_level1.index(var)
            vartuple = (self.vars_level0[varind], self.vars_level1[varind])
            vardata = self.pysat_fun.data[self.choosedata.currentText()].df[vartuple]
        except:
            try:
                vardata = self.pysat_fun.data[self.choosedata.currentText()][var]
            except:
                vardata = [0, 0]
        try:
            varmin = float(np.min(vardata))
            varmax = float(np.max(vardata))
            objmin.setValue(varmin)
            objmax.setValue(varmax)
        except:
            objmin.setValue(0)
            objmax.setValue(1)