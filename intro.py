import random
import pgzrun

TITLE = 'Tavuk'
WIDTH = 800
HEIGHT = 600
gravity = 1
jump_force = 0
isJumping = False
ground = HEIGHT - (HEIGHT//4)
score = 0
game_over = False

play_game = False
game_music = True
exit_game = False

is_sound_playing = False


class BlobActor(Actor):
    def __init__(self, image, **kwargs):
        super().__init__(image)
        self.images = []  # Animasyon kareleri
        self.frame_index = 0  # Mevcut kare indeksi
        self.animation_speed = 5  # Animasyon hızı (kaç frame'de bir değişecek)
        self.frame_timer = 0  # Zamanlayıcı
        self.flip_x = False  # Yatay aynalama (varsayılan: kapalı)

    def animate(self):
        """Animasyonu günceller."""
        if len(self.images) > 1:  # Birden fazla kare varsa animasyon yap
            self.frame_timer += 1
            if self.frame_timer >= self.animation_speed:
                self.frame_timer = 0  # Zamanlayıcıyı sıfırla
                self.frame_index = (self.frame_index + 1) % len(self.images)  # Sonraki kareye geç
                self.image = self.images[self.frame_index]  # Yeni kareyi yükle

    def move_left(self):
        self.images = ['blob_left7', 'blob_left6', 'blob_left5', 'blob_left4']
        self.flip_x = True  # Sola dönük (flip aktif)
        self.x -= 6

    def move_right(self):
        self.images = ['blob4', 'blob5', 'blob6', 'blob7']
        self.flip_x = False  # Sağa dönük (flip pasif)
        self.x += 6

    def jump(self):
        if self.flip_x:
            self.images = ['blob_left7', 'blob_left6', 'blob_left5', 'blob_left4']
        else:
            self.images = ['blob4', 'blob5', 'blob6', 'blob7']

    def idle(self):
        if self.flip_x:
            self.images = ['blob_left2', 'blob_left3']
        else:
            self.images = ['blob0', 'blob1']


class ChickenActor(Actor):
    def __init__(self, image, **kwargs):
        super().__init__(image)
        self.images = []  # Animasyon kareleri
        self.frame_index = 0  # Mevcut kare indeksi
        self.animation_speed = 5  # Animasyon hızı (kaç frame'de bir değişecek)
        self.frame_timer = 0  # Zamanlayıcı
        self.chicken_direction = "left"
        self.chicken_runnig = random.choice([True, False])
        self.chicken_scored = False

    def animate(self):
        """Animasyonu günceller."""
        if len(self.images) > 1:  # Birden fazla kare varsa animasyon yap
            self.frame_timer += 1
            if self.frame_timer >= self.animation_speed:
                self.frame_timer = 0  # Zamanlayıcıyı sıfırla
                self.frame_index = (self.frame_index + 1) % len(self.images)  # Sonraki kareye geç
                self.image = self.images[self.frame_index]  # Yeni kareyi yükle

    def move_left(self):
        if self.chicken_runnig:
            self.images = ['chicken_run_left0',
                           'chicken_run_left1']
            self.x -= 2
        else:
            self.images = ['chicken_walk_left5',
                           'chicken_walk_left4',
                           'chicken_walk_left3',
                           'chicken_walk_left2',
                           'chicken_walk_left1',
                           'chicken_walk_left0']
            self.x -= 1

    def move_right(self):
        if self.chicken_runnig:
            self.images = ['chicken_run0',
                           'chicken_run1']
            self.x += 2
        else:
            self.images = ['chicken_walk0',
                           'chicken_walk1',
                           'chicken_walk2',
                           'chicken_walk3',
                           'chicken_walk4',
                           'chicken_walk5']
            self.x += 1

    def chicken_start_move(self):
        if self.chicken_direction == "left":
            self.move_left()
        else:
            self.move_right()


background = Actor('mushroom-forest-full-resize')
main_menu_template = Actor('main_menu_template')

play_button = Actor('play_button', pos=(WIDTH // 2, HEIGHT//4))
music_button = Actor('music_square_button', pos=(WIDTH // 2, HEIGHT//2))
exit_button = Actor('exit_button', pos=(WIDTH // 2, HEIGHT - (HEIGHT//4)))
new_game_button = Actor('new_game_button')
menu_button = Actor('menu_button', pos=(WIDTH // 2, HEIGHT//2))

# BEN
blob = BlobActor('blob0')
blob.x = WIDTH // 2
blob.y = HEIGHT - (HEIGHT//4)

# TAVUKLAR
chickens = []


def chickenGenerator():
    for _ in range(12):
        chicken = ChickenActor('chicken_walk0')
        if random.choice([True, False]):
            chicken.chicken_direction = "left"
            chicken.x = random.randint(WIDTH + 750, WIDTH + 1500)
        else:
            chicken.chicken_direction = "right"
            chicken.x = -random.randint(50, 2000)
        chicken.y = HEIGHT - (HEIGHT // 4)
        chickens.append(chicken)


if game_music:
    music.play('music.wav')

def draw():
    global chickens, score, play_game, exit_game
    screen.clear()

    if game_over:
        # oyun bitti
        background.draw()
        screen.draw.text("Oyun Bitti",
                         centerx=WIDTH//2, centery=HEIGHT//2,
                         fontname="lambda-regular", fontsize=80)
        screen.draw.text("Puan: " + str(score),
                         centerx=WIDTH // 2, centery=HEIGHT - (HEIGHT // 3) -20,
                         fontname="lambda-regular", fontsize=35)

        play_game = False
        new_game_button.pos = (WIDTH // 5, HEIGHT - (HEIGHT//5))
        new_game_button.draw()

        menu_button.pos = (WIDTH // 2, HEIGHT - (HEIGHT // 5))
        menu_button.draw()

        exit_button.pos = (WIDTH - (WIDTH // 5), HEIGHT - (HEIGHT // 5))
        exit_button.draw()
    elif not play_game:
        # oyun ana ekranı
        main_menu_template.draw()
        play_button.draw()
        music_button.draw()
        exit_button.draw()
    else:
        # oyun başladı
        background.draw()
        blob.draw()
        screen.draw.text("Puan: " + str(score),
                         centerx=80, centery=170,
                         fontname="lambda-regular", fontsize=35)
        for chicken in chickens:
            chicken.draw()


def on_mouse_down(pos):
    global play_game, game_over, blob, game_music, menu_button, chickens, exit_button, score
    if not play_game:  # oyun esnasında buton tıklamalarını iptal ediyourum
        if play_button.collidepoint(pos):
            play_game = True
            chickenGenerator()
            score = 0
            blob.pos = (WIDTH // 2, HEIGHT - (HEIGHT // 4))
        elif new_game_button.collidepoint(pos):
            # yeni oyun için durumlar sıfırlanır
            play_game = True
            game_over = False
            score = 0
            blob.x = WIDTH // 2
            blob.y = HEIGHT - (HEIGHT // 4)
            chickenGenerator()
        elif music_button.collidepoint(pos):
            game_music = not game_music
            if game_music:
                music.play('music.wav')
        elif menu_button.collidepoint(pos):
            play_game = False
            game_over = False
            exit_button.pos = (WIDTH // 2, HEIGHT - (HEIGHT//4))
        elif exit_button.collidepoint(pos):
            exit()


def update():
    global gravity, jump_force, isJumping, chickens, score
    global game_over, play_game, game_music, exit_game, is_sound_playing
    if not game_music:
        music.stop()

    if play_game:
        blob.animate()
        blob.idle()
        for chicken in chickens:
            chicken.animate()
            chicken.chicken_start_move()

            # tavuk ekrandan çıktıktan bir süre sonra başa dönsün
            if chicken.chicken_direction == "left":
                # sola giden tavuk ekranın yarısını geçince paun alınır
                if chicken.x < WIDTH/2 and not chicken.chicken_scored:
                    score += 1
                    sounds.cricket.play()
                    chicken.chicken_scored = True
                if chicken.x < -random.randint(10, 70):
                    chicken.x = random.randint(WIDTH + 800, WIDTH + 2000)
                    chicken.chicken_scored = False

            else:  # direction right
                # sağa giden tavuk ekranın yarısını geçince paun alınır
                if chicken.x > WIDTH/2 and not chicken.chicken_scored:
                    score += 1
                    sounds.cricket.play()
                    chicken.chicken_scored = True
                if chicken.x > WIDTH + random.randint(10, 80):
                    chicken.x = -random.randint(350, 1500)
                    chicken.chicken_scored = False

            # tavuklarla çarpışma kontrolü
            if blob.colliderect(chicken):
                game_over = True
                chickens.clear()
                sounds.gameover.play()

        # zıplama mekaniği
        jump_force += gravity
        blob.y += jump_force

        if blob.y >= ground:
            blob.y = ground
            isJumping = False

        if keyboard.left:
            blob.move_left()
            if not is_sound_playing:  # Ses çalmıyorsa
                sounds.runblobfast.play()  # Ses çal
                is_sound_playing = True  # Sesin çaldığını işaretle
        elif keyboard.right:
            blob.move_right()
            if not is_sound_playing:  # Ses çalmıyorsa
                sounds.runblobfast.play()  # Ses çal
                is_sound_playing = True  # Sesin çaldığını işaretle
        else:  # Sol ok tuşu bırakıldıysa
            if is_sound_playing:  # Ses çalıyorsa
                sounds.runblobfast.stop()  # Ses durdur
                is_sound_playing = False  # Sesin durduğunu işaretle
        if keyboard.space and not isJumping:
            sounds.blobjump.play()  # çok uzun bir ses değil. stop gerekmez.
            isJumping = True
            jump_force = -16
            blob.y += jump_force
        if not blob.y == ground:
            sounds.runblobfast.stop()  # Ses durdur


pgzrun.go()
