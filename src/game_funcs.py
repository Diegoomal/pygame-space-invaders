
def detect_collision(player, enemies, score_value):
    for bullet in player.bullets[:]:
        for enemy in enemies[:]:
            if enemy.x < bullet.x < enemy.x + enemy.width and enemy.y < bullet.y < enemy.y + enemy.height:
                player.bullets.remove(bullet)
                enemies.remove(enemy)
                score_value += 1
    return score_value
