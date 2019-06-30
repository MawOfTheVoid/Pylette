from PyQt5 import QtCore, QtWidgets


class Settings_window(QtWidgets.QDialog):

    def __init__(self, parent, config):

        self.functionality(parent, config)
        self.mark_up()
        self.bind_buttons()
        self.load_settings()
        # to grey out the button if they are disabled by default
        self.reduce_clicked(self.reduce_checkbox.checkState())

    def functionality(self, parent, config):
        super().__init__(parent, QtCore.Qt.WindowCloseButtonHint)

        # to hinder certain radiobuttons from interacting with each other
        self.picture_import_radios = QtWidgets.QButtonGroup()
        # because you cant add spinboxes to QtWidgets.QButtonGroup()
        self.picture_import_spin = []
        self.export_scaling_group = QtWidgets.QButtonGroup()
        self.conf = config

    def mark_up(self):
        self.resize(350, 400)
        self.setWindowTitle("Settings")

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(6)

        self.pic_import_lbl = QtWidgets.QLabel(self)
        self.pic_import_lbl.setText("Picture import settings")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pic_import_lbl.sizePolicy().hasHeightForWidth())
        self.pic_import_lbl.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.pic_import_lbl)

        self.line = QtWidgets.QFrame(self)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)

        self.reduce_checkbox = QtWidgets.QCheckBox(self)
        self.reduce_checkbox.setText("Reduce colors")
        self.horizontalLayout_2.addWidget(self.reduce_checkbox)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(40, -1, -1, -1)

        self.quantize_radio = QtWidgets.QRadioButton(self)
        self.quantize_radio.setText("Quantize")
        self.picture_import_radios.addButton(self.quantize_radio)
        self.horizontalLayout_5.addWidget(self.quantize_radio)

        self.quantize_spin = QtWidgets.QSpinBox(self)
        self.quantize_spin.setMinimum(1)
        self.quantize_spin.setValue(10)
        self.quantize_spin.setMaximum(1000000)
        self.picture_import_spin.append(self.quantize_spin)
        self.horizontalLayout_5.addWidget(self.quantize_spin)

        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(40, -1, -1, -1)

        self.maxcolors_radio = QtWidgets.QRadioButton(self)
        self.maxcolors_radio.setText("Maxcolors")
        self.picture_import_radios.addButton(self.maxcolors_radio)
        self.horizontalLayout_3.addWidget(self.maxcolors_radio)

        self.maxcolors_spin = QtWidgets.QSpinBox(self)
        self.maxcolors_spin.setMinimum(1)
        self.maxcolors_spin.setValue(10)
        self.maxcolors_spin.setMaximum(1000000)
        self.picture_import_spin.append(self.maxcolors_spin)
        self.horizontalLayout_3.addWidget(self.maxcolors_spin)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(40, -1, -1, -1)

        self.threshold_radio = QtWidgets.QRadioButton(self)
        self.threshold_radio.setText("Threshold")
        self.picture_import_radios.addButton(self.threshold_radio)
        self.horizontalLayout_4.addWidget(self.threshold_radio)

        # relates to threshold
        self.threshold_spin = QtWidgets.QSpinBox(self)
        self.threshold_spin.setMinimum(0)
        self.threshold_spin.setMaximum(100)
        self.threshold_spin.setValue(5)
        self.picture_import_spin.append(self.threshold_spin)
        self.horizontalLayout_4.addWidget(self.threshold_spin)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()

        self.export_settings_lbl = QtWidgets.QLabel(self)
        self.export_settings_lbl.setText("Export settings")
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.export_settings_lbl.setSizePolicy(sizePolicy)
        self.horizontalLayout_6.addWidget(self.export_settings_lbl)

        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLayout_6.addWidget(self.line_2)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, -1, -1, -1)

        self.alpha_checkBox = QtWidgets.QCheckBox(self)
        self.alpha_checkBox.setText("Export with Alpha Channel")
        self.horizontalLayout_7.addWidget(self.alpha_checkBox)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(20, -1, -1, -1)

        self.settings_scaling_lbl = QtWidgets.QLabel(self)
        self.settings_scaling_lbl.setText("Export Picture Scaling")
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.settings_scaling_lbl.sizePolicy().hasHeightForWidth())
        self.settings_scaling_lbl.setSizePolicy(sizePolicy)
        self.horizontalLayout_8.addWidget(self.settings_scaling_lbl)

        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLayout_8.addWidget(self.line_3)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(40, -1, -1, -1)

        self.scaling_radio = QtWidgets.QRadioButton(self)
        self.scaling_radio.setText("Scaling")
        self.export_scaling_group.addButton(self.scaling_radio)
        self.horizontalLayout_9.addWidget(self.scaling_radio)

        # relates to Scaling
        self.scaling_spin = QtWidgets.QSpinBox(self)
        self.scaling_spin.setMinimum(1)
        self.scaling_spin.setMaximum(100)
        self.horizontalLayout_9.addWidget(self.scaling_spin)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(40, -1, -1, -1)

        self.resizing_radio = QtWidgets.QRadioButton(self)
        self.resizing_radio.setText("Resizing")
        self.export_scaling_group.addButton(self.resizing_radio)
        self.horizontalLayout_10.addWidget(self.resizing_radio)

        # relates to width (left)
        self.width_spin = QtWidgets.QSpinBox(self)
        self.width_spin.setMinimum(10)
        self.width_spin.setMaximum(1000000)
        self.width_spin.setValue(800)
        self.horizontalLayout_10.addWidget(self.width_spin)

        self.X_lbl = QtWidgets.QLabel(self)
        self.X_lbl.setText("X")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.X_lbl.sizePolicy().hasHeightForWidth())
        self.X_lbl.setSizePolicy(sizePolicy)
        self.horizontalLayout_10.addWidget(self.X_lbl)

        # relates to height (right)
        self.height_spin = QtWidgets.QSpinBox(self)
        self.height_spin.setMinimum(10)
        self.height_spin.setMaximum(1000000)
        self.height_spin.setValue(600)
        self.horizontalLayout_10.addWidget(self.height_spin)

        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()

        self.reset_btn = QtWidgets.QPushButton(self)
        self.reset_btn.setText("Reset Preferences")
        self.horizontalLayout_11.addWidget(self.reset_btn)

        self.cancel_btn = QtWidgets.QPushButton(self)
        self.cancel_btn.setText("Cancel")
        self.horizontalLayout_11.addWidget(self.cancel_btn)

        self.apply_btn = QtWidgets.QPushButton(self)
        self.apply_btn.setText("Apply")
        self.apply_btn.setDefault(True)
        self.horizontalLayout_11.addWidget(self.apply_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_11)

    def bind_buttons(self):
        self.reduce_checkbox.stateChanged.connect(self.reduce_clicked)
        self.reset_btn.clicked.connect(self.reset_btn_clicked)
        self.cancel_btn.clicked.connect(self.cancel_btn_clicked)
        self.apply_btn.clicked.connect(self.apply_btn_clicked)

    def reduce_clicked(self, state):
        # state == 0 => deactivated; state == 1 or 2 => activated
        is_activated = state == 0
        for radio in self.picture_import_radios.buttons():
            radio.setDisabled(is_activated)
        for spin in self.picture_import_spin:
            spin.setDisabled(is_activated)

    def reset_btn_clicked(self, event):
        self.dict_to_window(self.conf.default_json)

    def cancel_btn_clicked(self, event):
        self.done(0)

    def apply_btn_clicked(self, event):
        settings = self.window_to_dict()
        self.conf.update(settings)
        self.done(0)

    def load_settings(self):
        settings = self.conf.get_all_settings()
        self.dict_to_window(settings)

    def dict_to_window(self, settings):
        if settings["picture_import"]["reduce_colors"] is True:
            reduce_activate = 2
        elif settings["picture_import"]["reduce_colors"] is False:
            reduce_activate = 0
        self.reduce_checkbox.setCheckState(reduce_activate)

        self.quantize_radio.setChecked(settings["picture_import"]["quantize"][0])
        self.quantize_spin.setValue(settings["picture_import"]["quantize"][1])

        self.maxcolors_radio.setChecked(settings["picture_import"]["maxcolors"][0])
        self.maxcolors_spin.setValue(settings["picture_import"]["maxcolors"][1])

        self.threshold_radio.setChecked(settings["picture_import"]["threshold"][0])
        self.threshold_spin.setValue(settings["picture_import"]["threshold"][1])

        if settings["picture_export"]["alpha"] is True:
            reduce_activate = 2
        elif settings["picture_export"]["alpha"] is False:
            reduce_activate = 0
        self.alpha_checkBox.setCheckState(reduce_activate)

        self.scaling_radio.setChecked(settings["picture_export"]["scale"][0])
        self.scaling_spin.setValue(settings["picture_export"]["scale"][1])

        self.resizing_radio.setChecked(settings["picture_export"]["resize"][0])
        self.width_spin.setValue(settings["picture_export"]["resize"][1])
        self.height_spin.setValue(settings["picture_export"]["resize"][2])

    def window_to_dict(self):
        settings = self.conf.get_all_settings()
        activate = self.reduce_checkbox.checkState()
        if activate == 0:
            activate = False
        elif activate >= 1:
            activate = True
        settings["picture_import"]["reduce_colors"] = activate

        truth = self.quantize_radio.isChecked()
        value = self.quantize_spin.value()
        settings["picture_import"]["quantize"] = [truth, value]

        truth = self.threshold_radio.isChecked()
        value = self.threshold_spin.value()
        settings["picture_import"]["threshold"] = [truth, value]

        activate = self.alpha_checkBox.checkState()
        if activate == 0:
            activate = False
        elif activate >= 1:
            activate = True
        settings["picture_export"]["alpha"] = activate

        truth = self.scaling_radio.isChecked()
        value = self.scaling_spin.value()
        settings["picture_export"]["scale"] = [truth, value]

        truth = self.resizing_radio.isChecked()
        width = self.width_spin.value()
        height = self.height_spin.value()
        settings["picture_export"]["resize"] = [truth, width, height]

        return settings
