from typing import List, Dict

def place_figures_on_grid(n: int, m: int,
                          figures: List[str],
                          shapes: Dict[str, List[List[int]]]) -> List[List[int]]:
    """
    n, m: grid size (rows, cols)
    figures: list of letters representing figures to place, in order
    shapes: dict mapping letter -> 2D mask (list of lists) with 1 for filled cell, 0 for empty
    
    Returns grid as list of list of ints, with 0 for empty and k for cells occupied by
    the k-th figure (1-based).
    """
    # initialize grid
    grid = [[0] * m for _ in range(n)]

    for idx, letter in enumerate(figures):
        if letter not in shapes:
            raise ValueError(f"No shape provided for figure '{letter}'")

        mask = shapes[letter]
        h = len(mask)
        if h == 0:
            raise ValueError(f"Shape for '{letter}' is empty")
        w = len(mask[0])
        # sanity: ensure mask is rectangular
        for row in mask:
            if len(row) != w:
                raise ValueError(f"Non-rectangular mask for '{letter}'")

        placement_found = False
        best_r = None
        best_c = None

        # iterate all possible top-left placements (row-major order ensures smallest row, then smallest col)
        for r in range(0, n - h + 1):
            for c in range(0, m - w + 1):
                ok = True
                # check overlap and that mask's filled cells fit into zeros
                for i in range(h):
                    for j in range(w):
                        if mask[i][j]:
                            if grid[r + i][c + j] != 0:
                                ok = False
                                break
                    if not ok:
                        break
                if ok:
                    best_r, best_c = r, c
                    placement_found = True
                    # Because we scan rows then cols, this is the smallest-row, smallest-col candidate
                    break
            if placement_found:
                break

        if not placement_found:
            # The problem statement guarantees all figures fit; raise an error if not.
            raise RuntimeError(f"Cannot place figure '{letter}' (index {idx}) on grid")

        # place shape with value = idx+1
        val = idx + 1
        for i in range(h):
            for j in range(w):
                if mask[i][j]:
                    grid[best_r + i][best_c + j] = val

    return grid



def pretty_print(grid: List[List[int]]):
    for row in grid:
        print(row)
    print()
    for row in grid:
        print("".join(str(cell) if cell != 0 else "." for cell in row))

if __name__ == "__main__":
    # example shapes: 'e' as described and an 'i' vertical bar
    shapes = {
        'e': [
            [0,1,0],
            [1,1,1]
        ],
        'i': [
            [1],
            [1],
            [1]
        ]
    }

    # grid size and figures to place (in order)
    n, m = 4, 4
    figures = ['D', 'B', 'A', 'C']  # will place first 'e' (value 1), then second 'e' (2), then 'i' (3)

    grid = place_figures_on_grid(n, m, figures, shapes)
    pretty_print(grid)