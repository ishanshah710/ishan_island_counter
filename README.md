# Island Counter

This Repo counts the number of islands in a 2D grid.

## File Structure
- `main.py`: Python program implementing the solution.
- `island_count_strategies`: Directory containing diff. algos for counting islands
    - `bfs.py`: BFS implementation for counting islands
- `validation.py`: contains different validation logic
- `constants.py`: contains constants used
- `test.py`: Unit tests.
- `islands.txt`: Example input file.
- `run.sh`: Shell script to build docker image and run the solution using Docker.
- `Dockerfile`: Docker configuration.
- `requirements.txt`: Python dependencies.

## How to Run
1. Build and run the Docker container:
   ```bash
   ./run.sh islands.txt

### Run all tests by: `pytest test.py`
