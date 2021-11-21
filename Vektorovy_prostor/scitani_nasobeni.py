from manim import *

class Scitani_nasobeni(Scene):
    def construct(self):
        title = Tex(r"Vektory v $\mathbb{R}^2$ nad $\mathbb{R}$")
        title.add_background_rectangle()
        title.set_z_index(2)
        vector_numbers = MathTex(r"\vec{x} = \begin{pmatrix}x_1\\x_2\end{pmatrix}")
        self.add(title)
        self.wait(5)
        self.play(ApplyMethod(title.shift, 1*UP))
        self.play(Write(vector_numbers))
        self.wait(5)
        plane = NumberPlane()
        plane.add_coordinates()
        plane.set_z_index(0)
        self.play(FadeOut(vector_numbers))
        self.play(ApplyMethod(title.shift, 2*UP, 4.5*LEFT))
        self.wait(1)
        x_tex = MathTex(r"\vec{x} = \begin{pmatrix}3\\2\end{pmatrix}")
        x_tex.shift(2*UP + 5.5*LEFT)
        x_tex.add_background_rectangle()
        x_tex.set_z_index(2)
        self.play(FadeIn(x_tex))
        self.wait(2)
        
        self.play(Create(plane))
        self.wait(3)
        point = Circle(radius=0.05, color=RED, fill_opacity=1)
        point.shift(3*RIGHT, 2*UP)
        x = np.array([3, 2, 0])
        x_vec = Vector(direction=x, color = RED)
        x_label = MathTex(r"\vec{x}")
        x_label.move_to(x_vec.get_end()+0.3*x/np.linalg.norm(x))

        self.play(FadeIn(point, x_label))
        self.wait(3)
        
        self.play(GrowArrow(x_vec), FadeOut(point))
        self.wait(5)

        title2 = Tex(r"Sčítání vektorů").shift(3*UP).add_background_rectangle().align_to(title, LEFT)
        y_tex = MathTex(r"\vec{y} = \begin{pmatrix}2\\-3\end{pmatrix}")
        y_tex.align_to(x_tex, LEFT)
        y_tex.shift(0.6*UP)
        y_tex.add_background_rectangle().set_z_index(2)
        y = np.array([2, -3, 0])
        y_vec = Vector(direction=y, color = YELLOW)  
        y_label = MathTex(r"\vec{y}").move_to(y_vec.get_end()+0.2*y/np.linalg.norm(y))
        self.play(FadeIn(y_tex, y_label), GrowArrow(y_vec), ReplacementTransform(title, title2))
        self.wait(3)

        sum_tex = MathTex(r"\vec{x} + \vec{y} = \begin{pmatrix}3+2\\2-3\end{pmatrix} = \begin{pmatrix}5\\-1\end{pmatrix}")
        sum_tex.align_to(x_tex, LEFT).shift(1*DOWN).add_background_rectangle()
        self.play(Create(sum_tex))
        self.wait(7)

        y_copy = Vector(direction=[2, -3, 0], color = YELLOW).set_z_index(1).set_opacity(0.3)
        self.add(y_copy)
        self.play(ApplyMethod(y_vec.shift, x))
        self.wait(3)

        sum = np.array(x+y)
        sum_vec = Vector(direction=sum, color = GREEN)
        self.play(GrowArrow(sum_vec))
        sum_label = MathTex(r'\vec{x}+\vec{y}').move_to(sum_vec.get_end()+0.2*sum/np.linalg.norm(sum)).shift(0.4*DOWN)
        self.play(FadeIn(sum_label))
        self.wait(3)

        self.play(FadeOut(y_vec, y_label, y_copy, y_tex, sum_vec, sum_label, sum_tex))
        title3 = Tex(r"Násobení vektoru číslem").shift(3*UP).add_background_rectangle().align_to(title, LEFT)
        self.play(ReplacementTransform(title2, title3))
        self.wait(3)
        
        alpha_tex =  MathTex(r'\alpha=\frac{1}{2}').align_to(x_tex, LEFT).shift(0.6*UP).add_background_rectangle()
        self.play(Create(alpha_tex))
        alpha = 0.5

        multiplicate = MathTex(r'\alpha\cdot\vec{x} = \begin{pmatrix}\frac{1}{2}\cdot 3 \\[0.5em]\frac{1}{2}\cdot 2\end{pmatrix} = \begin{pmatrix}\frac{3}{2}\\[0.3em]1\end{pmatrix}')
        multiplicate.align_to(x_tex, LEFT).shift(1*DOWN).add_background_rectangle()
        self.play(Create(multiplicate))
        self.wait(5)

        x_group = VGroup(x_vec, x_label)
        alpha_x = alpha*x
        alpha_x_vec = Vector(alpha_x, color=GREEN)
        alpha_x_label = MathTex(r'\alpha\cdot\vec{x}').move_to(alpha_x + 0.2*alpha_x/np.linalg.norm(alpha_x)).shift(0.2*UP)
        alpha_x_group = VGroup(alpha_x_vec, alpha_x_label)
        self.play(ReplacementTransform(x_group, alpha_x_group))
        self.wait(5)

        beta_tex =  MathTex(r'\beta=-\frac{3}{2}').align_to(x_tex, LEFT).shift(0.6*UP).add_background_rectangle()
        self.play(ReplacementTransform(alpha_tex, beta_tex), ReplacementTransform(alpha_x_group, x_group))
        beta = -3/2

        multiplicate2 = MathTex(r'\beta\cdot\vec{x} = \begin{pmatrix}-\frac{9}{2}\\[0.3em]-3\end{pmatrix}')
        multiplicate2.align_to(x_tex, LEFT).shift(1*DOWN).add_background_rectangle()
        self.play(ReplacementTransform(multiplicate, multiplicate2))
        self.wait(5)

        beta_x = beta*x
        beta_x_vec = Vector(beta_x, color=YELLOW)
        beta_x_label = MathTex(r'\beta\cdot\vec{x}').move_to(beta_x + 0.2*beta_x/np.linalg.norm(beta_x)).shift(0.2*DOWN)
        beta_x_group = VGroup(beta_x_vec, beta_x_label)

        self.play(ReplacementTransform(x_group, beta_x_group))
        self.wait(8)