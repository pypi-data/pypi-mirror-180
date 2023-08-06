import pygame,time,random
_display = pygame.display
COLOR_BLACK = pygame.Color(195, 194, 200)
COLOR_RED = pygame.Color(96, 177, 85)
version = 'v1.25'
class MainGame():
    #游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    #创建老師
    Teacher_P1 = None
    Student_list = []
    Student_count = 5
    Bullet_list = []
    Student_bullet_list = []
    Explode_list = []
    Wall_list = []
    #开始游戏方法
    def startGame(self):
        _display.init()
        #创建窗口加载窗口(借鉴官方文档)
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        self.creatTeacher()
        self.creatStudent()
        self.creatWalls()
        #游戏标题
        _display.set_caption("The miserable life of architectural students"+version)
        #让窗口持续刷新操作
        while True:
            #给窗口填充颜色
            MainGame.window.fill(COLOR_BLACK)
            #在循环中持续完成事件的获取
            self.getEvent()
            #将绘制文字得到的小画布，粘贴到窗口中
            MainGame.window.blit(self.getTextSurface("%d number of students remaining"%len(MainGame.Student_list)),(5,5))
            #调用展示墙壁的方法
            self.blitWalls()
            if MainGame.Teacher_P1 and MainGame.Teacher_P1.live:
                # 将老師加入到窗口中
                MainGame.Teacher_P1.displayTeacher()
            else:
                del MainGame.Teacher_P1
                MainGame.Teacher_P1 = None
            #循环展示老師
            self.blitStudent()
            #根据老師的开关状态调用老師的移动方法
            if MainGame.Teacher_P1 and not MainGame.Teacher_P1.stop:
                MainGame.Teacher_P1.move()
                #调用碰撞墙壁的方法
                MainGame.Teacher_P1.hitWalls()
            #调用渲染子弹列表的一个方法
            self.blitBullet()
            #调用渲染子弹列表的一个方法
            self.blitStudentBullet()
            #调用展示爆炸效果的方法
            self.displayExplodes()
            time.sleep(0.02)
            #窗口的刷新
            _display.update()
    #创建老師的方法
    def creatTeacher(self):
        # 创建老師
        MainGame.Teacher_P1 = Teacher(400, 300)
        #创建音乐对象
        music = Music('img/start.wav')
        #调用播放音乐方法
        music.play()
    #创建學生
    def creatStudent(self):
        top = 100
        for i in range(MainGame.Student_count):
            speed = random.randint(3,6)
            #每次都随机生成一个left值
            left = random.randint(1, 7)
            eStudent = Student(left*100,top,speed)
            MainGame.Student_list.append(eStudent)
    #创建墙壁的方法
    def creatWalls(self):
        for i in range(6):
            wall = Wall(130*i,240)
            MainGame.Wall_list.append(wall)
    def blitWalls(self):
        for wall in MainGame.Wall_list:
            if wall.live:
                wall.displayWall()
            else:
                MainGame.Wall_list.remove(wall)
    #将老師加入到窗口中
    def blitStudent(self):
        for eTeacher in MainGame.Student_list:
            if eTeacher.live:
                eTeacher.displayTeacher()
                # 老師移动的方法
                eTeacher.randMove()
                #调用老師与墙壁的碰撞方法
                eTeacher.hitWalls()
                #老師是否撞到老師
                eTeacher.hitMyTeacher()
                # 调用老師的射击
                eBullet = eTeacher.shot()
                # 如果子弹为None。不加入到列表
                if eBullet:
                    # 将子弹存储子弹列表
                    MainGame.Student_bullet_list.append(eBullet)
            else:
                MainGame.Student_list.remove(eTeacher)
    #将子弹加入到窗口中
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            #如果子弹还活着，绘制出来，否则，直接从列表中移除该子弹
            if bullet.live:
                bullet.displayBullet()
                # 让子弹移动
                bullet.bulletMove()
                # 调用子弹与老師的碰撞方法
                bullet.hitStudent()
                # 调用判断子弹是否碰撞到墙壁的方法
                bullet.hitWalls()
            else:
                MainGame.Bullet_list.remove(bullet)
    #将子弹加入到窗口中
    def blitStudentBullet(self):
        for eBullet in MainGame.Student_bullet_list:
            # 如果子弹还活着，绘制出来，否则，直接从列表中移除该子弹
            if eBullet.live:
                eBullet.displayBullet()
                # 让子弹移动
                eBullet.bulletMove()
                #调用是否碰撞到墙壁的一个方法
                eBullet.hitWalls()
                if MainGame.Teacher_P1 and MainGame.Teacher_P1.live:
                    eBullet.hitMyTeacher()
            else:
                MainGame.Student_bullet_list.remove(eBullet)
    #新增方法： 展示爆炸效果列表
    def displayExplodes(self):
        for explode in MainGame.Explode_list:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.Explode_list.remove(explode)
    #获取程序期间所有事件(鼠标事件，键盘事件)
    def getEvent(self):
        #1.获取所有事件
        eventList = pygame.event.get()
        #2.对事件进行判断处理(1、点击关闭按钮  2、按下键盘上的某个按键)
        for event in eventList:
            #判断event.type 是否QUIT，如果是退出的话，直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.endGame()
            #判断事件类型是否为按键按下，如果是，继续判断按键是哪一个按键，来进行对应的处理
            if event.type == pygame.KEYDOWN:
                #点击ESC或r键让老師重生
                if (event.key == pygame.K_ESCAPE or event.key == pygame.K_r )and not MainGame.Teacher_P1:
                    #调用创建老師的方法
                    self.creatTeacher()
                if MainGame.Teacher_P1 and MainGame.Teacher_P1.live:
                    # 具体是哪一个按键的处理
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a :
                        print("老師向左调头，移动")
                        # 修改老師方向
                        MainGame.Teacher_P1.direction = 'L'
                        MainGame.Teacher_P1.stop = False
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        print("老師向右调头，移动")
                        # 修改老師方向
                        MainGame.Teacher_P1.direction = 'R'
                        MainGame.Teacher_P1.stop = False
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        print("老師向上调头，移动")
                        # 修改老師方向
                        MainGame.Teacher_P1.direction = 'U'
                        MainGame.Teacher_P1.stop = False
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        print("老師向下掉头，移动")
                        # 修改老師方向
                        MainGame.Teacher_P1.direction = 'D'
                        MainGame.Teacher_P1.stop = False
                    elif event.key == pygame.K_SPACE:
                        print("发射子弹")
                        if len(MainGame.Bullet_list) < 3:
                            # 产生一颗子弹
                            m = Bullet(MainGame.Teacher_P1)
                            # 将子弹加入到子弹列表
                            MainGame.Bullet_list.append(m)
                            music = Music('img/fire.wav')
                            music.play()
                        else:
                            print("子弹数量不足")
                        print("当前屏幕中的子弹数量为:%d" % len(MainGame.Bullet_list))
            #结束游戏方法
            if event.type == pygame.KEYUP:
                #松开的如果是方向键，才更改移动开关状态
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if MainGame.Teacher_P1 and MainGame.Teacher_P1.live:
                        # 修改老師的移动状态
                        MainGame.Teacher_P1.stop = True
    #左上角文字绘制的功能
    def getTextSurface(self,text):
        # 初始化字体模块
        pygame.font.init()
        #查看系统支持的所有字体
        # fontList = pygame.font.get_fonts()
        # print(fontList)
        # 选中一个合适的字体
        font = pygame.font.SysFont('kaiti',18)
        # 使用对应的字符完成相关内容的绘制
        textSurface = font.render(text,True,COLOR_RED)
        return textSurface
    def endGame(self):
        print("谢谢使用")
        #结束python解释器
        exit()
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Teacher(BaseItem):
    def __init__(self,left,top):
        self.images = {
            'U':pygame.image.load('img/p1TeacherU.gif'),
            'D':pygame.image.load('img/p1TeacherD.gif'),
            'L':pygame.image.load('img/p1TeacherL.gif'),
            'R':pygame.image.load('img/p1TeacherR.gif')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        #老師所在的区域  Rect->
        self.rect = self.image.get_rect()
        #指定老師初始化位置 分别距x，y轴的位置
        self.rect.left = left
        self.rect.top = top
        #新增速度属性
        self.speed = 5
        #新增属性： 老師的移动开关
        self.stop = True
        #新增属性  live 用来记录，老師是否活着
        self.live = True
        #新增属性： 用来记录老師移动之前的坐标(用于坐标还原时使用)
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    #老師的移动方法
    def move(self):
        #先记录移动之前的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop
    #新增碰撞墙壁的方法
    def hitWalls(self):
       for wall in MainGame.Wall_list:
           if pygame.sprite.collide_rect(wall,self):
               self.stay()
    #射击方法
    def shot(self):
        return Bullet(self)
    #展示老師(将老師这个surface绘制到窗口中  blit())
    def displayTeacher(self):
        #1.重新设置老師的图片
        self.image = self.images[self.direction]
        #2.将老師加入到窗口中
        MainGame.window.blit(self.image,self.rect)
class MyTeacher(Teacher):
    def __init__(self,left,top):
        super(MyTeacher, self).__init__(left,top)
    #新增主动碰撞到老師的方法
    def hitStudent(self):
        for eTeacher in MainGame.Student_list:
            if pygame.sprite.collide_rect(eTeacher,self):
                self.stay()

class Student(Teacher):
    def __init__(self,left,top,speed):
        super(Student, self).__init__(left,top)
        # self.live = True
        self.images = {
            'U': pygame.image.load('img/Student1U.gif'),
            'D': pygame.image.load('img/Student1D.gif'),
            'L': pygame.image.load('img/Student1L.gif'),
            'R': pygame.image.load('img/Student1R.gif')
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        # 老師所在的区域  Rect->
        self.rect = self.image.get_rect()
        # 指定老師初始化位置 分别距x，y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = speed
        self.stop = True
        #新增步数属性，用来控制老師随机移动
        self.step = 30

    def randDirection(self):
        num = random.randint(1,4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'
    # def displayEnemtTeacher(self):
    #     super().displayTeacher()
    #随机移动
    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 50
        else:
            self.move()
            self.step -= 1
    def shot(self):
        num = random.randint(1,1000)
        if num  <= 20:
            return Bullet(self)
    def hitMyTeacher(self):
        if MainGame.Teacher_P1 and MainGame.Teacher_P1.live:
            if pygame.sprite.collide_rect(self, MainGame.Teacher_P1):
                # 让老師停下来  stay()
                self.stay()
class Bullet(BaseItem):
    def __init__(self,people):
        #图片
        self.image = pygame.image.load('img/restart.gif')
        #方向（老師方向）
        self.direction = people.direction
        #位置
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = people.rect.left + people.rect.width/2 - self.rect.width/2
            self.rect.top = people.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = people.rect.left + people.rect.width / 2 - self.rect.width / 2
            self.rect.top = people.rect.top + people.rect.height
        elif self.direction == 'L':
            self.rect.left = people.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = people.rect.top + people.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = people.rect.left + people.rect.width
            self.rect.top = people.rect.top + people.rect.width / 2 - self.rect.width / 2
        #速度
        self.speed = 7
        #用来记录子弹是否活着
        self.live = True
    #子弹的移动方法
    def bulletMove(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                #修改状态值
                self.live = False
        elif self.direction == 'D':
            if self.rect.top < MainGame.SCREEN_HEIGHT - self.rect.height:
                self.rect.top += self.speed
            else:
                # 修改状态值
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                # 修改状态值
                self.live = False
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH - self.rect.width:
                self.rect.left += self.speed
            else:
                # 修改状态值
                self.live = False
    #展示子弹的方法
    def displayBullet(self):
        MainGame.window.blit(self.image,self.rect)
    #新增子弹碰撞老師的方法
    def hitStudent(self):
        for eTeacher in MainGame.Student_list:
            if pygame.sprite.collide_rect(eTeacher,self):
                #产生一个爆炸效果
                explode = Explode(eTeacher)
                #将爆炸效果加入到爆炸效果列表
                MainGame.Explode_list.append(explode)
                self.live = False
                eTeacher.live = False
    #新增子弹与老師的碰撞方法
    def hitMyTeacher(self):
        if pygame.sprite.collide_rect(self,MainGame.Teacher_P1):
            # 产生爆炸效果，并加入到爆炸效果列表中
            explode = Explode(MainGame.Teacher_P1)
            MainGame.Explode_list.append(explode)
            #修改子弹状态
            self.live = False
            #修改老師状态
            MainGame.Teacher_P1.live = False
    #新增子弹与墙壁的碰撞
    def hitWalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                #修改子弹的live属性
                self.live = False
                wall.hp -= 1
                if wall.hp <= 0:
                    wall.live = False
class Explode():
    def __init__(self,Teacher):
        self.rect = Teacher.rect
        self.step = 0
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif')
        ]
        self.image = self.images[self.step]
        self.live = True
    #展示爆炸效果
    def displayExplode(self):
        if self.step < len(self.images):
            MainGame.window.blit(self.image, self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0
class Wall():
    def __init__(self,left,top):
        self.image = pygame.image.load('img/steelsu.gif')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        #用来判断墙壁是否应该在窗口中展示
        self.live = True
        #用来记录墙壁的生命值
        self.hp = 3
    #展示墙壁的方法
    def displayWall(self):
        MainGame.window.blit(self.image,self.rect)
#老師出生
class Music():
    def __init__(self,fileName):
        self.fileName = fileName
        #先初始化混合器
        pygame.mixer.init()
        pygame.mixer.music.load(self.fileName)
    #开始播放音乐
    def play(self):
        pygame.mixer.music.play()
        pass
MainGame().startGame()
