# 至 P388 ,打算 改连续子弹,然后下一章是外星人,暂时放弃



import sys
import pygame

from setting import Settings as otherSet
from ship import Ship as otherShip
from bullet import Bullet as otherBullet

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        
        self.settings = otherSet()

        if 1==1:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        else:
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            
        
        pygame.display.set_caption("Alien Invasion")
        self.ship = otherShip(self)


        self.ship = otherShip(self)
        self.bullets = pygame.sprite.Group()


        

        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件。
            self._check_events()
            self.ship.update()


            self._update_bullets()      

            self._update_screen()

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        print(len(self.bullets))



    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            
            
            # 让最近绘制的屏幕可见。
            pygame.display.flip()

            

    def _check_events(self):
        # print(f'len({len(pygame.event)})')
        for event in pygame.event.get():
            

            if event.type == pygame.QUIT:
                sys.exit()



            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            

                

    def _check_keydown_events(self,event):
        print(f"{pygame.key.name(event.key)}")

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_SPACE:
            self.keySpace = True
            self._fire_bullet()


        if event.key == pygame.K_q:
            sys.exit()

                        
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False  

        if event.key == pygame.K_SPACE:
            self.keySpace = False

    def _fire_bullet(self):
        # if len(self.bullets) < self.settings.bullets_allowed:
        #     new_bullet = otherBullet(self)
        #     self.bullets.add(new_bullet)
        


        new_bullet = otherBullet(self)
        self.bullets.add(new_bullet)
        # while self.keySpace == True:
        #     self.bullets.add(new_bullet)

        


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()