from manim import *

class CameraTricks(VectorScene, MovingCameraScene):
    def construct(self):
        title = Tex(r"Doplněk podprostoru $\mathbb{R}^2$ nad $\mathbb{R}$").scale(1.2)
        self.add(title)
        self.wait(5)

        first = MathTex(r"P,Q \subset\subset \mathbb{R}^2").shift(1*UP)
        second = Tex(r"$Q$ je doplňkem $P\ \iff \ P \oplus Q = \mathbb{R}^2$").shift(0.2*UP)
        
        self.play(ApplyMethod(title.shift, 2*UP))
        self.play(Write(first))
        self.wait(4)
        self.play(Write(second))
        self.wait(5)

        self.play(FadeOut(title, first, second))
        self.wait(1)

        plane = NumberPlane(x_range=[-20, 20, 1],
                            y_range=[-20, 20, 1],)
        plane.add_coordinates()
        plane.set_z_index(0)
        self.play(Create(plane))
        self.play(self.camera.frame.animate.set(width=20))
        vector=(2,3)
        self.add_vector(vector)
        self.wait(3)
        self.play(self.camera.frame.animate.move_to(2*RIGHT))
        self.wait(5)