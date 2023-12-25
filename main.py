import pygame, sys, os

# Initialize Pygame
pygame.init()
# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cookie clicker game")

score = 0
multiplier = 1
cookies_per_sec = 0
black = (0, 0, 0)
white = (255, 255, 255)
brown = (102, 51, 0)

font = pygame.font.SysFont("comicsansms", 46)
font2 = pygame.font.SysFont("comicsansms", 20)

cookies_font = font
cookie_render = cookies_font.render(
    str(score), True, white
)  # Thank you for watching!!!!!
cookies_rect = cookie_render.get_rect()
multiplier_prices = [50, 500, 5_000, 1000_000]

multiplier_render = font2.render(f"Current Multiplier: x{multiplier}", True, white)
multiplier_rect = multiplier_render.get_rect()
multiplier_rect.x = 15
multiplier_rect.y = 1

x2multipler = font2
x2multipler_render = x2multipler.render(
    f"2x Cookies {multiplier_prices[0]}", True, white
)
x2multipler_rect = x2multipler_render.get_rect()
x2multipler_rect.x = 5
x2multipler_rect.y = 50

autoclickerguy_render = font2.render(
    f"Clicking guy  {multiplier_prices[1]}", True, white
)
autoclickerguy_rect = autoclickerguy_render.get_rect()
autoclickerguy_rect.x = 5
autoclickerguy_rect.y = 100

grandma_render = font2.render(f"Grandma x5  {multiplier_prices[2]}", True, white)
grandma_rect = grandma_render.get_rect()
grandma_rect.x = 5
grandma_rect.y = 150

cookiefarm_render = font2.render(f"Cookie Farm {multiplier_prices[3]}", True, white)
cookiefarm_rect = cookiefarm_render.get_rect()
cookiefarm_rect.x = 5
cookiefarm_rect.y = 200

images_path = os.path.join(
    "C:\\Users\\Filip\\Desktop\\Programing\\Python\\Candy_Clicker_Game",
    "Assets",
    "Sprites",
)

cookie = pygame.image.load(images_path + "\\cookie.png")
cookie2 = pygame.image.load(images_path + "\\cookie2.png")
current_cookie = cookie
cookie_rect = pygame.Rect(0, 0, 240, 233)
cookie_rect.x = (width - cookie_rect.width) // 2 + 115
cookie_rect.y = (height - cookie_rect.height) // 2

interface_border = pygame.Rect(0, 0, 230, height)
line_forborder = pygame.Rect(230, 0, 5, height)

last_score_time = pygame.time.get_ticks()
score_increment_interval = 120  # Increment the score every 100 milliseconds

running = True
clock = pygame.time.Clock()
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if cookie_rect.collidepoint(mouse_pos):
                score = score + multiplier
                current_cookie = cookie2
            elif (
                x2multipler_rect.collidepoint(mouse_pos)
                and score >= multiplier_prices[0]
            ):
                score -= multiplier_prices[0]
                multiplier = multiplier * 2
                multiplier_prices[0] = multiplier_prices[0] * multiplier
                x2multipler_render = x2multipler.render(
                    f"2x Cookies {multiplier_prices[0]}", True, white
                )
                multiplier_render = font2.render(
                    f"Current Multiplier: x{multiplier}", True, white
                )
            elif (
                autoclickerguy_rect.collidepoint(mouse_pos)
                and score >= multiplier_prices[1]
            ):
                score -= multiplier_prices[1]
                cookies_per_sec += 1
                multiplier_prices[1] = multiplier_prices[1] * multiplier
                autoclickerguy_render = font2.render(
                    f"Clicking guy  {multiplier_prices[1]}", True, white
                )
            elif grandma_rect.collidepoint(mouse_pos) and score >= multiplier_prices[2]:
                score -= multiplier_prices[2]
                multiplier = multiplier * 5
                multiplier_prices[2] = multiplier_prices[2] * multiplier
                grandma_render = font2.render(
                    f"Grandma x5{multiplier_prices[2]}", True, white
                )
                multiplier_render = font2.render(
                    f"Current Multiplier: x{multiplier}", True, white
                )
            elif (
                cookiefarm_rect.collidepoint(mouse_pos)
                and score >= multiplier_prices[3]
            ):
                score -= multiplier_prices[3]
                cookies_per_sec += 100
                multiplier_prices[3] = multiplier_prices[3] * multiplier
                cookiefarm_render = font2.render(
                    f"Cookie Farm {multiplier_prices[3]}", True, white
                )
    if current_time - last_score_time >= score_increment_interval:
        score = score + cookies_per_sec * multiplier
        last_score_time = current_time

    screen.fill(white)
    screen.fill(brown)
    pygame.draw.rect(screen, brown, interface_border)
    pygame.draw.rect(screen, black, line_forborder)
    pygame.draw.line(screen, black, (0, 40), (230, 40), 5)
    if current_cookie == cookie:
        screen.blit(current_cookie, (cookie_rect.x, cookie_rect.y))
    else:
        screen.blit(current_cookie, ((width - 270) // 2 + 115, (height - 263) // 2))
    screen.blit(
        cookie_render,
        ((width - cookie_render.get_width()) // 2 + 115, cookie_rect.y - 100),
    )
    screen.blit(multiplier_render, (multiplier_rect.x, multiplier_rect.y))
    screen.blit(x2multipler_render, (x2multipler_rect.x, x2multipler_rect.y))
    screen.blit(autoclickerguy_render, (autoclickerguy_rect.x, autoclickerguy_rect.y))
    screen.blit(grandma_render, (grandma_rect.x, grandma_rect.y))
    screen.blit(cookiefarm_render, (cookiefarm_rect.x, cookiefarm_rect.y))
    cookie_render = cookies_font.render(str(score), True, white)
    pygame.display.flip()
    score = score + cookies_per_sec * multiplier
    current_cookie = cookie

    clock.tick(60)


pygame.quit()
sys.exit()
