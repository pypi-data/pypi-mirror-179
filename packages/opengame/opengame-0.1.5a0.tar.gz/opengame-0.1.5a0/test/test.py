import unittest


class OpenGameTestCase(unittest.TestCase):
    def test_window_show(self):
        import opengame as og
        window = og.Window()
        try:
            window.show()
        except SystemExit:
            return
        
    def test_sprite_move(self):
        import opengame as og
        window = og.Window()
        bird = og.Sprite('bird.png', (120, 80))
        @window.when_draw
        def draw():
            bird.show()
            if window.rates(20):
                bird.rotate(10)
                bird.forward(10)
        try:
            window.show()
        except SystemExit:
            return
        
    def test_background_rolling(self):
        import opengame as og
        window = og.Window()
        background1 = og.Background('grassland.png')
        background2 = background1.clone()
        background2.x = 240
        
        @window.when_draw
        def draw():
            background1.show()
            background2.show()
            background1.scroll_right()
            background2.scroll_right()
        try:
            window.show()
        except SystemExit:
            return
        
    def test_label(self):
        import opengame as og
        window = og.Window()
        label = og.Label('hello world')
        label.pack()
        try:
            window.show()
        except SystemExit:
            return
        
    def test_translate(self):
        import opengame as og
        translator = og.translate.Translator(
            input_language=og.translate.languages.france,
            cookies='BIDUPSID=101765CAE51AF93F923C469FA36DC67E; PSTM=1641645875; __yjs_duid=1_019e1b4964d26594bf17d330ca32ddee1641645902504; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; BAIDUID=3BF7E2AD42CBEC1E0F6DBE34C0ED3B3F:FG=1; BDUSS=mpGOS1rU25GeWRFSmxsZ2xBTXUwUlZyeTZtS2pPQ2pUWWNiUGIyMVY4UThqUzVqRVFBQUFBJCQAAAAAAAAAAAEAAAAy6mEp17PC6DIwMDkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwAB2M8AAdjQ; BDUSS_BFESS=mpGOS1rU25GeWRFSmxsZ2xBTXUwUlZyeTZtS2pPQ2pUWWNiUGIyMVY4UThqUzVqRVFBQUFBJCQAAAAAAAAAAAEAAAAy6mEp17PC6DIwMDkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwAB2M8AAdjQ; MCITY=-176%3A; BAIDUID_BFESS=3BF7E2AD42CBEC1E0F6DBE34C0ED3B3F:FG=1; BA_HECTOR=8g2l01a1a501akak2h041o261hjq6vg1b; ZFY=Zs1KJ6uhYvF4v1uuS0xw36gTzQtD8Bu90OL4i1PA:Ba4:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=37152_36555_37352_37299_36885_34813_37486_37403_37404_36789_37500_26350_37285_37466; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; delPer=0; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664780207,1664782859,1664794173,1664973016; ab_sr=1.0.1_OGQwZjYwZjVhMTZjZWEwODkxMWQ3OTZkMTNiZmM3ZDAxMDcxMzkxZWE4ODYzYTAyZGFjZTc5N2ZhOTdlNmYyMDUxODUyYmMyNzgwNDEwM2JjYzY3OTlhYzQyZDcxYzRlMTdjMmRmYmRhNWE3ZGI2OGQ1MjM5MGZjZDBlNDg4NzlkZmFhNGQ0YTIzMzNmNDE3MzViMWY3ZmRlNjBmZmZhOWYwNjM4MTFhZWE5MzEyNzczN2NjOGI0NjBlNmRiMmU3; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664973090'
        )
        translator.load('Je suis un chat.')
        print(translator.get())
        
    def test_math(self):
        import opengame as og
        test = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
        ]
        flat = og.math.flatten(test)
        self.assertEqual(flat, list(range(1, 16)))
        self.assertEqual(og.math.chunk(flat, 5), test)
        self.assertEqual(og.math.duplicate_removal([1, 1, -1, 9], True), [1, -1, 9])
        self.assertEqual(og.math.find(test, 1), (0, 0))
        for case in og.math.switch(404):
            if case(400):
                self.assertEqual(0, 1)
                break
            if case(200, 300):
                self.assertEqual(0, 2)
                break
            if case(404):
                self.assertEqual(2, 2)
                break

    def test_screencap(self):
        import opengame as og
        window = og.Window()
        label = og.Label('0')
        label.pack()
        screencap = og.screencap.Screencap()
        
        @window.when_draw
        def draw():
            screencap.record()
            if window.rates(30):
                label.set_text(og.random.randint(1, 10))
            if og.timer.time > 10:
                screencap.save()
                window.destroy()
                
        try:
            window.show()
        except SystemExit:
            return
        
    def test_camera(self):
        import opengame as og
        window = og.Window()
        camera = og.Camera(auto_start=True)
        camera.pack()

        @window.when_draw
        def draw():
            camera.record()
            
        try:
            window.show()
        except SystemExit:
            return
        
    def test_web_view(self):
        import opengame as og
        window = og.Window()
        og.WebView(url='www.baidu.com')
        try:
            window.show()
        except SystemExit:
            return
        
    def test_window_gl(self):
        import opengame as og
        window = og.GLWindow(style=og.styles.resizable)
        
        gl, glu = window.gl, window.glu
        glu.gluPerspective(45, window.width / window.height, 0.1, 50.0)
        gl.glTranslatef(0.0, 0.0, -5.0)

        vertices = ((1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1))
        quads = ((0, 3, 6, 4), (2, 5, 6, 3), (1, 2, 5, 7), (1, 0, 4, 7), (7, 4, 6, 5), (2, 3, 0, 1))

        @window.when_draw
        def draw():
            gl.glRotatef(1, 1, 1, 1)
            gl.glBegin(gl.GL_QUADS)
            for q in quads:
                for v in q:
                    gl.glVertex3fv(vertices[v])
            gl.glEnd()
            
        try:
            window.show()
        except SystemExit:
            return
        
    def test_rich_text(self):
        import opengame as og
        window = og.Window()
        og.RichText(file='richtext.rtf')
        try:
            window.show()
        except SystemExit:
            return
        
    def test_video(self):
        import opengame as og
        window = og.Window(size=(800, 450))
        video = og.Video('test.mp4', (800, 450))
        video.pack()
        
        @window.when_draw
        def draw():
            video.read()
        
        try:
            window.show()
        except SystemExit:
            return
        
    def test_entry(self):
        import opengame as og
        window = og.Window(fps=50)
        entry = og.Entry()
        entry.start()
        entry.pack()
        
        try:
            window.show()
        except SystemExit:
            return
        
    def test_child(self):
        import time
        import subprocess
        import win32gui
        import opengame as og
        
        window = og.Window()
        subprocess.Popen('notepad')
        time.sleep(3)
        notepad = win32gui.FindWindow(0, 'notepad')

        child = og.Child(notepad)
        child.pack()
        
        try:
            window.show()
        except SystemExit:
            return
        
    def test_random_bar(self):
        import opengame as og
        window = og.Window()
        bar = og.Bar()
        bar.pack()
    
        @window.when_draw
        def draw():
            if window.rates(15):
                bar.set_proportion(og.random.random())
    
        try:
            window.show()
        except SystemExit:
            return

    def test_pen(self):
        import opengame as og
        window = og.Window()
        pen = og.Pen()
    
        @window.when_draw
        def draw():
            pen.rect((0, 0, 0), (-40, -40), (20, 20))
            pen.circle((255, 0, 0), (0, 0), 15)
            pen.line((0, 255, 0), (100, 80), (-80, -60))
            pen.ellipse((0, 0, 255), (105, 85), (60, 25))
            pen.polygon((128, 128, 128), [(-80, -80), (-80, -120), (-160, -120)])
            pen.arc((128, 0, 0), (-120, 0), 40, 0, 120)
            pen.pie((0, 128, 0), (-120, 100), 40, 0, 120)
            pen.bezier((0, 0, 128), [(100, -120), (80, -150), (70, -130)], 40)
    
        try:
            window.show()
        except SystemExit:
            return


if __name__ == '__main__':
    unittest.main()
