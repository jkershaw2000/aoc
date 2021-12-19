testX = (20, 30)
testY = (-10, -5)
targetX = (139, 187)
targetY = (-148, -89)


def check_in_area(x, y, targetX, targetY):
    if targetX[0] <= x <= targetX[1] and targetY[0] <= y <= targetY[1]:
        return True
    return False


def next_velocity(vX, vY):

    return vX, vY - 1


def shoot_projectile(tx, ty, vx, vy):
    px, py = 0, 0
    max_y = 0
    while (px < max(tx) + 1 and not (vx == 0 and px < min(tx))) and not (
        px > min(tx) and py < min(ty)
    ):
        px += vx
        py += vy

        if vx < 0:
            vx += 1
        elif vx > 0:
            vx -= 1
        vy -= 1

        max_y = max(max_y, py)

        if tx[0] <= px <= tx[1] and ty[0] <= py <= ty[1]:
            return True, max_y
    return False, 0


max_height = 0
count = 0
for x in range(max(targetX) * 2):
    for y in range(min(targetY), max(targetX)):
        hit, height = shoot_projectile(targetX, targetY, x, y)
        if hit:
            count += 1
            if height > max_height:
                max_height = height

part1 = max_height
part2 = count
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
