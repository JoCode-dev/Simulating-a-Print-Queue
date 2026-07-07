"""Simulation d'une file d'impression (FIFO) partagée dans un bureau."""

from collections import deque


class Queue:
    """File d'attente générique respectant le principe FIFO."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Ajoute un élément à la fin de la file."""
        self._items.append(item)

    def dequeue(self):
        """Retire et retourne l'élément en tête de la file."""
        if self.isEmpty():
            raise IndexError("Impossible de retirer un élément : la file est vide.")
        return self._items.popleft()

    def peek(self):
        """Retourne l'élément en tête sans le retirer."""
        if self.isEmpty():
            raise IndexError("Impossible de consulter la tête : la file est vide.")
        return self._items[0]

    def isEmpty(self):
        """Indique si la file est vide."""
        return len(self._items) == 0

    def size(self):
        """Retourne le nombre d'éléments dans la file."""
        return len(self._items)


class PrintJob:
    """Représente une tâche d'impression (nom + nombre de pages)."""

    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"{self.name} ({self.pages} page{'s' if self.pages > 1 else ''})"


class PrinterQueue:
    """Gère les tâches d'impression à l'aide d'une file FIFO."""

    def __init__(self):
        self.queue = Queue()

    def add_job(self, name, pages):
        """Ajoute une nouvelle tâche d'impression à la file."""
        job = PrintJob(name, pages)
        self.queue.enqueue(job)
        print(f"Tâche ajoutée : {job}")

    def process_job(self):
        """Traite (imprime) la prochaine tâche de la file."""
        if self.queue.isEmpty():
            print("Aucune tâche à traiter : la file est vide.")
            return None
        job = self.queue.dequeue()
        print(f"Impression en cours : {job}... Terminé.")
        return job

    def process_all(self):
        """Traite toutes les tâches restantes dans l'ordre d'arrivée."""
        if self.queue.isEmpty():
            print("Aucune tâche à traiter : la file est vide.")
            return
        while not self.queue.isEmpty():
            self.process_job()

    def print_queue(self):
        """Affiche l'état actuel de la file d'impression."""
        if self.queue.isEmpty():
            print("File d'impression : (vide)")
            return
        print(f"File d'impression ({self.queue.size()} tâche(s) en attente) :")
        for index, job in enumerate(self.queue._items, start=1):
            print(f"  {index}. {job}")


if __name__ == "__main__":
    printer = PrinterQueue()

    print("=== Ajout des tâches d'impression ===")
    printer.add_job("Alice", 3)
    printer.add_job("Bob", 1)
    printer.add_job("Charlie", 5)
    printer.add_job("Diana", 2)

    print("\n=== État de la file ===")
    printer.print_queue()

    print("\n=== Traitement de la première tâche ===")
    printer.process_job()

    print("\n=== État de la file après une impression ===")
    printer.print_queue()

    print("\n=== Traitement de toutes les tâches restantes ===")
    printer.process_all()

    print("\n=== État final de la file ===")
    printer.print_queue()
