from src.models.process import Process, ProcessState
from src.core.process_manager import ProcessManager
from src.scheduling.ready_queue import ReadyQueue
from src.scheduling.fcfs import FCFSScheduler
from src.scheduling.round_robin import RoundRobinScheduler

'''
def main():
    process = Process(
        pid=1,
        name="Reproductor multimedia",
        burst_time=10
    )

    print(f"PID: {process.pid}")
    print(f"Aplicacion: {process.name}")
    print(f"Estado: {process.state.value}")
    print(f"Timepo: {process.burst_time} segundos")
    print(f"Tiempo restante: {process.remaining_time} segundos")
    print(f"Progreso: {process.progress:.0f}%")
'''

'''
def main():
    manager = ProcessManager()

    # Crear algunos procesos de prueba
    process1 = manager.create_process("Navegador", 8)
    process2 = manager.create_process("Editor de texto", 5)
    process3 = manager.create_process("Reproductor multimedia", 12)

    # Mostrar los procesos registrados
    for process in manager.get_all_processes():
        print(
            f"PID = {process.pid} | "
            f"Nombre = {process.name} | "
            f"Estado = {process.state.value} | "
            f"Duración = {process.burst_time}"
        )

    # Probar la finalización de un proceso
    manager.terminate_process(process2.pid)

    print("\nDespués de finalizar el segundo proceso:")
    for process in manager.get_all_processes():
        print(f"PID = {process.pid} | Estado = {process.state.value}")

'''

'''
def main():
    manager = ProcessManager()
    ready_queue = ReadyQueue()

    #Crea los procesos
    manager.create_process("Navegador", 8)
    manager.create_process("Editor de texto", 5)
    manager.create_process("Reproductor multimedia", 12)

    #Envia los procesos a la cola de listos
    for process in manager.get_all_processes():
        ready_queue.enqueue(process)

    print("COLA DE PROCESOS LISTOS")
    for process in ready_queue.get_all():
        print(f"PID = {process.pid} | {process.name} | {process.state.value}")

    print(f"\nProcesos esperando: {len(ready_queue)}")

    #Asigna la CPU al primer proceso
    running_process = ready_queue.dispatch_next()

    print("\nPROCESO ASIGNADO A LA CPU")
    if running_process is not None:
        print(
            f"PID = {running_process.pid} | "
            f"{running_process.name} | "
            f"{running_process.state.value}"
        )

    print("\nCOLA DESPUES DE L AASIGNACION")
    for process in ready_queue.get_all():
        print(f"PID = {process.pid} | {process.name} | {process.state.value})")


    print(f"\nProcesos esperando: {len(ready_queue)}")
'''

'''
def main():
    manager = ProcessManager()
    ready_queue = ReadyQueue()

    #Crear procesos con diferentees timepos de CPU.
    manager.create_process("Navegador", 3)
    manager.create_process("Editor de texto", 2)
    manager.create_process("Reproductor multimedia", 4)

    #Enviar los procesos a la cola de listos.
    for process in manager.get_all_processes():
        ready_queue.enqueue(process)

    #Crear el planificador FCFS.
    scheduler = FCFSScheduler(ready_queue)

    print("SIMULADOR FCFS\n")

    while scheduler.current_process is not None or not ready_queue.is_empty():
        process = scheduler.step()

        if process is not None:
            print(
                f"Tiempo: {scheduler.current_time} | "
                f"PID: {process.pid} | "
                f"Proceso: {process.name} | "
                f"Restante: {process.remaining_time} | "
                f"Progreso: {process.progress:.0f}% |"
                f"Estado: {process.state.value}"
            )

    print("\nRESUMEN FINAL")
    for process in manager.get_all_processes():
        print(
            f"PID: {process.pid} | "
            f"{process.name} | "
            f"Estado: {process.state.value} | "
            f"Ejecucion: {process.elapsed_time} | "
            f"Espera: {process.waiting_time}"
        )
'''


def main():
    manager = ProcessManager()
    ready_queue = ReadyQueue()

    manager.create_process("Navegador", 3)
    manager.create_process("Editor de texto", 2)
    manager.create_process("Reproductor multimedia", 4)

    for process in manager.get_all_processes():
        ready_queue.enqueue(process)

    scheduler = RoundRobinScheduler(
        ready_queue=ready_queue,
        quantum=2,
    )

    print("SIMULACIÓN ROUND ROBIN")
    print(f"Quantum: {scheduler.quantum} segundos\n")

    while (
        scheduler.current_process is not None
        or not ready_queue.is_empty()
    ):
        process = scheduler.step()

        if process is not None:
            print(
                f"Tiempo: {scheduler.current_time} | "
                f"PID: {process.pid} | "
                f"Proceso: {process.name} | "
                f"Restante: {process.remaining_time} | "
                f"Progreso: {process.progress:.0f}% | "
                f"Estado: {process.state.value}"
            )

    print("\nRESUMEN FINAL")

    for process in manager.get_all_processes():
        print(
            f"PID: {process.pid} | "
            f"{process.name} | "
            f"Estado: {process.state.value} | "
            f"Ejecución: {process.elapsed_time} | "
            f"Espera: {process.waiting_time}"
        )


if __name__ == "__main__":
    main()




