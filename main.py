import pygame
import random

import ui
from algorithms import bubble_sort, quick_sort, merge_sort, heap_sort

WIDTH, HEIGHT = 900, 550

ALGORITHMS = {
    pygame.K_1: (bubble_sort, "Bubble Sort"),
    pygame.K_2: (quick_sort, "Quick Sort"),
    pygame.K_3: (merge_sort, "Merge Sort"),
    pygame.K_4: (heap_sort, "Heap Sort")
}

def reset(algo_func, num_bars):
    arr = [random.randint(10, HEIGHT - 100) for _ in range(num_bars)]
    sorter = algo_func(arr)
    return arr, sorter

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    num_bars = 80
    fps = 60
    paused = False
    sorting = True

    current_algo, algo_name = ALGORITHMS[pygame.K_1]

    arr, sorter = reset(current_algo, num_bars)
    idx1, idx2 = -1, -1

    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    arr, sorter = reset(current_algo, num_bars)
                    sorting, idx1, idx2 = True, -1, -1
                elif event.key == pygame.K_UP:
                    fps = min(fps + 15, 1000)
                elif event.key == pygame.K_DOWN:
                    fps = max(fps - 15, 5)

                elif event.key in ALGORITHMS:
                    current_algo, algo_name = ALGORITHMS[event.key]
                    arr, sorter = reset(current_algo, num_bars)
                    sorting, idx1, idx2 = True, -1, -1

        if sorting and not paused:
            try:
                arr, idx1, idx2 = next(sorter)
            except StopIteration:
                sorting = False
                idx1, idx2 = -1, -1

        screen.fill(ui.BLACK)
        ui.draw_bars(screen, arr, idx1, idx2, sorting, WIDTH, HEIGHT)

        status_str = "PAUSED" if paused else ("RUNNING" if sorting else "FINISHED")
        ui.draw_hud(screen, font, algo_name, status_str, fps, num_bars)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()