import random
import time

from PySide6.QtCore import QObject, QRunnable, Signal

CYCLES = 1000


class WorkerSignals(QObject):
    progress = Signal(str, int)
    finished = Signal(str)


class Worker(QRunnable):
    def __init__(self, w_id) -> None:
        super().__init__()
        self.signals = WorkerSignals()

        self.w_id = w_id

    def run(self):
        sleep_time = random.random() / 100
        for n in range(1, CYCLES + 1):
            self.signals.progress.emit(self.w_id, n / CYCLES * 100)
            time.sleep(sleep_time)

        self.signals.finished.emit(self.w_id)
