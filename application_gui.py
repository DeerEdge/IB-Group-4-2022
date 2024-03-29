# Import PyQt5's widgets to be used throughout the program
from random import randint

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# A class is created that holds all functions of the program
class ui_main_window(object):
    global trial_num
    trial_num = 1

    # This function setups up a basic window where widgets can be added
    def setup_window(self, main_window):
        main_window.setWindowTitle("How Temperature Affects the Rate of Reaction of Pepsin in Egg White Proteins")
        main_window.setObjectName("main_window")
        # The size of the window is specified using "resize()"
        main_window.setFixedSize(750, 550)

        # The bottom bar of a window is added using the QStatusBar widget
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        self.status_bar.showMessage(" IB Group 4 Project - Anthony (Chem),  Aarnav (Bio),  Dheeraj (CS),  JT (Bio),  and Mahika (Physics)")
        main_window.setStatusBar(self.status_bar)
        self.setup_simulation()

    def setup_simulation(self):
        global selected_temp
        global experiment_data
        global trendline_data
        global data_index

        experiment_data = [[0.440, 0.450, 0.470, 0.370, 0.331, 0.434, 0.526, 0.624, 0.654, 0.700, 0.732],
                           [0.712, 0.798, 0.890, 0.990, 1.055, 1.110, 1.140, 1.140, 1.150, 1.150, 1.150],
                           [1.210, 0.4520, 0.440, 0.4760, 0.482, 0.482, 0.512, 0.536, 0.550, 0.544, 0.530],
                           [0.212, 0.604, 0.806, 1.020, 1.180, 1.250, 1.240, 1.250, 1.300, 1.350, 1.400],
                           [0.107, 0.109, 0.113, 0.112, 0.124, 0.113, 0.114, 0.117, 0.114, 0.115, 0.113]]
        trendline_data = ["y=(1.13^-3)x+0.352", "y=(1.44^-3)x+0.809", "y=(-7.73^-4)x+0.681", "y=(3.31^-3)x+0.559", "y=(1.73^-5)x+0.111"]
        data_index = 0

        self.selected_temp_label = self.create_QLabel("main_window", "temp_label", "Selected Temperature: 33° Celsius", 486, 15, 260, 20)

        self.backdrop = QtWidgets.QGroupBox(main_window)
        self.backdrop.setGeometry(20, 30, 72, 235)
        self.backdrop.setObjectName("backdrop")

        self.proteins_component = QtWidgets.QGroupBox(main_window)
        self.proteins_component.setGeometry(43, 163, 27, 86)
        self.proteins_component.setObjectName("proteins_added")
        self.proteins_component.hide()

        self.cuvette = QtWidgets.QLabel(main_window)
        self.cuvette.setFixedSize(53, 231)
        self.cuvette.move(30, 40)
        self.cuvette.setPixmap(QtGui.QPixmap("application_data_and_graphs/cuvette.png"))
        self.cuvette.setScaledContents(True)
        self.cuvette.show()

        self.observation_label = self.create_QLabel("main_window", "observation_label", "Observations:", 114, 60, 180, 40)
        self.observation_text_box = QGroupBox(main_window)
        self.observation_text_box.setFixedSize(100, 166)
        self.observation_text_box.move(115, 94)
        self.observation_placeholder = self.create_QLabel("observation_text_box", "placeholder_text_label", "Click Through \n   Steps 1-3 ", 8, 60, 160, 40)
        self.observation1 = self.create_QLabel("observation_text_box", "observation_labels",
                                               "- Abs.  usually \n   starts \n   increasing",
                                               4, 3, 160, 60)
        self.observation2 = self.create_QLabel("observation_text_box", "observation_labels",
                                               "- White clumps \n   start forming", 4, 56, 160,
                                               40)
        self.observation3 = self.create_QLabel("observation_text_box", "observation_labels",
                                               "- Abs.  starts \n   to stabilize", 4, 92, 160,
                                               40)
        self.observation4 = self.create_QLabel("observation_text_box", "observation_labels",
                                               "- Begins \n   to separate", 4, 125, 160,
                                               40)
        self.observation1.hide()
        self.observation2.hide()
        self.observation3.hide()
        self.observation4.hide()

        self.stopwatch_label = self.create_QLabel("main_window", "stopwatch_label", "00.00.0", 340, 20, 260, 40)
        self.stopwatch_label.setFont(QFont('Arial', 30))

        self.graphed_results_label = self.create_QLabel("main_window", "graph_label", "Graphed Results: ", 20, 265, 120, 40)
        self.trendline_label = self.create_QLabel("main_window", "trendline_label", "Trendline Equation: ", 300, 265, 120, 40)
        self.input_label = self.create_QLabel("main_window", "input_label", "Enter a Time (x): ", 300, 345, 150, 40)
        self.input_line = self.create_QLineEdit("main_window", "input_line", False, 300, 380, 50, 30)
        self.input_line.textChanged.connect(self.calculate_absorbance)
        self.input_line.setEnabled(False)
        self.second_label = self.create_QLabel("main_window", "seconds_label", "Seconds", 355, 375, 150, 40)
        self.output_label = self.create_QLabel("main_window", "output_label", "Absorbance Value (y): ", 300, 405, 150, 40)
        self.output_line = self.create_QLineEdit("main_window", "output_line", True, 300, 440, 50, 30)
        self.output_line.setEnabled(False)
        self.second_label = self.create_QLabel("main_window", "unitless_label", "(Unitless)", 355, 435, 150, 40)
        self.graph_xlabel = AbsorbanceLabel(main_window)
        self.graph_xlabel.setGeometry(10, 320, 40, 100)
        self.graph_ylabel = self.create_QLabel("main_window", "axis_label", "Time (s)", 136, 474, 100, 40)
        self.placeholder_box = QGroupBox(main_window)
        self.placeholder_box.setFixedSize(237, 178)
        self.placeholder_box.move(40, 300)
        self.placeholder_text = self.create_QLabel("placeholder_box", "placeholder_text_label", "Click Through Steps 1-3 \n    to Run a Simulation", 40, 58, 160, 40)
        self.placeholder_box2 = QGroupBox(main_window)
        self.placeholder_box2.setFixedSize(158, 50)
        self.placeholder_box2.move(300, 300)
        self.placeholder_text2 = self.create_QLabel("placeholder_box2", "placeholder_text_label",
                                                   "Click Through \n  Steps 1-3 ", 36, 4, 160, 40)

        self.time_table_label = self.create_QLabel("main_window", "time_table_label", "           Time \n      (Every 30s)", 242, 54, 180, 40)
        self.absorbance_label = self.create_QLabel("main_window", "absorbance_label", "Absorbance", 366, 64, 180, 40)
        self.tableWidget = QTableWidget(main_window)
        self.tableWidget.setGeometry(228, 94, 230, 164)
        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnCount(2)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        for i in range(11):
            for j in range(2):
                TableWidgetItem = QTableWidgetItem("                         ")
                TableWidgetItem.setFlags(Qt.NoItemFlags)
                self.tableWidget.setItem(i, j, TableWidgetItem)

        self.divider_line = self.create_QFrame("main_window", "divider", "VLine", 470, 15, 1, 495)

        self.add_proteins_button = self.create_QPushButton("main_window", "add_proteins", "  1.  Add Egg White Proteins (5mL)    ", "None", 480, 65, 260, 50)
        self.add_proteins_button.clicked.connect(self.add_proteins)
        self.add_hcl_button = self.create_QPushButton("main_window", "add_hcl", "  2.  Add Hydrochrloic Acid (3mL)       ", "None ", 480, 115, 260, 50)
        self.add_hcl_button.clicked.connect(self.add_hcl)
        self.add_hcl_button.setEnabled(False)
        self.add_pepsin_and_start_button = self.create_QPushButton("main_window", "add_pepsin", "  3.  Add Pepsin (1mL) and Start       ", "None", 480, 165, 260, 50)
        self.add_pepsin_and_start_button.clicked.connect(self.add_pepsin_and_start)
        self.add_pepsin_and_start_button.setEnabled(False)
        self.end_and_log_button = self.create_QPushButton("main_window", "end_and_log", "  4.  End Simulation and Log Results ", "None", 480, 215, 260, 50)
        self.end_and_log_button.clicked.connect(self.end_and_log)
        self.end_and_log_button.setEnabled(False)
        self.another_sim_button = self.create_QPushButton("main_window", "end_and_log", "  5.  Create Another Simulation         ", "None", 480, 265, 260, 50)
        self.another_sim_button.clicked.connect(self.reset)
        self.another_sim_button.setEnabled(False)

        self.temperature_slider = QtWidgets.QSlider(main_window)
        self.temperature_slider.setGeometry(485, 30, 240, 40)
        self.temperature_slider.setOrientation(Qt.Orientation.Horizontal)
        self.temperature_slider.setMinimum(0)
        self.temperature_slider.setMaximum(4)
        self.temperature_slider.setValue(0)
        self.temperature_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.temperature_slider.setTickInterval(1)
        selected_temp = 33
        self.temperature_slider.valueChanged.connect(self.get_temp)

        self.trial_log_label = self.create_QLabel("main_window", "trail_log_label", "Trial Log:", 486, 315, 260, 30)
        self.trial_log_objects = self.create_QScrollArea("main_window", "upcoming_events_QScrollArea", "vertical_layout", 486, 345, 249, 168)
        self.trial_log = self.trial_log_objects[0]
        self.trial_log_layout = self.trial_log_objects[1]
        self.trial_log_scrollArea = self.trial_log_objects[2]

    def get_temp(self):
        global selected_temp
        selected_temp = 33 + 2 * self.temperature_slider.value()
        self.selected_temp_label.setText("Selected Temperature: " + str(selected_temp) + "° Celsius")

    def add_proteins(self):
        global data_index
        global data_index
        if self.temperature_slider.value() == 0:
            data_index = 0
        elif self.temperature_slider.value() == 1:
            data_index = 1
        elif self.temperature_slider.value() == 2:
            data_index = 2
        elif self.temperature_slider.value() == 3:
            data_index = 3
        else:
            data_index = 4
        self.proteins_component.show()
        self.add_proteins_button.setEnabled(False)
        self.temperature_slider.setEnabled(False)
        self.add_hcl_button.setEnabled(True)

    def add_hcl(self):
        self.proteins_component.setStyleSheet('QGroupBox {background-color: rgb(243, 228, 171);}')
        self.proteins_component.setGeometry(43, 113, 27, 136)
        self.add_hcl_button.setEnabled(False)
        self.add_pepsin_and_start_button.setEnabled(True)

    def add_pepsin_and_start(self):
        global timer
        self.add_pepsin_and_start_button.setEnabled(False)
        self.proteins_component.setStyleSheet('QGroupBox {background-color: rgb(243, 234, 203);}')
        self.proteins_component.setGeometry(43, 96, 27, 153)
        self.placeholder_text.setText("Running Simulation...")
        self.placeholder_text.move(53, 62)
        self.placeholder_text2.setText("Running...")
        self.placeholder_text2.move(46, 5)
        self.observation_placeholder.hide()
        self.seconds = 0
        self.minutes = 0
        self.row = 0
        self.column = 0
        self.list_index = 0
        # self.add_pepsin_and_start_button.clicked.connect(self.add_pepsin_and_start)
        timer = QtCore.QTimer(main_window)
        timer.timeout.connect(self.timer)
        timer.start(5)

    def timer(self):
        global timer
        global experiment_data
        global data_index
        self.minutes = int(self.seconds / 600)
        if self.seconds == 3001:
            timer.stop()
            self.graphed_results = QtWidgets.QLabel(main_window)
            self.graphed_results.setFixedSize(237, 178)
            self.graphed_results.move(40, 300)
            self.trendline_results = QtWidgets.QLabel(main_window)
            self.trendline_results.setFixedSize(158, 50)
            self.trendline_results.move(300, 300)
            if data_index == 0:
                self.graphed_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/33 Degrees Celsius.png"))
                self.trendline_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/33 Trendline.png"))
            elif data_index == 1:
                self.graphed_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/35 Degrees Celsius.png"))
                self.trendline_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/35 Trendline.png"))
            elif data_index == 2:
                self.graphed_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/37 Degrees Celsius.png"))
                self.trendline_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/37 Trendline.png"))
            elif data_index == 3:
                self.graphed_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/39 Degrees Celsius.png"))
                self.trendline_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/39 Trendline.png"))
            else:
                self.graphed_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/41 Degrees Celsius.png"))
                self.trendline_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/41 Trendline.png"))
            self.graphed_results.setScaledContents(True)
            self.graphed_results.show()
            self.trendline_results.setScaledContents(True)
            self.trendline_results.show()
            self.end_and_log_button.setEnabled(True)
            self.input_line.setEnabled(True)
            self.output_line.setEnabled(True)
        elif (self.seconds - self.minutes * 600) < 100:
            self.stopwatch_label.setText("0" + str(self.minutes) + "." + "0" + str(round((self.seconds / 10 - self.minutes * 60), 1)))
        else:
            self.stopwatch_label.setText("0" + str(self.minutes) + "." + str(round((self.seconds / 10 - self.minutes * 60), 1)))
        if (self.seconds == 0 or self.seconds % 300 == 0):
            if self.seconds < 1000:
                TableWidgetItemSec = QTableWidgetItem(str(int(self.seconds/10)) + "                    ")
            else:
                TableWidgetItemSec = QTableWidgetItem(str(int(self.seconds/10)) + "               ")
            # TableWidgetItemSec.setFlags(Qt.NoItemFlags)
            self.tableWidget.setItem(self.row, self.column, TableWidgetItemSec)
            TableWidgetItemVal = QTableWidgetItem(('{:.3f}'.format(experiment_data[data_index][self.list_index])) + "                 ")
            # TableWidgetItemVal.setFlags(Qt.NoItemFlags)
            self.tableWidget.setItem(self.row, self.column + 1, TableWidgetItemVal)
            self.list_index += 1
            self.row += 1

        if self.seconds == 300:
            self.observation1.show()
            for i in range(10):
                # self.molecule = self.create_QLabel("proteins_component", "molecule", "None", randint(1, 26), randint(1, 134), 4, 4)
                # self.molecule.setStyleSheet("border: 2px solid black;")
                self.molecule = self.create_QLabel("proteins_component", "molecule", "None", randint(1, 26), randint(1, 134), 4, 4)
                self.molecule.setStyleSheet("border: 2px solid black;")

        elif self.seconds == 1200:
            self.observation2.show()
        elif self.seconds == 2700:
            self.observation3.show()
        elif self.seconds == 3000:
            self.observation4.show()
        self.seconds += 1

    def end_and_log(self):
        global trial_num
        global selected_temp
        global trendline_data
        global data_index
        self.trial_object = QtWidgets.QGroupBox(self.trial_log)
        self.trial_object.setFixedSize(223, 75)
        self.trial_object.setLayout(QtWidgets.QVBoxLayout())
        self.title = QLabel(self.trial_object)
        self.title.setGeometry(10, 5, 200, 30)
        self.title.setText("Trial " + str(trial_num))
        self.temp = QLabel(self.trial_object)
        self.temp.setGeometry(10, 25, 350, 30)
        self.temp.setText("Selected Temperature: " + str(selected_temp) + "°C")
        self.trendline_equation = QLabel(self.trial_object)
        self.trendline_equation.setGeometry(10, 45, 200, 30)
        self.trendline_equation.setText("Trendline: " + str(trendline_data[data_index]))
        self.trial_log_layout.addWidget(self.trial_object)
        self.trial_log_scrollArea.setWidget(self.trial_log)
        self.trial_log_scrollArea.verticalScrollBar().setSliderPosition(0)

        trial_num += 1
        self.end_and_log_button.setEnabled(False)
        self.another_sim_button.setEnabled(True)

    def calculate_absorbance(self):
        try:
            if data_index == 0:
                absorbance = 0.00113 * int(self.input_line.text()) + 0.352
                self.output_line.setText('{:.3f}'.format((absorbance)))
            elif data_index == 1:
                absorbance = 0.00144 * int(self.input_line.text()) + 0.809
                self.output_line.setText('{:.3f}'.format((absorbance)))
            elif data_index == 2:
                absorbance = -0.000773 * int(self.input_line.text()) + 0.681
                self.output_line.setText('{:.3f}'.format((absorbance)))
            elif data_index == 3:
                absorbance = 0.00331 * int(self.input_line.text()) + 0.559
                self.output_line.setText('{:.3f}'.format((absorbance)))
            else:
                absorbance = 0.0000173 * int(self.input_line.text()) + 0.111
                self.output_line.setText('{:.3f}'.format((absorbance)))
        except:
            self.output_line.setText("")

    def reset(self):
        self.another_sim_button.setEnabled(False)
        self.temperature_slider.setEnabled(True)
        self.add_proteins_button.setEnabled(True)
        self.stopwatch_label.setText("00.00.0")
        self.proteins_component.setGeometry(43, 163, 27, 86)
        self.proteins_component.hide()
        for i in range(11):
            for j in range(2):
                TableWidgetItem = QTableWidgetItem("                         ")
                TableWidgetItem.setFlags(Qt.NoItemFlags)
                self.tableWidget.setItem(i, j, TableWidgetItem)
        self.observation1.hide()
        self.observation2.hide()
        self.observation3.hide()
        self.observation4.hide()
        self.input_line.setText("")
        self.output_line.setText("")
        self.input_line.setEnabled(False)
        self.output_line.setEnabled(False)
        self.graphed_results.deleteLater()
        self.trendline_results.deleteLater()
        self.placeholder_text.setText("Click Through Steps 1-3 \n    to Run a Simulation")
        self.placeholder_text2.setText("Click Through \n  Steps 1-3 ")
        self.placeholder_text.move(40, 58)
        self.placeholder_text2.move(36, 4)
        self.proteins_component.setStyleSheet('QGroupBox {background-color: rgb(241, 217, 131);}')

    # Widget Creation Functions
    def create_QLabel(self, container, object_name, text, x_coordinate, y_coordinate, width, length,):
        # Creates and associates QLabel to specified container
        if container == "main_window":
            self.QLabel = QtWidgets.QLabel(main_window)
        elif container == "placeholder_box":
            self.QLabel = QtWidgets.QLabel(self.placeholder_box)
        elif container == "placeholder_box2":
            self.QLabel = QtWidgets.QLabel(self.placeholder_box2)
        elif container == "observation_text_box":
            self.QLabel = QtWidgets.QLabel(self.observation_text_box)
        elif container == "proteins_component":
            self.QLabel = QtWidgets.QLabel(self.proteins_component)
        self.QLabel.setObjectName(object_name)
        if text != "None":
            self.QLabel.setText(text)
        # Geometry of QLabel is specified by the passed function parameters
        self.QLabel.setGeometry(QtCore.QRect(x_coordinate, y_coordinate, width, length))
        return self.QLabel

    def create_QLineEdit(self, container, object_name, read_only, x_coordinate, y_coordinate, width, length):
        # Creates and associates QLabel to specified container
        if container == "main_window":
            self.QLineEdit = QtWidgets.QLineEdit(main_window)
        self.QLineEdit.setObjectName(object_name)
        # user cannot type in the boxes
        self.QLineEdit.setReadOnly(read_only)
        # Geometry of QLineEdit is specified by the passed function parameters
        self.QLineEdit.setFixedSize(width, length)
        self.QLineEdit.move(x_coordinate, y_coordinate)
        return self.QLineEdit

    def create_QScrollArea(self, container, object_name, layout, x_coordinate, y_coordinate, fixed_width, min_length):
        self.scrollArea_object_container = QtWidgets.QWidget()
        if container == "main_window":
            self.QScrollArea = QtWidgets.QScrollArea(main_window)
        self.QScrollArea.setFixedWidth(fixed_width)
        self.QScrollArea.setFixedHeight(min_length)
        self.QScrollArea.move(x_coordinate, y_coordinate)
        self.QScrollArea.setWidgetResizable(True)
        self.QScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        if layout == "vertical_layout":
            self.scroll_vertical_layout = QtWidgets.QVBoxLayout(self.scrollArea_object_container)
            self.scrollArea_object_container.setLayout(self.scroll_vertical_layout)
            return [self.scrollArea_object_container, self.scroll_vertical_layout, self.QScrollArea]
        elif layout == "grid_layout":
            self.scroll_grid_layout = QtWidgets.QGridLayout(self.scrollArea_object_container)
            self.scrollArea_object_container.setLayout(self.scroll_grid_layout)
            self.QScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            return [self.scrollArea_object_container, self.scroll_grid_layout, self.QScrollArea]

    def create_QFrame(self, container, object_name, orientation, x_coordinate, y_coordinate, width, length):
        if container == "main_window":
            self.QFrame = QtWidgets.QFrame(main_window)
        self.QFrame.setObjectName(object_name)
        self.QFrame.setGeometry(QtCore.QRect(x_coordinate, y_coordinate, width, length))
        if orientation == "VLine":
            self.QFrame.setFrameShape(QtWidgets.QFrame.VLine)

    def create_QPushButton(self, container, object_name, text, icon, x_coordinate, y_coordinate, width, length):
        # Creates and associates QLabel to specified container
        if container == "login_widget_container":
            self.QPushButton = QtWidgets.QPushButton(self.login_widget_container)
        elif container == "central_widget":
            self.QPushButton = QtWidgets.QPushButton(self.central_widget)
        elif container == "main_window":
            self.QPushButton = QtWidgets.QPushButton(main_window)
        elif container == "student_profile_tab":
            self.QPushButton = QtWidgets.QPushButton(self.student_profile_tab)

        elif container == "rewards_tab":
            self.QPushButton = QtWidgets.QPushButton(self.rewards_tab)
        self.QPushButton.setObjectName(object_name)
        if text != "None":
            self.QPushButton.setText(text)
        if icon != "None":
            self.QPushButton.setIcon(QIcon(icon))
        # Geometry of QLineEdit is specified by the passed function parameters
        self.QPushButton.setFixedSize(width, length)
        self.QPushButton.move(x_coordinate, y_coordinate)
        return self.QPushButton

class AbsorbanceLabel(QWidget):
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.black)
        painter.translate(20, 100)
        painter.rotate(-90)
        painter.drawText(0, 0, "Absorbance")
        painter.end()

if __name__ == "__main__":
    import sys
    # An application is created
    app = QtWidgets.QApplication(sys.argv)
    # Read the css file and apply the stylesheet
    with open("application_styling.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    # A main window is created for the application
    main_window = QtWidgets.QMainWindow()
    # The user interface sets up the main window class
    ui = ui_main_window()
    ui.setup_window(main_window)
    main_window.show()
    sys.exit(app.exec_())