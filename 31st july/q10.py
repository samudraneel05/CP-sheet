# place_shapes_AB C D E.py
from typing import List, Dict

def draw_grid(n: int, m: int, figures: List[str]) -> List[List[int]]:
    shapes: Dict[str, List[List[int]]] = {
        'A': [[1]],
        'B': [[1,1,1]],
        'C': [[1,1],
              [1,1]],
        'D': [[1,0],
              [1,1],
              [1,0]],
        'E': [[0,1,0],
              [1,1,1]]
    }

    # sanity checks
    for k, mask in shapes.items():
        if not mask or any(len(row) != len(mask[0]) for row in mask):
            raise ValueError(f"Invalid mask for shape {k}")

    grid = [[0] * m for _ in range(n)]

    for idx, letter in enumerate(figures):
        if letter not in shapes:
            raise ValueError(f"Unknown figure '{letter}'")
        mask = shapes[letter]
        h = len(mask)
        w = len(mask[0])

        placed = False
        # scan top-left anchors row-major (lowest row, then lowest col)
        for r in range(0, n - h + 1):
            for c in range(0, m - w + 1):
                ok = True
                for i in range(h):
                    for j in range(w):
                        if mask[i][j] and grid[r + i][c + j] != 0:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    val = idx + 1
                    for i in range(h):
                        for j in range(w):
                            if mask[i][j]:
                                grid[r + i][c + j] = val
                    placed = True
                    break
            if placed:
                break


    return grid


