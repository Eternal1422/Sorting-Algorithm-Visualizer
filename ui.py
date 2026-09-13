import pygame

BLACK = (15, 15, 15)
WHITE = (220, 220, 220)
RED = (235, 64, 52)
GREEN = (52, 235, 122)
GRAY = (100, 100, 100)

def draw_bars(screen, arr, idx1, idx2, sorting, width, height):
    num_bars = len(arr)
    bar_width = width / num_bars

    for i, val in enumerate(arr):
        color = RED if (i == idx1 or i == idx2) else WHITE
        if not sorting:
            color = GREEN

        rect_x = i * bar_width
        rect_y = height - val
        pygame.draw.rect(screen, color, (rect_x, rect_y, bar_width - 1, val))

def draw_hud(screen, font, algo_name, status, fps, num_bars):
    line1 = f"Algo: {algo_name} | Status: {status} | Speed: {fps} FPS | Bars: {num_bars}"
    line2 = "[SPACE] Play/Pause | [R] Reset | [1] Bubble Sort | [2] Quick Sort | [3] Merge Sort | [4] Heap Sort | [UP/DOWN] Speed"

    surface1 = font.render(line1, True, GREEN if status == "RUNNING" else RED)
    surface2 = font.render(line2, True, GRAY)

    screen.blit(surface1, (15, 15))
    screen.blit(surface2, (15, 40))