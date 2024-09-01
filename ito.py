import sys
import pygame
from random import randint

pygame.init() #pygame初期化

class Title: #最初に表示される画面
    def __init__(self) -> None:
        self.block1_color = (0,0,0) #背景の色
        self.button = pygame.Rect(500,300,400,100) #ボタンのサイズ
        self.enable = True
    def update(self):
        pass
    def draw(self,screen):
        if self.enable:
            pygame.draw.rect(screen,self.block1_color,self.button)
            text1 = font.render("ito(2~10)",True,(0,0,255)) #引数：テキスト内容、antialias、文字の色RGB
            text2 = font.render("start",True,(255,255,255)) #引数：テキスト内容、antialias、文字の色RGB
            main_surface.blit(text1,(100,100)) #メイン画面にテキスト配置
            main_surface.blit(text2,(525,285))
            if event.type == pygame.MOUSEBUTTONDOWN:   #ボタン押されたら画面が変わる
                if self.button.collidepoint(event.pos):
                    gamen1.enable = False
                    gamen2.enable = True

class Mode: #mode変更画面
    def __init__(self) -> None:
        self.block1_color = (0,100,0)
        self.button2 =  pygame.Rect(100,100,100,100)
        self.button3 =  pygame.Rect(100,300,100,100)
        self.button4 =  pygame.Rect(100,500,100,100)
        self.button5 =  pygame.Rect(500,100,100,100)
        self.button6 =  pygame.Rect(500,300,100,100)
        self.button7 =  pygame.Rect(500,500,100,100)
        self.button8 =  pygame.Rect(900,100,100,100)
        self.button9 =  pygame.Rect(900,300,100,100)
        self.button10 =  pygame.Rect(900,500,100,100)
        self.enable = False
    def update(self):
        pass
    def draw(self,screen):
        if self.enable:
            pygame.draw.rect(screen,self.block1_color,self.button2)
            pygame.draw.rect(screen,self.block1_color,self.button3)
            pygame.draw.rect(screen,self.block1_color,self.button4)
            pygame.draw.rect(screen,self.block1_color,self.button5)
            pygame.draw.rect(screen,self.block1_color,self.button6)
            pygame.draw.rect(screen,self.block1_color,self.button7)
            pygame.draw.rect(screen,self.block1_color,self.button8)
            pygame.draw.rect(screen,self.block1_color,self.button9)
            pygame.draw.rect(screen,self.block1_color,self.button10)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button2.collidepoint(event.pos):
                    gamen2.enable = False
                    gamen3.enable = True
                    gamen3.set_players(2)
                elif self.button3.collidepoint(event.pos):
                    gamen2.enable = False
                    gamen3.enable = True
                    gamen3.set_players(3)
                elif self.button4.collidepoint(event.pos):
                    gamen2.enable = False
                    gamen3.enable = True
                    gamen3.set_players(4)
                elif self.button5.collidepoint(event.pos):
                    gamen2.enable = False
                    gamen3.enable = True
                    gamen3.set_players(5)
                elif self.button6.collidepoint(event.pos):
                    gamen2.enable = False
                    gamen3.enable = True
                    gamen3.set_players(6)
                elif self.button7.collidepoint(event.pos):
                    gamen2.enable = False
                    gamen3.enable = True
                    gamen3.set_players(7)
                elif self.button8.collidepoint(event.pos):
                    gamen2.enable = False
                    gamen3.enable = True
                    gamen3.set_players(8)
                elif self.button9.collidepoint(event.pos):
                    gamen2.enable = False
                    gamen3.enable = True
                    gamen3.set_players(9)
                elif self.button10.collidepoint(event.pos):
                    gamen2.enable = False
                    gamen3.enable = True
                    gamen3.set_players(10)
    
class Play:
    def __init__(self) -> None:
        self.cards = []
        self.card_positions = []
        self.block1_color = (0, 0, 0)
        self.dragging = False
        self.dragged_card_index = None
        self.offset_x = 0
        self.offset_y = 0
        self.enable = False

        # 判定ボタンを追加
        self.check_button = pygame.Rect(650, 500, 200, 100)
        self.font = pygame.font.Font(None, 50)
          
        # 成功メッセージの管理
        self.success_message = ""
        self.message_displayed = False

    def set_players(self, num_players):
        """プレイヤー数に応じてカードとその位置を設定"""
        self.cards = [randint(1, 100) for _ in range(num_players)]
        self.card_positions = [(50 + i * 150, 75) for i in range(num_players)]

    def update(self):
        # ドラッグ中の処理
        if self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.card_positions[self.dragged_card_index] = (mouse_x + self.offset_x, mouse_y + self.offset_y)

    def draw(self, screen):
        if self.enable:
            # プレイヤー数に応じてカードを表示
            for i, card_num in enumerate(self.cards):
                position = self.card_positions[i]
                screen.blit(img_dict[card_num], position)

            # 判定ボタンを描画
            pygame.draw.rect(screen, (0, 128, 0), self.check_button)
            button_text = self.font.render("Check Order", True, (255, 255, 255))
            screen.blit(button_text, (self.check_button.x + 20, self.check_button.y + 30))

            # 成功メッセージを描画
            if self.message_displayed:
                success_text = self.font.render(self.success_message, True, (0, 255, 0))
                screen.blit(success_text, (600, 400))

    def handle_event(self, event):
        # マウスボタンが押されたときの処理
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            
            # 判定ボタンがクリックされたときの処理
            if self.check_button.collidepoint(mouse_x, mouse_y):
                if self.check_order():
                    self.success_message = "Success! The cards are in the correct order."
                    self.message_displayed = True
                else:
                    self.success_message = "Cards are not in order yet."
                    self.message_displayed = True
            
            # カードがクリックされたときの処理
            elif not self.dragging:
                for i, (card_num, pos) in enumerate(zip(self.cards, self.card_positions)):
                    card_rect = img_dict[card_num].get_rect(topleft=pos)
                    if card_rect.collidepoint(mouse_x, mouse_y):
                        self.dragging = True
                        self.dragged_card_index = i
                        self.offset_x = pos[0] - mouse_x
                        self.offset_y = pos[1] - mouse_y
                        break

        # マウスボタンが離されたときの処理
        elif event.type == pygame.MOUSEBUTTONUP and self.dragging:
            self.dragging = False
            self.dragged_card_index = None

    def check_order(self):
        """カードの位置に基づいて順序をチェックする"""
        # カードのX座標に基づいてカードをソート
        sorted_cards = sorted(zip(self.card_positions, self.cards), key=lambda x: x[0][0])
        
        # 並び替えたカードの番号リスト
        sorted_numbers = [card_num for pos, card_num in sorted_cards]

        # 並び替えたカードの番号リストが昇順かどうかをチェック
        return sorted_numbers == sorted(sorted_numbers)


main_surface = pygame.display.set_mode((1500,700)) #メインン画面初期化(横,縦)
clock = pygame.time.Clock() #Clockオブジェクト作成

num = []
img_dict = {}
for card in range(1, 101):
    # '1_100/' ディレクトリから画像をロードして辞書に保存
    img_dict[card] = pygame.transform.rotozoom(
        pygame.image.load(f'1_100/{card}.png'), 0, 0.12)
    
card_num1 = randint(1,101) #card読み込み
card_num2 = randint(1,101)
card_num3 = randint(1,101)


going = True #ループを続けるかどうか
gamen1 = Title()
gamen2 = Mode()
gamen3 = Play()        

while going: #終了イベントまでループ
    for event in pygame.event.get(): 
        #終了イベント
        #ループ終了
        if event.type == pygame.QUIT:
            going = False  
        #イベントを各画面に伝える
        if gamen3.enable:
            gamen3.handle_event(event)   
                

    main_surface.fill((255,255,255))
    pygame.display.set_caption("ito") #title
    font = pygame.font.Font(None,200) #Noneはpygameの規定のフォント
    gamen1.update()
    gamen2.update()
    gamen3.update()
    gamen1.draw(main_surface)
    gamen2.draw(main_surface)
    gamen3.draw(main_surface)
    pygame.display.update() #メイン画面の更新
    clock.tick(10) #フレームレートの設定

#終了処理
pygame.quit()
sys.exit()


