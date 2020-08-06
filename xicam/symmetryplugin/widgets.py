from qtpy.QtCore import Qt
from qtpy.QtWidgets import QHBoxLayout, QLabel, QSlider, QSpinBox, QVBoxLayout, QWidget

from xicam.gui.widgets.imageviewmixins import ImageView


class LabeledSlider(QWidget):
    def __init__(self, text, *args, minimum=1, maximum=10, parent=None, **kwargs):
        super(LabeledSlider, self).__init__(parent)

        self.label = QLabel(text)
        self.slider = QSlider(*args, **kwargs)
        self.slider.setMinimum(minimum)
        self.slider.setMaximum(maximum)
        self.slider.setTickInterval(5)
        self.valuebox = QSpinBox()
        self.valuebox.setRange(minimum, maximum)
        self.valuebox.setValue(self.slider.value())
        self.slider.valueChanged.connect(self.valuebox.setValue)
        self.valuebox.valueChanged.connect(self.slider.setValue)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.valuebox)
        self.setLayout(layout)


class ImageCorrectionSliders(QWidget):
    def __init__(self, *args, **kwargs):
        super(ImageCorrectionSliders, self).__init__(*args, **kwargs)

        self.label = QLabel("Results Image Correction")
        self.blur_slider = LabeledSlider("blur", maximum=20, orientation=Qt.Horizontal)
        self.color_slider = LabeledSlider("color", maximum=20, orientation=Qt.Horizontal)
        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(self.blur_slider)
        layout.addWidget(self.color_slider)
        self.setLayout(layout)
