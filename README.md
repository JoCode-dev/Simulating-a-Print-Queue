# Simulating a Print Queue

Simulation d'une file d'impression partagée dans un bureau, basée sur une structure de données **file (Queue)** respectant le principe **FIFO** (First-In-First-Out).

Plusieurs employés envoient des tâches d'impression (nom + nombre de pages) vers une imprimante partagée. Les tâches sont traitées une par une, dans l'ordre exact où elles ont été reçues.

## Structure du projet

```
.
├── print_queue.py   # Implémentation des classes et jeu de tests
└── README.md
```

## Classes

### `Queue`
File d'attente générique (FIFO) s'appuyant sur `collections.deque` pour des opérations en O(1).

| Méthode        | Description                                             |
| -------------- | ------------------------------------------------------- |
| `enqueue(item)`| Ajoute un élément à la fin de la file                   |
| `dequeue()`    | Retire et retourne l'élément en tête (erreur si vide)   |
| `peek()`       | Retourne l'élément en tête sans le retirer              |
| `isEmpty()`    | Indique si la file est vide                             |
| `size()`       | Retourne le nombre d'éléments dans la file              |

### `PrintJob`
Représente une tâche d'impression : un `name` et un nombre de `pages`.

### `PrinterQueue`
Gère les tâches d'impression à l'aide de la classe `Queue`.

| Méthode                | Description                                        |
| ---------------------- | -------------------------------------------------- |
| `add_job(name, pages)` | Ajoute une nouvelle tâche à la file                |
| `process_job()`        | Traite (imprime) la prochaine tâche                |
| `process_all()`        | Traite toutes les tâches restantes dans l'ordre    |
| `print_queue()`        | Affiche l'état actuel de la file                   |

## Utilisation

Prérequis : Python 3.

```bash
python3 print_queue.py
```

## Exemple de sortie

```
=== Ajout des tâches d'impression ===
Tâche ajoutée : Alice (3 pages)
Tâche ajoutée : Bob (1 page)
Tâche ajoutée : Charlie (5 pages)
Tâche ajoutée : Diana (2 pages)

=== État de la file ===
File d'impression (4 tâche(s) en attente) :
  1. Alice (3 pages)
  2. Bob (1 page)
  3. Charlie (5 pages)
  4. Diana (2 pages)

=== Traitement de la première tâche ===
Impression en cours : Alice (3 pages)... Terminé.
```

La tâche d'Alice est traitée en premier, ce qui illustre bien le comportement FIFO.
