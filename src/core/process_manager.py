from src.models.process import Process, ProcessState

class ProcessManager:
    def __init__(self):
        self._next_pid = 1
        self._processes: dict[int, Process] = {}

    def create_process(self, name: str, burst_time: int) ->Process:
        """Crea n procesos, le asigna PID y lo registra."""
        process = Process(
            pid=self._next_pid,
            name=name,
            burst_time=burst_time,
        )

        self._processes[process.pid] = process
        self._next_pid += 1

        return process

    def get_process(self, pid: int) -> Process | None:
        """Busca un proceso por su PID"""
        return self._processes.get(pid)

    def get_all_processes(self) -> list[Process]:
        """Devuelve los procesos registrados, ordenados por PID."""
        return list(self._processes.values())

    def terminate_process(self, pid: int) -> bool:
        """Marca un proceso como finalizado si existe."""
        process = self.get_process(pid)

        if process is None:
            return False

        process.state = ProcessState.TERMINATED
        process.remaining_time = 0 

        return True