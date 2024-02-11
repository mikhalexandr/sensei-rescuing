import pygame
import consts
import windows
import lvl_gen
from processHelper import load_image
import random


class Pic(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, sprite, *group):
        sprite = load_image(sprite)
        group = group
        super().__init__(*group)
        self.image = pygame.transform.scale(sprite, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


boss_group = pygame.sprite.Group()
boss_projectile_group = pygame.sprite.Group()
b_projectile_speed = []


class Boss(pygame.sprite.Sprite):
    pic = load_image(consts.kowlad)
    # php = load_image('пуля')

    def __init__(self, x, y, koef, act=0):
        super().__init__(boss_group)
        self.sprites = pygame.transform.scale(
            Boss.pic, (Boss.pic.get_width() * koef, Boss.pic.get_height() * koef))
        self.k = koef
        self.frames = []
        self.cut_sheet(self.sprites, koef, act)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.counter = 0
        self.act = act
        self.looking_right = False
        self.hp = 20
        self.bullet_speed = 6
        self.step = 0
        self.hitick = 0
        self.pospoint = 0

    def cut_sheet(self, sprites, koef, act):
        self.rect = pygame.Rect(0, 0, 64 * koef,
                                108 * koef)

        for i in range(sprites.get_height() // int(108 * koef)):
            frame_location = (self.rect.w * act, self.rect.h * i)
            self.frames.append(sprites.subsurface(pygame.Rect(
                frame_location, self.rect.size)))

    def update(self):
        lvl_gen.get_shadow(*self.rect)
        lvl_gen.shadowgroup.draw(windows.screen)
        self.image = self.frames[self.cur_frame]

        if not self.step:
            if self.counter == 7:
                self.cur_frame = (self.cur_frame + 1) % 8
        else:
            if self.counter % (self.step * 3) in range(0, 3):
                if self.hitick != 4:
                    a = pygame.transform.scale(load_image(consts.shadow), (self.rect.w, self.rect.h))
                    self.image = a
                    self.hitick += 1
                else:
                    self.hitick = 0
                    self.step = 0
        self.counter = (self.counter + 1) % 8

    def set_coords(self, x, y):
        self.rect[:2] = [x, y]

    def get_coords(self):
        return self.rect[0], self.rect[1]

    # def shoot(self):
    #     Pic(self.get_coords()[0] + self.get_size()[0] // 2,
    #         self.get_coords()[1] + self.get_size()[1] // 2.5,
    #         Boss.php.get_width() // 2 * windows.k ** windows.fullscreen,
    #         Boss.php.get_height() // 2 * windows.k ** windows.fullscreen, marker,
    #         boss_projectile_group)
    #     if self.looking_right:
    #         self.projectile_speed.append((self.bullet_speed * self.k ** windows.fullscreen, self))
    #     else:
    #         self.projectile_speed.append((-self.bullet_speed * self.k ** windows.fullscreen, self))

    def get_hit(self):
        self.hp -= 1
        self.step = 2
        self.make_move()
        print(self.hp)
        return self.hp

    def change_act(self, act, coords):
        pos = coords
        self.act = act
        self.frames = []
        self.cur_frame = 0
        if act == 0:
            self.cut_sheet(self.sprites, self.k, self.act)
        elif act == 1:
            self.cut_sheet(self.sprites, self.k, self.act)
        else:
            pass
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(*pos)

    def shoot(self):
        pass

    def make_move(self):
        cordi = [[896, 322], [64, 322], [64, 66], [896, 66], [480, 66]]
        a = random.randint(0, 4)
        lvl_gen.get_shadow(*self.rect)
        lvl_gen.shadowgroup.draw(windows.screen)
        while a == self.pospoint:
            a = random.randint(0, 4)
        self.set_coords(windows.otstupx * windows.fullscreen + cordi[a][0] * self.k, cordi[a][1] * self.k)
        print(a)
        if a in [0, 3]:
            self.change_act(0, self.get_coords())
        elif a in [1, 2]:
            self.change_act(1, self.get_coords())
        self.pospoint = a