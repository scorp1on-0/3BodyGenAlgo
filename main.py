from statistics import geometric_mean

import pygame as pg
import math
from random import uniform
def r():
    return uniform(-1, 1)
pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("3 Body Simulation")
font = pg.font.Font(None, 74)

clock = pg.time.Clock()
FPS = 120000/1
crash = False

def distance(bd1, bd2):
    dist = math.sqrt((bd1.centerx - bd2.centerx)**2 + (bd1.centery - bd2.centery)**2)
    if dist < 40: return 0
    return dist


body1 = pg.draw.circle(screen, (255, 0, 0), (r() * 100, r() * 100), 20)
velocity1 = pg.math.Vector2(r(), r())
body2 = pg.draw.circle(screen, (0, 255, 0), (300, 330), 20)
velocity2 = pg.math.Vector2(0.001, 0)
body3 = pg.draw.circle(screen, (0, 0, 255), (700, 200), 20)
velocity3 = pg.math.Vector2(0, -0.0011)
i = 0
SPEED = 10**3
oob = False
running = True
simulation = 0
crashes = 0
stable_configurations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
stable_configurations = [-0.6050246669166366, -0.12073441388946173, 0.07058792810907694, -0.7005773813899745, 0.8944023879666855, 0.6756393263972876, 0.385009617269368, 0.8347017856463376, 0.2955953467922173, 0.19688268612813928, 0.65197587125789, 0.3175860447080738]
generation: int = 18
nextgen = True
iterations = 0
diff = 2
maxgen = generation

while running:
    simulation += 1
    rands = []
    for rand in range(6):
        rands.append(uniform(-1, 1))
    for rand in range(6):
        rands.append(uniform(0, 1))
    if generation > 1:
        # print(stable_configurations)
        # print(f"Generation: {generation}")
        for i in range(6):
            rands[i] = stable_configurations[i] + (rands[i]/(10**(generation/4)))
        for i in range(6):
            rands[i+6] = stable_configurations[i+6] + (rands[i+6]/(10**(generation/4)))
        nextgen = False

    # rands = [-0.6731700953062449, 0.0909075589408499, -0.1610956320219894, -0.3724372699133158, 0.2973989304137983, -0.4722279365488633, 0.11989382128350401, 0.5601601038973282, 0.6012472122035754, 0.7849893153451774, 0.3457655073657808, 0.02492323383280315]
    body1 = pg.draw.circle(screen, (255, 0, 0), (rands[6]*1000, rands[7]*1000), 20)
    velocity1 = pg.math.Vector2(rands[0]/1000, rands[1]/1000)
    body2 = pg.draw.circle(screen, (0, 255, 0), (rands[8]*1000, rands[9]*1000), 20)
    velocity2 = pg.math.Vector2(rands[2]/1000, rands[3]/1000)
    body3 = pg.draw.circle(screen, (0, 0, 255), (rands[10]*1000, rands[11]*1000), 20)
    velocity3 = pg.math.Vector2(rands[4]/1000, rands[5]/1000)
    for i in range(2000+generation*100):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break

        screen.fill((0, 0, 0))
        text = font.render(f"Gen {generation}. Iter: {iterations}", True, (255, 255, 255))
        screen.blit(text, (20, 20))
        body1 = pg.draw.circle(screen, (255, 0, 0), body1.center, 20)
        # velocity1.x += (body2.centerx + body3.centerx)/2 - body1.centerx
        try:
            velocity1.x += (body2.centerx - body1.centerx) /(distance(body1, body2)**3)/2 + (body3.centerx - body1.centerx)/(distance(body1, body3)**3)/2
            velocity1.y += (body2.centery - body1.centery) /(distance(body1, body2)**3)/2 + (body3.centery - body1.centery)/(distance(body1, body3)**3)/2
            body1.center += velocity1 * SPEED
            veline1 = pg.draw.line(screen, (255, 255, 255), body1.center, (body1.centerx + 10000*velocity1.x, body1.centery + 10000*velocity1.y), width=2)

            body2 = pg.draw.circle(screen, (0, 255, 0), body2.center, 20)
            velocity2.x += (body1.centerx - body2.centerx) /(distance(body1, body2)**3)/2 + (body3.centerx - body2.centerx)/(distance(body3, body2)**3)/2
            velocity2.y += (body1.centery - body2.centery) /(distance(body1, body2)**3)/2 + (body3.centery - body2.centery)/(distance(body3, body2)**3)/2
            body2.center += velocity2 * SPEED
            veline2 = pg.draw.line(screen, (255, 255, 255), body2.center,
                                   (body2.centerx + 10000 * velocity2.x, body2.centery + 10000 * velocity2.y), width=2)

            body3 = pg.draw.circle(screen, (0, 0, 255), body3.center, 20)
            velocity3.x += (body1.centerx - body3.centerx) /(distance(body1, body3)**3)/2 + (body2.centerx - body3.centerx)/(distance(body3, body2)**3)/2
            velocity3.y += (body1.centery - body3.centery) /(distance(body1, body3)**3)/2 + (body2.centery - body3.centery)/(distance(body3, body2)**3)/2
            body3.center += velocity3 * SPEED
            veline3 = pg.draw.line(screen, (255, 255, 255), body3.center,
                                   (body3.centerx + 10000 * velocity3.x, body3.centery + 10000 * velocity3.y), width=2)
        except:
            # print(f"Division by zero. Planets crashed!")
            crash = True
            crashes += 1
            break
        if generation > 0: pg.display.flip()

        clock.tick(FPS*10/generation/100)
        bodies = [body1, body2, body3]
        for body in bodies:
            if max(abs(body.centerx), abs(body.centery)) > 980 or min(abs(body.centerx), abs(body.centery)) < 20:
                # print("break because out of bounds:")
                oob = False
                # print(max(abs(body.centerx), abs(body.centery)))
                break
        else: continue
        break
    # print(oob, crash)
    for body in bodies:
        if max(abs(body.centerx), abs(body.centery)) > 980 or min(abs(body.centerx), abs(body.centery)) < 20:
            # print(max(abs(body.centerx), abs(body.centery)))
            oob = False
            iterations += 1
    if oob == False and crash == False:
        # print(max(abs(body.centerx), abs(body.centery)))
        print(f"Possible stable configuration at sim {simulation}: {rands}")
        print(f"Planet crashes: {crashes}")
        stable_configurations = rands
        # stable_configurations.append(rands)
        nextgen = True
        print(f"Generation: {generation}")
        generation += 1
        iterations = 0
        if generation > maxgen: maxgen = generation
    if iterations > 5:
        if maxgen + 1 == generation: diff = 1
        iterations = 0
        generation = maxgen - diff
        if generation <= 0: generation = 1
        diff+=1
    crash = False
    oob = False
pg.quit()
