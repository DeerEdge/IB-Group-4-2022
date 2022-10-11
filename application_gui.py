# Import PyQt5's widgets to be used throughout the program

import PyQt5
from PyQt5 import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time


# A class is created that holds all functions of the program
class ui_main_window(object):
    # This function setups up a basic window where widgets can be added
    def setup_window(self, main_window):
        main_window.setWindowTitle("How Temperature Affects the Rate of Reaction of Pepsin in Egg White Proteins")
        main_window.setObjectName("main_window")
        # The size of the window is specified using "resize()"
        main_window.setFixedSize(650, 550)

        # The bottom bar of a window is added using the QStatusBar widget
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        self.status_bar.showMessage(" IB Group 4 Project - Anthony (Chem),  Aarnav (Bio),  Dheeraj (CS),  JT (Bio),  and Mahika (Physics)")
        main_window.setStatusBar(self.status_bar)
        self.setup_simulation()

    def setup_simulation(self):
        self.selected_temp_label = self.create_QLabel("main_window", "temp_label", "Selected Temperature: ", 386, 30, 260, 30)

        frame = QtWidgets.QWidget(main_window)
        frame.resize(260,60)
        frame.move(380,50)
        frame_layout = QtWidgets.QHBoxLayout()
        frame.setLayout(frame_layout)
        self.temperature_slider = LabeledSlider(33, 41, 2, orientation=Qt.Horizontal)
        self.temperature_slider.resize(260,60)
        frame_layout.addWidget(self.temperature_slider)
        frame.show()

        self.proteins_component = QtWidgets.QGroupBox(main_window)
        self.proteins_component.setGeometry(72, 163, 28, 87)
        self.proteins_component.setObjectName("proteins_added")
        self.proteins_component.hide()

        self.stopwatch_label = self.create_QLabel("main_window", "stopwatch_label", "00.00.0", 240, 30, 260, 40)
        self.stopwatch_label.setFont(QFont('Arial', 30))

        self.cuvette = QtWidgets.QLabel(main_window)
        self.cuvette.setFixedSize(53, 231)
        self.cuvette.move(60, 40)
        self.cuvette.setPixmap(QtGui.QPixmap("application_data_and_graphs/cuvette.png"))
        self.cuvette.setScaledContents(True)
        self.cuvette.show()

        self.graphed_results = QtWidgets.QLabel(main_window)
        self.graphed_results.setFixedSize(237, 178)
        self.graphed_results.move(40, 300)
        self.graphed_results.setPixmap(QtGui.QPixmap("application_data_and_graphs/33 Degrees Celsius.png"))
        self.graphed_results.setScaledContents(True)
        self.graphed_results.show()

        self.divider_line = self.create_QFrame("main_window", "divider", "VLine", 370, 15, 1, 495)

        self.add_proteins_button = self.create_QPushButton("main_window", "add_proteins", "  1.  Add Egg White Proteins (5mL)    ", "None", 380, 110, 260, 50)
        self.add_proteins_button.clicked.connect(self.add_proteins)
        self.add_hcl_button = self.create_QPushButton("main_window", "add_hcl", "  2.  Add Hydrochrloic Acid (3mL)       ", "None ", 380, 160, 260, 50)
        self.add_hcl_button.clicked.connect(self.add_hcl)
        self.add_hcl_button.setEnabled(False)
        self.add_pepsin_and_start_button = self.create_QPushButton("main_window", "add_pepsin", "  3.  Add Pepsin (1mL) and Start       ", "None", 380, 210, 260, 50)
        self.add_pepsin_and_start_button.setEnabled(False)
        self.end_and_log_button = self.create_QPushButton("main_window", "end_and_log", "  4.  End Simulation and Log Results ", "None", 380, 260, 260, 50)
        self.end_and_log_button.setEnabled(False)

        self.trial_log_label = self.create_QLabel("main_window", "trail_log_label", "Trial Log:", 386, 315, 260, 30)
        self.trial_log_objects = self.create_QScrollArea("main_window", "upcoming_events_QScrollArea", "vertical_layout", 386, 340, 249, 168)
        self.trial_log = self.trial_log_objects[0]
        self.trial_log_layout = self.trial_log_objects[1]
        self.trial_log_scrollArea = self.trial_log_objects[2]

        for i in range(4):
            self.trial_object = QtWidgets.QGroupBox(self.trial_log)
            self.trial_object.setFixedSize(223, 80)
            self.trial_object.setLayout(QtWidgets.QVBoxLayout())
            self.text = QLabel(self.trial_object)
            self.text.setGeometry(10, 10, 100, 30)
            self.text.setText("Trial " + str(i + 1))
            self.trial_log_layout.addWidget(self.trial_object)
            i = i + 1
        self.trial_log_scrollArea.setWidget(self.trial_log)
        self.trial_log_scrollArea.verticalScrollBar().setSliderPosition(0)

    def add_proteins(self):
        self.proteins_component.show()
        self.add_proteins_button.setEnabled(False)
        self.add_hcl_button.setEnabled(True)

    def add_hcl(self):
        self.proteins_component.setGeometry(72, 113, 28, 137)
        self.add_hcl_button.setEnabled(False)
        self.add_pepsin_and_start_button.setEnabled(True)
        self.seconds = 0
        self.minutes = 0
        # self.add_pepsin_and_start_button.clicked.connect(self.add_pepsin_and_start)
        timer = QtCore.QTimer(main_window)
        timer.timeout.connect(self.add_pepsin_and_start)
        timer.start(6)


    def add_pepsin_and_start(self):
        self.minutes = int(self.seconds / 600)
        if (self.seconds - self.minutes * 600) < 100:
            self.stopwatch_label.setText("0" + str(self.minutes) + "." + "0" + str(round((self.seconds / 10 - self.minutes * 60), 1)))
        else:
            self.stopwatch_label.setText("0" + str(self.minutes) + "." + str(round((self.seconds / 10 - self.minutes * 60), 1)))
        self.seconds += 1

    # Widget Creation Functions
    def create_QCheckBox(self, container, x_coordinate, y_coordinate, width, length):
        if container == "dashboard_tab":
            self.QCheckBox = QtWidgets.QCheckBox(self.dashboard_tab)
        elif container == "upcoming_events_tab":
            self.QCheckBox = QtWidgets.QCheckBox(self.upcoming_events_tab)
        elif container == "event":
            self.QCheckBox = QtWidgets.QCheckBox(self.event_object)
        self.QCheckBox.resize(width, length)
        self.QCheckBox.move(x_coordinate, y_coordinate)
        return QCheckBox

    def create_QCalendar(self, container, x_coordinate, y_coordinate, width, length):
        if container == "upcoming_events_tab":
            self.QCalender = QtWidgets.QCalendarWidget(self.upcoming_events_tab)
        elif container == "admin_events_tab":
            self.QCalender = QtWidgets.QCalendarWidget(self.admin_events_tab)
        self.QCalender.setGeometry(x_coordinate, y_coordinate, width, length)
        return self.QCalender

    def create_QLabel(self, container, object_name, text, x_coordinate, y_coordinate, width, length,):
        # Creates and associates QLabel to specified container
        if container == "main_window":
            self.QLabel = QtWidgets.QLabel(main_window)
        self.QLabel.setObjectName(object_name)
        self.QLabel.setText(text)
        # Geometry of QLabel is specified by the passed function parameters
        self.QLabel.setGeometry(QtCore.QRect(x_coordinate, y_coordinate, width, length))
        return self.QLabel

    def create_QLineEdit(self, container, object_name, read_only, x_coordinate, y_coordinate, width, length):
        # Creates and associates QLabel to specified container
        if container == "login_widget_container":
            self.QLineEdit = QtWidgets.QLineEdit(self.login_widget_container)
        elif container == "dashboard_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.dashboard_tab)
        elif container == "admin_dashboard_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.admin_dashboard_tab)
        elif container == "upcoming_events_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.upcoming_events_tab)
        elif container == "points_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.points_tab)
        elif container == "rewards_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.rewards_tab)
        elif container == "student_profile_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.student_profile_tab)

            # Administrator
        elif container == "admin_dashboard_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.admin_dashboard_tab)
        elif container == "admin_events_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.admin_events_tab)
        elif container == "maps_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.maps_tab)
        elif container == "admin_statistics_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.admin_statistics_tab)
        elif container == "admin_student_view_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.admin_student_view_tab)
        self.QLineEdit.setObjectName(object_name)
        # user cannot type in the boxes
        self.QLineEdit.setReadOnly(read_only)
        # Geometry of QLineEdit is specified by the passed function parameters
        self.QLineEdit.setFixedSize(width, length)
        self.QLineEdit.move(x_coordinate, y_coordinate)
        return self.QLineEdit

    def create_QTextEdit(self, container, object_name, read_only, x_coordinate, y_coordinate, width, length):
        # Creates and associates QLabel to specified container
        if container == "login_widget_container":
            self.QTextEdit = QtWidgets.QTextEdit(self.login_widget_container)
        elif container == "dashboard_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.dashboard_tab)
        elif container == "admin_dashboard_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.admin_dashboard_tab)
        elif container == "upcoming_events_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.upcoming_events_tab)
        elif container == "points_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.points_tab)
        elif container == "rewards_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.rewards_tab)
        elif container == "student_profile_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.student_profile_tab)

            # Administrator
        elif container == "admin_dashboard_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.admin_dashboard_tab)
        elif container == "admin_events_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.admin_events_tab)
        elif container == "maps_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.maps_tab)
        elif container == "admin_statistics_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.admin_statistics_tab)
        elif container == "admin_student_view_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.admin_student_view_tab)
        self.QTextEdit.setObjectName(object_name)
        # user cannot type in the boxes
        self.QTextEdit.setReadOnly(read_only)
        # Geometry of QLineEdit is specified by the passed function parameters
        self.QTextEdit.setFixedSize(width, length)
        self.QTextEdit.move(x_coordinate, y_coordinate)
        self.QTextEdit.setWordWrapMode(True)

        return self.QTextEdit

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

    def create_horizontal_QwtSlider(self, container, x_coordinate, y_coordinate, width, length):
        if container == "main_window":
            self.QwtSlider = QtWidgets.QSlider(Qt.Horizontal, main_window)
        self.QSlider.setGeometry(x_coordinate, y_coordinate, width, length)
        return self.QSlider

class LabeledSlider(QtWidgets.QWidget):
    def __init__(self, minimum, maximum, interval, orientation=Qt.Horizontal,
            labels=None, parent=None):
        super(LabeledSlider, self).__init__(parent=parent)

        levels=range(minimum, maximum+interval, interval)
        if labels is not None:
            if not isinstance(labels, (tuple, list)):
                raise Exception("<labels> is a list or tuple.")
            if len(labels) != len(levels):
                raise Exception("Size of <labels> doesn't match levels.")
            self.levels=list(zip(levels,labels))
        else:
            self.levels=list(zip(levels,map(str,levels)))

        if orientation==Qt.Horizontal:
            self.layout=QtWidgets.QVBoxLayout(self)
        elif orientation==Qt.Vertical:
            self.layout=QtWidgets.QHBoxLayout(self)
        else:
            raise Exception("<orientation> wrong.")

        # gives some space to print labels
        self.left_margin=10
        self.top_margin=0
        self.right_margin=10
        self.bottom_margin=0

        self.layout.setContentsMargins(self.left_margin,self.top_margin,
                self.right_margin,self.bottom_margin)

        self.sl=QtWidgets.QSlider(orientation, self)
        self.sl.setPageStep(2)
        self.sl.setSingleStep(2)
        self.sl.setMinimum(minimum)
        self.sl.setMaximum(maximum)
        self.sl.setValue(minimum)
        if orientation==Qt.Horizontal:
            self.sl.setTickPosition(QtWidgets.QSlider.TicksBelow)
            self.sl.setMinimumWidth(100) # just to make it easier to read
            self.sl.setMinimumHeight(25)  # just to make it easier to read
        else:
            self.sl.setTickPosition(QtWidgets.QSlider.TicksLeft)
            self.sl.setMinimumHeight(10) # just to make it easier to read
        self.sl.setTickInterval(interval)

        self.layout.addWidget(self.sl)

    def paintEvent(self, e):
        super(LabeledSlider,self).paintEvent(e)

        style=self.sl.style()
        painter=QPainter(self)
        st_slider=QStyleOptionSlider()
        st_slider.initFrom(self.sl)
        st_slider.orientation=self.sl.orientation()

        length=style.pixelMetric(QStyle.PM_SliderLength, st_slider, self.sl)
        available=style.pixelMetric(QStyle.PM_SliderSpaceAvailable, st_slider, self.sl)

        for v, v_str in self.levels:

            # get the size of the label
            rect=painter.drawText(QRect(), Qt.TextDontPrint, v_str)

            if self.sl.orientation()==Qt.Horizontal:
                # I assume the offset is half the length of slider, therefore
                # + length//2
                x_loc=QStyle.sliderPositionFromValue(self.sl.minimum(),
                        self.sl.maximum(), v, available)+length//2

                # left bound of the text = center - half of text width + L_margin
                left=x_loc-rect.width()//2+self.left_margin
                bottom=self.rect().bottom()

                # enlarge margins if clipping
                if v==self.sl.minimum():
                    if left<=0:
                        self.left_margin=rect.width()//2-x_loc
                    if self.bottom_margin<=rect.height():
                        self.bottom_margin=rect.height()

                    self.layout.setContentsMargins(self.left_margin,
                            self.top_margin, self.right_margin,
                            self.bottom_margin)

                if v==self.sl.maximum() and rect.width()//2>=self.right_margin:
                    self.right_margin=rect.width()//2
                    self.layout.setContentsMargins(self.left_margin,
                            self.top_margin, self.right_margin,
                            self.bottom_margin)

            else:
                y_loc=QStyle.sliderPositionFromValue(self.sl.minimum(),
                        self.sl.maximum(), v, available, upsideDown=True)

                bottom=y_loc+length//2+rect.height()//2+self.top_margin-3
                # there is a 3 px offset that I can't attribute to any metric

                left=self.left_margin-rect.width()
                if left<=0:
                    self.left_margin=rect.width()+2
                    self.layout.setContentsMargins(self.left_margin,
                            self.top_margin, self.right_margin,
                            self.bottom_margin)

            pos=QPoint(left, bottom)
            painter.drawText(pos, v_str)

        return

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