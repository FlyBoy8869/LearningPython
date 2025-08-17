import gettext
import uuid

from PySide6.QtCore import QSize, QThreadPool
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import (
    QLayout,
    QMainWindow,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QVBoxLayout,
)

from mainwindow_ui import Ui_MainWindow
from progress_widget import ProgressWidget
from worker import Worker


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.resize(QSize(500, 100))
        self.pb_start_worker.setDefault(True)

        self.setStatusBar(QStatusBar())

        self.thread_pool = QThreadPool()
        self.setWindowTitle(
            f"QThreadPool Example - {self.thread_pool.maxThreadCount()} threads",
        )
        self.progress_bars = {}

        spacer = QSpacerItem(
            20,
            40,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding,
        )

        self.progress_bars_layout = QVBoxLayout()
        self.progress_bars_layout.setSizeConstraint(
            QLayout.SizeConstraint.SetMinAndMaxSize,
        )
        self.progress_bars_layout.addItem(spacer)
        self.frm_progress_bars_container.setLayout(self.progress_bars_layout)

        self.pb_start_worker.clicked.connect(self._start_worker)

    def _start_worker(self):
        w_id = uuid.uuid4().hex
        worker = Worker(w_id)
        worker.signals.progress.connect(self.update_progress_bar)
        worker.signals.finished.connect(self.worker_finished)

        progress_widget = ProgressWidget(w_id)
        progress_widget.show()
        self.progress_bars[w_id] = progress_widget
        n = len(self.progress_bars)
        # insert progress bars before the verticle spacer, but downward in order of creation
        self.verticalLayout_2.insertWidget(n - 1, progress_widget)

        self.thread_pool.start(worker)

        self.statusBar().showMessage(
            f"{n} {gettext.ngettext('worker', 'workers', n)} running...",
        )

    def update_progress_bar(self, w_id, value):
        self.progress_bars[w_id].progress_bar.setValue(value)

    def worker_finished(self, w_id):
        p_bar = self.progress_bars.pop(w_id)
        p_bar.deleteLater()

        n = len(self.progress_bars)
        self.statusBar().showMessage(
            (
                f"{n} {gettext.ngettext('worker', 'workers', n)} running..."
                if self.progress_bars
                else ""
            ),
        )
        print(f"worker {w_id} finished")

    def closeEvent(self, event: QCloseEvent) -> None:  # noqa: N802
        if self.progress_bars:
            return event.ignore()
        return super().closeEvent(event)
