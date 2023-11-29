def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    f = [0] + flowerbed + [0]
    count = 0
    for i in range(1, len(f) - 1):
        if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
            count += 1
            f[i] = 1

    return count >= n
