def count_islands(map_grid):
    rows = len(map_grid)
    cols = len(map_grid[0])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(r, c):
        visited.add((r, c))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and map_grid[nr][nc] == 'L' and (nr, nc) not in visited:
                dfs(nr, nc)

    island_count = 0
    for r in range(rows):
        for c in range(cols):
            if map_grid[r][c] == 'L' and (r, c) not in visited:
                dfs(r, c)
                island_count += 1

    return island_count

# Example usage
map1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]

map2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]

print(count_islands(map1))  # Output: 1
print(count_islands(map2))  # Output: 3


