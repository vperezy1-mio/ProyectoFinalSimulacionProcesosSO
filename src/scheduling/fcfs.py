from src.models.process import Process, ProcessState
from src.scheduling.ready_queue import ReadyQueue

class FCFSScheduler:
    def __init__(self, ready_queue: ReadyQueue):
        self.ready_queue = ready_queue
        self.current_process: Process | None = None
        self.current_time = 0


    def step(self) -> Process | None:
        """Avanza la simulacion una unidad de tiempo, para poder visualizar la simulacion rafagas en segundos"""

        #si la CPU esta libre, tomar el siguiente proceso.
        if self.current_process is None:
            self.current_process = self.ready_queue.dispatch_next()

        #No hay procesos para ejecutar.
        if self.current_process is None:
            return None

        #Los procesos que esperan acumulan timepo de espera.
        for process in self.ready_queue.get_all():
            process.waiting_time += 1


        #Ejecutar una unidad de timepo de CPU.
        process = self.current_process
        process.remaining_time -= 1
        process.elapsed_time += 1
        self.current_time += 1

        #Finalizar cuando se agota el timepo de CPU requerido.
        if process.remaining_time == 0:
            process.state = ProcessState.TERMINATED
            self.current_process = None

        return process

    def run_until_complete(self) -> None:
        """Ejecuta todos los procesos hasta vaciar la cola."""

        while self.current_process is not None or not self.ready_queue.is_empty():
            self.step()


