from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import FadeTransition,ScreenManager 
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles
import time
from pygame import mixer
import os
import sys
import random
import webbrowser

mixer.init()

kv='''
MyScreenManager:             
    MDScreen:
        MDFloatLayout:
            size_hint:(1,1)
            md_bg_color:'#0ed459d8'
            MDLabel:
                text:'7/290'
                pos_hint:{'center_x':0.5,'top':0.8}
                size_hint_y:None
                height:'40dp'
                halign:'center'
                font_style:'Digital'
                theme_text_color:'Custom'
                text_color:'red'
                theme_font_size:'Custom'
                font_size:'30dp'
            FitImage:
                source:'assets/background/log.png'
                size_hint:(None,None)
                width:'100dp'
                pos_hint:{'center_x':0.5,'center_y':0.5}
            MDLabel:
                text:'My Speaker'
                pos_hint:{'center_x':0.5,'y':0.3}
                size_hint_y:None
                height:'40dp'
                halign:'center'
                theme_text_color:'Custom'
                text_color:'wheat'
                font_style:'Digital'
                theme_font_size:'Custom'
                font_size:'40dp'
            MDLabel:
                id:loadings
                pos_hint:{'center_x':0.5,'y':0.3/2}
                size_hint_y:None
                height:'40dp'
                halign:'center'
                theme_text_color:'Custom'
                text_color:'wheat'
                font_style:'Digital'
                theme_font_size:'Custom'
                font_size:'20dp'
    MDScreen:
        name:'about'
        MDBoxLayout:
            size_hint:(1,1)
            md_bg_color:'white'
            orientation:'vertical'
            MDTopAppBar:
                title:'About'
                left_action_items:[['arrow-left',lambda x:app.go_screens(x)]]
            MDBoxLayout:
                orientation:'vertical'
                padding:[20,]
                MDLabel:
                    text:'About App'
                    halign:'center'
                    font_style:'Digital'
                    size_hint_y:None
                    height:'40dp'
                MDLabel:
                    padding:[0,]
                    id:about
                MDLabel:
                    text:'Version'
                    halign:'center'
                    font_style:'Digital'
                    size_hint_y:None
                    height:'40dp'
                MDLabel:
                    text:'0.0.1'
                    halign:'center'
                    size_hint_y:None
                    height:'40dp'
                MDLabel:
                    text:'Developer'
                    halign:'center'
                    font_style:'Digital'
                    size_hint_y:None
                    height:'40dp'
                MDLabel:
                    text:'Nyson Mwachande'
                    halign:'center'
                    size_hint_y:None
                    height:'40dp'
                MDLabel:
                    text:'follow Developer'
                    halign:'center'
                    font_style:'Digital'
                    size_hint_y:None
                    height:'40dp'
                MDBoxLayout:
                    orientation:'horizontal'
                    size_hint_y:None
                    height:'50dp'
                    MDWidget:
                    MDIconButton:
                        icon:'facebook'
                        theme_icon_color:'Custom'
                        color:'white'
                        on_release:app.open_fb()
                    MDIconButton:
                        icon:'whatsapp'
                        theme_icon_color:'Custom'
                        color:'white'
                        on_release:app.open_wap()
                    MDIconButton:
                        icon:'github'
                        theme_icon_color:'Custom'
                        color:'white'
                        on_release:app.open_gh()
                    MDWidget:

    MDScreen:
        name:'home'
        MDBoxLayout:
            MDBoxLayout:
                size_hint:(1,1)
                md_bg_color:'#0ec459d8'
                orientation:'vertical'
                padding:15
                spacing:5
                MDBoxLayout:
                    size_hint_y:None
                    orientation:'horizontal'
                    height:'40dp'
                    canvas.before:
                        Color:
                            rgba:rgba('#ffffffff')
                        Rectangle:
                            source:'assets/background/bg.png'
                            pos:self.pos
                            size:self.size
                    MDWidget:
                    MDWidget:
                    MDIconButton:
                        icon:'dots-vertical'
                        theme_icon_color:'Custom'
                        color:'white'
                        on_release:app.menu_items(bt)
                MDBoxLayout:
                    md_bg_color:'gray'
                    padding:[20,]
                    size_hint_y:None
                    height:'160dp'
                    MDBoxLayout:
                        orientation:'vertical'
                        pos_hint:{'center_x':0.5,'center_y':0.5}
                        md_bg_color:'black'
                        padding:5
                        size_hint_y:None
                        height:'130dp'
                        MDFloatLayout:
                            size_hint_y:None
                            height:'20dp'
                            padding:5
                            MDIcon:
                                icon:'play'
                                pos_hint:{'x':0,'y':0}
                                theme_icon_color:'Custom'
                                color:'gray'
                                id:play_icon
                            MDIcon:
                                icon:'pause'
                                pos_hint:{'x':0.1/2,'y':0}
                                theme_icon_color:'Custom'
                                color:'gray'
                                id:pause_icon
                            MDIcon:
                                icon:'stop'
                                pos_hint:{'x':0.1,'y':0}
                                theme_icon_color:'Custom'
                                color:'gray'
                                id:stop_icon
                            MDIcon:
                                icon:'repeat'
                                id:repeat_icon
                                pos_hint:{'x':0.3/2,'y':0}
                                theme_icon_color:'Custom'
                                color:'gray'
                            MDIcon:
                                icon:'shuffle'
                                id:shuffle_icon
                                pos_hint:{'x':0.2,'y':0}
                                theme_icon_color:'Custom'
                                color:'gray'
                            MDLabel:
                                id:usb
                                text:'USB'
                                pos_hint:{'x':0.3,'y':0}
                                theme_text_color:'Custom'
                            MDLabel:
                                id:tft
                                text:'TFT'
                                pos_hint:{'x':0.4,'y':0}
                                theme_text_color:'Custom'
                            MDLabel:
                                id:bt
                                text:'C'
                                pos_hint:{'x':0.5,'y':0}
                                theme_text_color:'Custom'
                        
                        MDLabel:
                            theme_text_color:'Custom'
                            text_color:'red'
                            theme_font_size:'Custom'
                            font_size:'30dp'
                            font_style:'Digital'
                            id:tracks
                        
                Button:
                    canvas.before:
                        Color:
                            rgba:rgba('#ffffffff')
                        Rectangle:
                            source:'assets/background/mode.png'
                            pos:self.pos
                            size:self.size
                    background_color:(0,0,0,0)
                    size_hint:(None,None)
                    width:'60dp'
                    height:'30dp'
                    on_press:app.set_mode()
                        
                MDBoxLayout:
                    size_hint_y:None
                    height:'45dp'
                    padding:[0,5,0,5]
                    spacing:5
                    Button:
                        canvas.before:
                            Color:
                                rgba:rgba('#ffffffff')
                            Rectangle:
                                source:'assets/background/prev.png'
                                pos:self.pos
                                size:self.size
                        background_color:(0,0,0,0)
                        on_press:app.previous_song()
                    Button:
                        canvas.before:
                            Color:
                                rgba:rgba('#ffffffff')
                            Rectangle:
                                source:'assets/background/play.png'
                                pos:self.pos
                                size:self.size
                        background_color:(0,0,0,0)
                        on_press:app.play_button()
                    Button:
                        canvas.before:
                            Color:
                                rgba:rgba('#ffffffff')
                            Rectangle:
                                source:'assets/background/stop.png'
                                pos:self.pos
                                size:self.size
                        background_color:(0,0,0,0)
                        on_press:app.stop_button()
                    Button:
                        canvas.before:
                            Color:
                                rgba:rgba('#ffffffff')
                            Rectangle:
                                source:'assets/background/next.png'
                                pos:self.pos
                                size:self.size
                        background_color:(0,0,0,0)
                        on_press:app.next_song()
                    Button:
                        canvas.before:
                            Color:
                                rgba:rgba('#ffffffff')
                            Rectangle:
                                source:'assets/background/repeat.png'
                                pos:self.pos
                                size:self.size
                        background_color:(0,0,0,0)
                        on_press:app.set_repeat()
                    Button:
                        canvas.before:
                            Color:
                                rgba:rgba('#ffffffff')
                            Rectangle:
                                source:'assets/background/shuffle.png'
                                pos:self.pos
                                size:self.size
                        background_color:(0,0,0,0)
                        on_press:app.set_shuffle()
                MDBoxLayout:
                    canvas.before:
                        Color:
                            rgba:rgba('#ffffffff')
                        Rectangle:
                            source:'assets/background/speaker.png'
                            pos:self.pos
                            size:self.size
                    radius:[50,]



'''
class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition=FadeTransition()
class ledApp(MDApp):
    def build(self):
        LabelBase.register(name='Digital',fn_regular='assets/fonts/DS-DIGIB.TTF')
        self.theme_cls.font_styles["Digital"] =[
            "Digital",
            30,
            False,
            0.30,
            ]
        sc=Builder.load_string(kv)
        self.shuffle_icon=sc.ids.shuffle_icon
        self.repeat_icon=sc.ids.repeat_icon
        self.play_icon=sc.ids.play_icon
        self.pause_icon=sc.ids.pause_icon
        self.stop_icon=sc.ids.stop_icon
        self.tracks=sc.ids.tracks
        self.usb=sc.ids.usb
        self.tft=sc.ids.tft
        self.bt=sc.ids.bt
        self.labelabout=sc.ids.about
        self.sm=sc
        self.loadings=sc.ids.loadings

        self.labelabout.text="this app is designed as an MP3 music player that display LED visual effects only \n - it plays audio from your device storage (C ) \n - USB mode supports OTG device(still in testing) \n - TFT mode is intented for memory card access(not fully tested) \n NOTE: this app focuses only on LED output "

        
        self.repeat=False
        self.shuffle=False
        self.playing_song=0
        self.list_song=[]
        self.stopped=False
        self.paused=False
        self.display_time=False
        self.index_song=None
        self.shuffled=[]
        self.load=0
        Clock.schedule_interval(self.load_screens,1/10)
    
        return sc
    def load_screens(self,dt):
        self.load+=2
        if self.load<15:
            self.loadings.text=f'[_{self.load}%]'
        elif self.load<35:
            self.loadings.text=f'[__{self.load}%]'
        elif self.load<45:
            self.loadings.text=f'[___{self.load}%]'
        elif self.load<55:
            self.loadings.text=f'[____{self.load}%]'
        elif self.load<65:
            self.loadings.text=f'[_____{self.load}%]'
        elif self.load<85:
            self.loadings.text=f'[______{self.load}%]'
        elif self.load<95:
            self.loadings.text=f'[_______{self.load}%]'
        elif self.load<100:
            self.loadings.text=f'[________{self.load}%]'
        
        else:
            Clock.unschedule(self.load_screens)
            self.loadings.text='[_________done%]'
            Clock.schedule_once(self.go_screens,1)
            self.set_up_on_load()
    def go_screens(self,dt):
        self.sm.current='home'


    def menu_items(self,bt):
        items_list=[
            {'text':'about','on_release': lambda :self.app_about()},
            {'text':'exit','on_release': lambda :self.app_exit()}
        ]
        self.menu=MDDropdownMenu(
            items=items_list,
            caller=bt
        )
        self.menu.open()
    
    def app_about(self):
        self.menu.dismiss()
        self.sm.current='about'

    def app_exit(self):
        self.menu.dismiss()
        sys.exit()
        
    def load_song(self):
        self.list_song=[]
        self.shuffled=[]
        if os.path.exists(self.sd):
            for root,dirs,files in os.walk(self.sd):
                mp3s=[file for file in files if file.endswith(('.mp3'))]
                if mp3s:
                    for mp3 in mp3s:
                        self.list_song.append(os.path.join(root,mp3))
                else:
                    self.tracks.text='No files'
                
                 
        else:
            self.tracks.text=f'no drive'

        if self.list_song:
            if self.shuffle:
                self.shuffled=[i for i in range(len(self.list_song))]
                random.shuffle(self.shuffled)
            else: 
                self.shuffled=[i for i in range(len(self.list_song))]
            self.song_play()
        
    def set_shuffle(self):
        if self.shuffle:
            self.shuffle=False
            self.shuffle_icon.color='gray'
            if self.list_song:
                self.shuffled=[]
                self.shuffled=[i for i in range(len(self.list_song))]
        else:
            self.shuffle=True
            self.shuffle_icon.color='red'
            if self.list_song:
                self.shuffled=[]
                self.shuffled=[i for i in range(len(self.list_song))]
                random.shuffle(self.shuffled)
        
    def set_repeat(self):
        if self.repeat:
            self.repeat=False
            self.repeat_icon.color='gray'
        else:
            self.repeat=True
            self.repeat_icon.color='red'
    
    def set_mode(self):
        Clock.unschedule(self.music_time)
        self.play_icon.color='gray'
        self.pause_icon.color='gray'
        self.stop_icon.color='gray'
        try:
            mixer.music.stop()
        except:
            pass
        if self.mode==1:
            self.mode=2
            try:
                mixer.music.stop()
                mixer.music.load('assets/template/tft.ogg')
                mixer.music.play()
            except:
                pass
        elif self.mode==2:
            self.mode=3
            try:
                mixer.music.stop()
                mixer.music.load('assets/template/c.ogg')
                mixer.music.play()
            except:
                pass
        elif self.mode==3:
            self.mode=1
            try:
                mixer.music.stop()
                mixer.music.load('assets/template/usb.ogg')
                mixer.music.play()
            except:
                pass
        self.changes_load()
        
        
    ###################
    def set_up_on_load(self):
        self.mode=3
        try:
            mixer.music.load('assets/template/c.ogg')
            mixer.music.play()
        except:
            pass
        self.changes_load()
        
    def changes_load(self):
        if self.mode==1:
            self.usb.text_color='red'
            self.tft.text_color='gray'
            self.bt.text_color='gray'
            self.tracks.text='usb'
            if os.path.exists('/storage/usb'):
                self.sd='/storage/usb'
            else:
                self.sd='/storage/otg'
            confirm=time.time()
            self.mode_now=confirm
            self.usb_reffer=confirm
            self.modded=confirm
            Clock.schedule_once(self.go_there_usb,4)
        elif self.mode==2:
            self.usb.text_color='gray'
            self.tft.text_color='red'
            self.bt.text_color='gray'
            self.tracks.text='tft'
            if os.path.exists('/mnt/sdcard/external_sd/'):
                self.sd='/mnt/sdcard/external_sd/'
            elif os.path.exists('/mnt/external_sd/'):
                self.sd='/mnt/external_sd/'
            elif os.path.exists('/mnt/extSdCard/'):
                self.sd='/mnt/extSdCard/'
            else:
                self.sd='/storage/sdcard1'
            confirm=time.time()
            self.mode_now=confirm
            self.tft_reffer=confirm
            self.modded=confirm
            Clock.schedule_once(self.go_there_tft,4)
            
        elif self.mode==3:
            self.usb.text_color='gray'
            self.tft.text_color='gray'
            self.bt.text_color='red'
            self.tracks.text='Load..'
            if os.path.exists('/mnt/sdcard/'):
                self.sd='/mnt/sdcard/'
            elif os.path.exists('/sdcard/'):
                self.sd='/sdcard/'
            elif os.path.exists('/mnt/sdcard/emulated/0/'):
                self.sd='/mnt/sdcard/emulated/0/'
            else:
                self.sd='/storage/sdcard0'
            confirm=time.time()
            self.mode_now=confirm
            self.c_reffer=confirm
            self.modded=confirm
            Clock.schedule_once(self.go_there_c,4)
            

    def song_play(self):
        selected=self.shuffled[self.playing_song]
        self.now_playing=self.list_song[selected]
        self.stopped=False
        self.paused=False
        mixer.music.stop()
        try:
            mixer.music.load(self.now_playing)
            mixer.music.play()
            self.play_icon.color='red'
            self.pause_icon.color='gray'
            self.stop_icon.color='gray'

        except:
            self.next_song()
        self.information()
    def information(self):
        for index,file in enumerate(self.list_song,start=1):
            if file==self.now_playing:
                self.tracks.text=f'{index}/{len(self.list_song)}'
                self.index_song=index
        Clock.schedule_interval(self.music_time,1)
            

    def next_song(self):
        if self.list_song:
            Clock.unschedule(self.music_time)
            if not self.shuffle:
                if self.index_song:
                    self.playing_song=self.index_song-1

            if self.playing_song < len(self.list_song) -1:
                self.playing_song+=1
            else:
                self.playing_song=0
            self.song_play()

    def previous_song(self):
        if self.list_song:
            Clock.unschedule(self.music_time)
            if not self.shuffle:
                if self.index_song:
                    self.playing_song=self.index_song-1

            if self.playing_song > 0:
                self.playing_song-=1
            else:
                self.playing_song=len(self.list_song)-1
            self.song_play()

    def music_time(self,dt):
        if self.mode_now==self.modded:
            song=mixer.music.get_pos()/1000
            if song < 0:
                if self.repeat:
                    self.song_play()
                else:
                    self.next_song()
            else:
                if song < 3600:
                    mm,ss=divmod(song,60)
                    self.tracks.text=f"{int(mm):02d}:{int(ss):02d}"
                else:
                    mm,ss=divmod(song,60)
                    hh,mm=divmod(mm,60)
                    self.tracks.text=f"{int(hh):02d}:{int(mm):02d}:{int(ss):02d}"
                
    def play_button(self):
        if not self.stopped:
            if self.paused:
                try:
                    mixer.music.unpause()
                    self.paused=False
                    self.play_icon.color='red'
                    self.pause_icon.color='gray'
                    self.stop_icon.color='gray'

                except:
                    pass
            else:
                mixer.music.pause()
                self.paused=True
                self.play_icon.color='gray'
                self.pause_icon.color='red'
                self.stop_icon.color='gray'
        else:
            try:
                mixer.music.play()
                self.stopped=False
                self.paused=False
                self.play_icon.color='red'
                self.pause_icon.color='gray'
                self.stop_icon.color='gray'
                Clock.schedule_interval(self.music_time,1)

                
            except:
                pass
    def stop_button(self):
        if self.list_song:
            if not self.stopped:
                try:
                    mixer.music.stop()
                    Clock.unschedule(self.music_time)
                    self.stopped=True
                    self.play_icon.color='gray'
                    self.pause_icon.color='gray'
                    self.stop_icon.color='red'
                except:
                    pass

    def go_there_tft(self,dt):
        if self.mode_now==self.tft_reffer:
            self.load_song()
    def go_there_usb(self,dt):
        if self.mode_now==self.usb_reffer:
            self.load_song()
    def go_there_c(self,dt):
        if self.mode_now==self.c_reffer:
            self.load_song()

    def open_fb(self):
        url="www.facebook.com"
        webbrowser.open(url)
    def open_wap(self):
        url="www.whatsapp.com/channel/0029VbAYoDIHVvTgvybf173F"
        webbrowser.open(url)
    def open_gh(self):
        url="www.github.com/mwacha3"
        webbrowser.open(url)
        
if __name__=='__main__':
    ledApp().run()
