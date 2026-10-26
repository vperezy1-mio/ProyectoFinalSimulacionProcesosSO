from collections import deque
from src.models.process import Process, ProcessState

class ReadyQueue:
    def __init__(self):
        self._queue: deque[Process] = deque()
        self._queued_pids: set[int] = set()

    def enqueue(self, process: Process) -> None:
        """Agrega un proceso a la cola de listos."""
        if process.pid in self._queued_pids:
            raise ValueError("El proceso ya esta en la cola de listos.")

        if process.state not in (
            ProcessState.NEW,
            ProcessState.RUNNING,
        ):
            raise ValueError(
                f"No se puede agregar un porceso en estado "
                f"{process.state.value}."
            )

        process.state = ProcessState.READY
        self._queue.append(process)
        self._queued_pids.add(process.pid)


    def dispatch_next(self) -> Process | None:
        """Retira el primero de la cola y le asigna la CPU."""
        if not self._queue:
            return None

        process = self._queue.popleft()
        self._queued_pids.remove(process.pid)
        process.state = ProcessState.RUNNING

        return process

    def get_all(self) -> list[Process]:
        """Consulta los procesos que siguen esperando."""
        return list(self._queue)

    def is_empty(self) -> bool:
        return not self._queue

    def __len__(self) -> int:
        return len(self._queue)
    
