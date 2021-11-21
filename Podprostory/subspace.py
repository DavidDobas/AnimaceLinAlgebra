from manim import *

class Subspace(VectorScene):
    def construct(self):
        title = Tex(r"Podprostory v $\mathbb{R}^2$ nad $\mathbb{R}$").scale(1.2)
        self.add(title)
        self.wait(5)

        first = MathTex(r"1)\: P\subset\mathbb{R}^2").shift(1.5*LEFT + 1.6*UP)
        second = MathTex(r"2)\: P\neq\emptyset").align_to(first, LEFT).shift(0.6*UP)
        third = MathTex(r"3)\: (\forall\vec{x}, \vec{y} \in P)(\vec{x} + \vec{y} \in P)")
        third.shift(0.4*DOWN).align_to(first, LEFT)
        fourth = MathTex(r"4)\: (\forall\alpha\in \mathbb{R}, \forall\vec{y} \in P)(\alpha\vec{x} \in P)")
        fourth.shift(1.4*DOWN).align_to(first, LEFT)
        zero = MathTex(r"\alpha = 0 \Rightarrow \vec{0} \in P")
        zero.shift(2*DOWN).align_to(first, LEFT).shift(1*RIGHT).scale(0.8)
        
        self.play(ApplyMethod(title.shift, 2.5*UP))
        self.play(Write(first))
        self.wait(4)
        self.play(Write(second))
        self.wait(2)
        self.play(Write(third))
        self.wait(4)
        self.play(Write(fourth))
        self.wait(4)
        self.play(Write(zero))
        self.wait(5)
        """group = VGroup(first, second, third, fourth)
        first_moved = MathTex(r"1)\: P\subset\mathbb{R}^2").add_background_rectangle()
        first_moved.scale(0.5).shift(6*LEFT + 3.5*UP)
        second_moved = MathTex(r"2)\: P\neq\emptyset").align_to(first, LEFT)
        second_moved.scale(0.5).shift(3*UP).align_to(first_moved, LEFT).add_background_rectangle()
        third_moved = MathTex(r"3)\: (\forall\vec{x}, \vec{y} \in P)(\vec{x} + \vec{y} \in P)")
        third_moved.scale(0.5).shift(2.5*UP).align_to(first_moved, LEFT).add_background_rectangle()
        fourth_moved = MathTex(r"4)\: (\forall\alpha\in \mathbb{R}, \forall\vec{x} \in P)(\alpha\vec{x} \in P)").scale(0.5)
        fourth_moved.shift(2.*UP).align_to(first_moved, LEFT).add_background_rectangle()
        group_moved = VGroup(first_moved, second_moved, third_moved, fourth_moved)
        self.play(FadeOut(title), ReplacementTransform(group, group_moved))"""
        self.play(FadeOut(title, first, second, third, fourth, zero))
        self.wait(1)

        plane = NumberPlane()
        plane.add_coordinates()
        plane.set_z_index(0)
        self.play(Create(plane))

        self.wait(3)
        
        def create_vect(array, color, label):
            x = array
            vec = Vector(x, color=color).set_z_index(2)
            vec_label = label
            shift = [0,0.3,0] if x[1]>0 else [0,-0.3,0]
            vec_label.move_to(x+0.3*x/np.linalg.norm(x)+shift)
            return vec, vec_label

        def rotated_cos(t):
            return 0.5*np.array((np.sqrt(2)/2*t - np.sqrt(2)/2*np.cos(t), np.sqrt(2)/2*t + np.sqrt(2)/2*np.cos(t),0))
        cos_fc = ParametricFunction(rotated_cos, t_range = np.array([-20,20]), fill_opacity=0).set_color(WHITE)
        self.play(FadeIn(cos_fc))
        self.wait(4)
        self.play(FadeOut(cos_fc))
        
        self.wait(1)
        sin_fc = FunctionGraph(lambda t: np.sin(t)).set_color(WHITE)
        self.play(FadeIn(sin_fc))
        self.wait(3)
        
        def add_arrow(array, color, label):
            vec, lab = create_vect(array, color, label)
            x = VGroup(vec, lab)
            self.play(GrowArrow(vec), FadeIn(lab))
            self.wait(1)
            return x
        
        x_array = np.array([1,np.sin(1),0])
        x = add_arrow(x_array, GREEN, MathTex(r"\vec{x}"))

        y_array = np.array([3,np.sin(3),0])
        y = add_arrow(y_array, BLUE, MathTex(r"\vec{y}"))

        z_array = x_array + y_array
        z_vec, z_label = create_vect(z_array, YELLOW, MathTex(r"\vec{x}+\vec{y}"))
        x_line = Line(start=z_array, end=x_array, color=WHITE).set_opacity(0.3)
        y_line = Line(start=z_array, end=y_array, color=WHITE).set_opacity(0.3)
        self.play(FadeIn(x_line, y_line))
        self.play(GrowArrow(z_vec), FadeIn(z_label))
        self.wait(4)

        self.play(FadeOut(x, y, z_vec, z_label, x_line, y_line))
        self.wait(5)

        line_x = FunctionGraph(lambda t: 2/3*t).set_color(WHITE).set_opacity(0.7)
        self.play(ReplacementTransform(sin_fc, line_x))
        
        self.wait(5)
        x_array = 0.7*np.array([3,2,0])
        x = add_arrow(x_array, GREEN, MathTex(r"\vec{x}"))
        self.wait(8)

        line_y = FunctionGraph(lambda t: -1/4*t).set_color(WHITE).set_opacity(0.7)
        self.play(FadeIn(line_y))
        
        y_array = 0.7*np.array([4,-1,0])
        self.wait(3)

        def sector_func(u,v):
            return u*x_array + v*y_array
        sector = Surface(sector_func, u_range=[0,5], v_range=[0,5], fill_opacity=0.5, fill_color=GREY)
        self.play(FadeIn(sector))
        self.wait(3)
        y = add_arrow(y_array, RED, MathTex(r"\vec{y}"))

        z_array = x_array + y_array
        z_vec, z_label = create_vect(z_array, YELLOW, MathTex(r"\vec{x}+\vec{y}"))
        x_line = Line(start=z_array, end=x_array, color=WHITE).set_opacity(0.3)
        y_line = Line(start=z_array, end=y_array, color=WHITE).set_opacity(0.3)
        self.play(FadeIn(x_line, y_line))
        self.wait(1)
        self.play(GrowArrow(z_vec), FadeIn(z_label))
        self.wait(5)
        
        def different_sums(previous_group, x_array, y_array, alpha, beta):
            z_array = alpha*x_array + beta*y_array
            x = VGroup(*create_vect(alpha*x_array, GREEN, MathTex(r"\vec{x}")))
            y = VGroup(*create_vect(beta*y_array, RED, MathTex(r"\vec{y}")))
            z_vec, z_label = create_vect(z_array, YELLOW, MathTex(r"\vec{x}+\vec{y}"))
            x_line = Line(start=z_array, end=alpha*x_array, color=WHITE).set_opacity(0.3)
            y_line = Line(start=z_array, end=beta*y_array, color=WHITE).set_opacity(0.3)
            z_group = VGroup(x, y, z_vec, z_label, x_line, y_line).set_z_index(1)
            self.play(ReplacementTransform(previous_group, z_group))
            return z_group
        
        group = VGroup(x, y, z_vec, z_label, x_line, y_line)
        x_coeffs = [1.1, 0.8]
        y_coeffs = [0.4, 1]
        for a, b in zip(x_coeffs, y_coeffs):
            group = different_sums(group, x_array, y_array, a, b)
            self.wait(2)

        x_array_new = 0.5*np.array([3,2,0]) + 0.2*np.array([4,-1,0])
        y_array_new = 0.2*np.array([3,2,0]) + 0.7*np.array([4,-1,0])
        group = different_sums(group, x_array_new, y_array_new, 1, 1)
        self.wait(2)
        x_array_new = 0.7*np.array([3,2,0]) + 0.2*np.array([4,-1,0])
        y_array_new = 0.3*np.array([3,2,0]) + 0.5*np.array([4,-1,0])
        group = different_sums(group, x_array_new, y_array_new, 1, 1)
        self.wait(2)
        group = different_sums(group, x_array, y_array, 0.8, 0.6)
        self.wait(2)
        
        
        self.wait(3)
        group = different_sums(group, x_array, y_array, -0.8, -0.6)
        self.wait(3)
        
        sector2 = Surface(sector_func, u_range=[-5,0], v_range=[-5,0], fill_opacity=0.5, fill_color=GREY).set_z_index(0)
        self.play(FadeIn(sector2))
        self.wait(5)

        group = different_sums(group, x_array, y_array, 0.8, -0.6)
        self.wait(2)

        sector3 = Surface(sector_func, u_range=[5,0], v_range=[-5,0], fill_opacity=0.5, fill_color=GREY).set_z_index(0)
        self.play(FadeIn(sector3))
        self.wait(2)

        group = different_sums(group, x_array, y_array, -0.8, 0.6)
        self.wait(2)

        sector4 = Surface(sector_func, u_range=[-5,0], v_range=[5,0], fill_opacity=0.5, fill_color=GREY).set_z_index(0)
        self.play(FadeIn(sector4))

        self.wait(5)


class SumOfSubspaces(VectorScene):
    def construct(self):
        def create_vect(array, color, label):
            x = array
            vec = Vector(x, color=color).set_z_index(2)
            vec_label = label
            shift = [0,0.3,0] if x[1]>0 else [0,-0.3,0]
            vec_label.move_to(x+0.3*x/np.linalg.norm(x)+shift)
            return vec, vec_label

        def add_arrow(array, color, label):
            vec, lab = create_vect(array, color, label)
            x = VGroup(vec, lab)
            self.play(GrowArrow(vec), FadeIn(lab))
            self.wait(1)
            return x
        
        plane = NumberPlane()
        plane.add_coordinates()
        plane.set_z_index(0)
        self.play(Create(plane))

        sum = MathTex(r"A+B:=\{\vec{a}+\vec{b}\ |\ \vec{a}\in A, \vec{b}\in B\}").shift(3.5*LEFT + 3.5*UP).add_background_rectangle()
        self.play(FadeIn(sum))
        self.wait(20)

        lineP = FunctionGraph(lambda t: 2/3*t).set_color(WHITE).set_opacity(0.7)
        labelP = MathTex("P").shift(4.9*RIGHT + 2.8*UP)
        self.play(FadeIn(lineP, labelP))
        lineQ = FunctionGraph(lambda t: -2/5*t).set_color(WHITE).set_opacity(0.7)
        labelQ = MathTex("Q").shift(6*RIGHT + 1.9*DOWN)
        self.play(FadeIn(lineQ, labelQ))
        self.wait(1)

        x_array = 3/4*np.array([3,2,0])
        x = add_arrow(x_array, GREEN, MathTex(r"\vec{x}"))

        y_array = 1/2*np.array([5,-2,0])
        y = add_arrow(y_array, BLUE, MathTex(r"\vec{y}"))

        self.wait(2)

        z_array = x_array + y_array
        z_vec, z_label = create_vect(z_array, YELLOW, MathTex(r"\vec{x}+\vec{y}"))
        x_line = Line(start=z_array, end=x_array, color=WHITE).set_opacity(0.3)
        y_line = Line(start=z_array, end=y_array, color=WHITE).set_opacity(0.3)
        self.play(FadeIn(x_line, y_line))
        self.wait(1)
        self.play(GrowArrow(z_vec), FadeIn(z_label))
        self.wait(5)
        group = VGroup(x, y, z_vec, z_label, x_line, y_line)

        def different_sums(previous_group, x_array, y_array, alpha, beta):
            z_array = alpha*x_array + beta*y_array
            x = VGroup(*create_vect(alpha*x_array, GREEN, MathTex(r"\vec{x}")))
            y = VGroup(*create_vect(beta*y_array, BLUE, MathTex(r"\vec{y}")))
            z_vec, z_label = create_vect(z_array, YELLOW, MathTex(r"\vec{x}+\vec{y}"))
            x_line = Line(start=z_array, end=alpha*x_array, color=WHITE).set_opacity(0.3)
            y_line = Line(start=z_array, end=beta*y_array, color=WHITE).set_opacity(0.3)
            z_group = VGroup(x, y, z_vec, z_label, x_line, y_line)
            self.play(ReplacementTransform(previous_group, z_group))
            return z_group
        
        x_coeffs = [1.1, 0.8, -0.5, 1.4]
        y_coeffs = [1.4, -1.2, 1.1, -0.5]
        for a, b in zip(x_coeffs, y_coeffs):
            group = different_sums(group, x_array, y_array, a, b)
            self.wait(2)
        
        self.wait(2)
        