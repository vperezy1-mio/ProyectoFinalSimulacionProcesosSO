from dataclasses import dataclass
from enum import Enum

class ProcessState(Enum):
    """Enum representa el estado de los procesos en el sistema"""
    NEW = "Nuevo"
    READY = "Listo"
    RUNNING = "Ejecucion"
    BLOCKED = "Bloqueado"
    TERMINATED = "Finalizado"

@dataclass
class Process:
    """Clase que representa un proceso en el sistema"""
    pid: int
    name: str
    burst_time: int

    state: ProcessState = ProcessState.NEW
    remaining_time: int = 0
    waiting_time: int = 0
    elapsed_time: int = 0

    def __post_init__(self):
        if self.burst_time <=0:
            raise ValueError("El tiempo de CPU debe de ser mayor que cero.")

        self.remaining_time = self.burst_time

    @property
    def progress(self) -> float:
        completed = self.burst_time - self.remaining_time
        return (completed / self.burst_time) * 100
    
    
