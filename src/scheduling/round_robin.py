from src.models.process import Process, ProcessState
from src.scheduling.ready_queue import ReadyQueue

class RoundRobinScheduler:
    def __init__(self, ready_queue: ReadyQueue, quantum: int = 2):
        if quantum <= 0:
            raise ValueError("El quantum debe ser mayor que cero.")

        self.ready_queue = ready_queue
        self.quantum = quantum
        self.current_process: Process | None = None
        self.quantum_used = 0
        self.current_time = 0

    def step(self) -> Process | None:
        """Avanza la simulacion ua unidad de tiempo."""

        #Si la CPU esta libre, tomar el siguiente proceso.
        if self.current_process is None:
            self.current_process = self.ready_queue.dispatch_next()
            self.quantum_used = 0

        #No hay proceso para ejecutar
        if self.current_process is None:
            return None

        #Los procesos que esperan acumulan timepo de espera.
        for process in self.ready_queue.get_all():
            process.waiting_time += 1

        #Ejecutar una unidad de tiempo.
        process = self.current_process
        process.remaining_time -= 1
        process.elapsed_time += 1
        self.quantum_used += 1
        self.current_time += 1

        #Si termino, liberar la CPU.
        if process.remaining_time == 0:
            process.state = ProcessState.TERMINATED
            self.current_process = None
            self.quantum_used = 0

        #Si agoto su turno, enviarlo al final de la cola de listos.
        elif self.quantum_used >= self.quantum:
            self.current_process = None
            self.quantum_used = 0
            self.ready_queue.enqueue(process)

        return process

    def run_until_complete(self) -> None:
        """Ejecuta los progcesos hasta vaciar la cola."""

        while (
            self.current_process is not None
            or not self.ready_queue.is_empty()
        ):
            self.step()