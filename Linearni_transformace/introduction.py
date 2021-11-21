from manim import *
from imports.vectors_creation import create_vect, create_sum_lines

class Intro1D(Scene):
    def construct(self):
        title = Tex(r"Lineární zobrazení v $\mathbb{R}$ nad $\mathbb{R}$").scale(1.5)
        title.add_background_rectangle()
        self.add(title)
        self.wait(4)

        self.play(ApplyMethod(title.shift, 1.5*UP))

        definition = Tex(r"$A: \mathbb{R} \rightarrow \mathbb{R}$ je lineární zobrazení").shift(3*LEFT).scale(0.8)
        iff = MathTex(r"\Leftrightarrow").shift(0.1*RIGHT)
        first_ax = MathTex(r"(\forall x, y \in \mathbb{R})(A(x+y) = A(x) + A(y))").scale(0.8).shift(3.7*RIGHT + 0.3*UP)
        sec_ax = MathTex(r"(\forall \alpha, x \in \mathbb{R})(A(\alpha x) = \alpha A(x))").scale(0.8).align_to(first_ax, LEFT).shift(0.3*DOWN)
        self.play(Write(definition))
        self.wait(1)
        self.play(Write(iff))
        self.play(Write(first_ax))
        self.wait(2)
        self.play(Write(sec_ax))
        self.wait(5)

class Examples1D(VectorScene, Scene):
    def construct(self):
        ax = Axes(
            x_range=[-6, 10], y_range=[-3, 3], axis_config={"include_tip": False, "include_numbers": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="A(x)")
        self.add(ax, labels)
        self.wait(5)
        exp_fc = ax.plot(lambda t: np.exp(t)/5, color=BLUE)
        self.play(FadeIn(exp_fc))
        self.wait(5)
        tr_zero_tick = ax.y_axis.get_tick(1/5, size=0.05)
        self.add(tr_zero_tick)
        tr_zero_label = MathTex("A(0)").scale(0.7).shift(ax.c2p(0,1/5)).align_to(ax.y_axis.get_left(), RIGHT).shift(0.1*LEFT+0.1*UP)
        self.play(FadeIn(tr_zero_label))
        self.wait(3)
        self.play(FadeOut(exp_fc, tr_zero_tick, tr_zero_label))
        self.wait(1)
        def A(t): return np.sin(t)
        sin_fc = ax.plot(A, color=BLUE)
        self.play(FadeIn(sin_fc))
        self.wait(3)

        def point_with_coordinates(point, label):
            a = Dot(ax.coords_to_point(*point), color=WHITE).set_z_index(2)
            shift = 0.3*DOWN if point[1] > 0 else 0.3*UP
            a_tick = ax.x_axis.get_tick(point[0], size=0.05).set_z_index(2)
            a_label = MathTex(label).scale(0.7).align_to(ax.x_axis, DOWN).shift(ax.c2p(point[0],0) + shift)
            tr_a_tick = ax.y_axis.get_tick(point[1], size=0.05).set_z_index(2)
            tr_a_label = MathTex(f"A({label})").scale(0.7).shift(ax.c2p(0,point[1])).align_to(ax.y_axis.get_left(), RIGHT).shift(0.1*LEFT)
            lines = ax.get_lines_to_point(ax.c2p(*point))
            self.play(FadeIn(a, a_tick, a_label, tr_a_tick, tr_a_label, lines))
            return VGroup(a, a_tick, a_label, tr_a_tick, tr_a_label, lines)
        
        a = point_with_coordinates([2, A(2)], "a")
        self.wait(1)
        b = point_with_coordinates([2.7, A(2.7)], "b")
        self.wait(2)
        a_plus_b = point_with_coordinates([4.7, A(4.7)], "a+b")
        self.wait(4)
        tr_a_plus_tr_b_tick = ax.y_axis.get_tick(A(2) + A(2.7), size=0.05)
        #Dot(ax.coords_to_point(0, np.sin(2) + np.sin(2.7)), stroke_width=2,  fill_color=PURPLE)
        tr_a_plus_tr_b_label = MathTex("A(a) + A(b)").scale(0.7).shift(ax.c2p(0,A(2) + A(2.7))).align_to(ax.y_axis.get_left(), RIGHT).shift(0.1*LEFT)
        self.play(FadeIn(tr_a_plus_tr_b_tick, tr_a_plus_tr_b_label))
        self.wait(2)
        self.wait(3)
        self.play(FadeOut(a, b, a_plus_b, tr_a_plus_tr_b_tick, tr_a_plus_tr_b_label))
        self.wait(2)

        def A(t): return t/3
        lin_fc = ax.plot(A, color=BLUE)
        self.play(ReplacementTransform(sin_fc, lin_fc))
        self.wait(3)
        def lin_functions(function): 
            a = point_with_coordinates([2, function(2)], "a")
            self.wait(1)
            b = point_with_coordinates([3.5, function(3.5)], "b")
            self.wait(2)
            a_plus_b = point_with_coordinates([5.5, function(5.5)], "a+b")
            self.wait(2)
            tr_a_plus_b_label = MathTex(f"A(a) + A(b)").scale(0.7).shift(ax.c2p(0,function(5.5))).align_to(ax.y_axis.get_left(), RIGHT).shift(0.1*LEFT)
            self.play(ReplacementTransform(a_plus_b[4], tr_a_plus_b_label))
            self.wait(2)
            self.play(FadeOut(b, a_plus_b, tr_a_plus_b_label))
            self.wait(1)
            alpha = 2.4
            alpha_a = point_with_coordinates([alpha*2, function(alpha*2)], r"\alpha\cdot a")
            self.wait(2)
            tr_alpha_a = MathTex(r"\alpha\cdot A(a)").scale(0.7).shift(ax.c2p(0,function(alpha*2))).align_to(ax.y_axis.get_left(), RIGHT).shift(0.1*LEFT)
            self.play(ReplacementTransform(alpha_a[4], tr_alpha_a))
            self.wait(3)
            self.play(FadeOut(a, alpha_a, tr_alpha_a))

        lin_functions(A)
        self.wait(1)

        def A(t): return -t/4
        lin_fc2 = ax.plot(A, color=BLUE)
        self.play(ReplacementTransform(lin_fc, lin_fc2))
        self.wait(3)
        lin_functions(A)
        

class Intro2D(Scene):
    def construct(self):
        title = Tex(r"Lineární zobrazení v $\mathbb{R}^2$ nad $\mathbb{R}$").scale(1.5)
        title.add_background_rectangle()
        self.add(title)
        self.wait(5)

        self.play(ApplyMethod(title.shift, 1.5*UP))

        definition = Tex(r"$A: \mathbb{R}^2 \rightarrow \mathbb{R}^2$ je lineární zobrazení").shift(0.6*UP).scale(0.8)
        iff = MathTex(r"\Leftrightarrow").shift(0.1*DOWN)
        first_ax = MathTex(r"(\forall \alpha \in \mathbb{R}, \forall \vec{x}, \vec{y} \in \mathbb{R}^2)(A(\alpha\vec{x}+\vec{y}) = \alpha A\vec{x} + A\vec{y})").scale(0.8).shift(0.8*DOWN)
        self.play(Write(definition))
        self.wait(1)
        self.play(Write(iff))
        self.play(Write(first_ax))
        self.wait(8)

class NonLinear(Scene):
    def construct(self):

        grid = NumberPlane(x_range=[-20,20,1], y_range=[-20,20,1])
        grid.prepare_for_nonlinear_transform()
        self.add(grid)
        self.wait(6)
        def f(p):
            return [p[0]+p[1]**2, np.sin(p[0])-p[1], 0]
        self.play(
            grid.animate.apply_function(
                lambda p: f(p)
            ),
            run_time=3,
        )
        self.wait(6)

class Transformations2D(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        self.wait(1)
        x = 2/3*np.array([3,1,0])
        x_vec = self.add_vector(x, color=GREEN).set_z_index(2)
        self.add_transformable_label(x_vec, MathTex(r"\vec{x}", color=GREEN), transformation_name='A', animate=False)
        self.wait(1)

        alpha_x = np.array([3,1,0])
        alpha_x_vec = self.add_vector(alpha_x, color=BLUE).set_z_index(1)
        alpha_x_lab = self.add_transformable_label(alpha_x_vec, MathTex(r"\alpha\vec{x}", color=BLUE), at_tip = True, transformation_name='A', animate=False)
        self.wait(1)

        y = np.array([-1,1,0])
        y_vec = self.add_vector(y, color=RED)
        self.add_transformable_label(y_vec, MathTex(r"\vec{y}", color=RED), transformation_name='A', animate=False)
        self.wait(2)
        line_x, line_y = create_sum_lines(self, alpha_x, y, add=True)
        self.add_transformable_mobject(line_x, line_y)
        z = alpha_x+y
        z_vec = self.add_vector(z, color=YELLOW)
        z_lab = self.add_transformable_label(z_vec, MathTex(r"\alpha\vec{x} + \vec{y}", color=YELLOW), transformation_name='A', at_tip=True, animate=False)
        self.wait(2)
        matrix = np.array([[-1,0],[1,-1.5]])
        self.apply_matrix(matrix)
        self.wait(3)
        alpha_x_lab_new = MathTex(r"\alpha A\vec{x}", color=BLUE)
        alpha_x_lab_new.move_to(alpha_x_lab).scale(LARGE_BUFF - 0.2).add_background_rectangle()
        z_lab_new = MathTex(r"\alpha A\vec{x} + A\vec{y}", color=YELLOW)
        z_lab_new.move_to(z_lab).scale(LARGE_BUFF - 0.2).add_background_rectangle()
        self.play(ReplacementTransform(alpha_x_lab, alpha_x_lab_new), ReplacementTransform(z_lab, z_lab_new))
        self.wait(7)

class TransformLine(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        a = np.array((-1,1,0))
        vec_a = self.add_vector(a, color=RED)
        self.add_transformable_label(vec_a, MathTex(r"\vec{a}"), animate=False, transformation_name="A")
        self.wait(5)

        b = np.array((1,1.5,0))
        vec_b = self.add_vector(b, color=BLUE)
        self.add_transformable_label(vec_b, MathTex(r"\vec{b}"), animate=False, transformation_name="A")
        self.wait(2)
        arr_b = Vector(b).shift(a).set_color(BLUE)
        self.play(GrowArrow(arr_b))
        self.wait(3)
        arrows = [Vector(t*b).shift(a).set_color(BLUE) for t in [1.5,2,1.5,0.5,-0.2,-0.8,-1.5]]
        arrow_old = arr_b
        for arrow in arrows:
            self.play(ReplacementTransform(arrow_old, arrow))
            self.wait(1)
            arrow_old = arrow
        self.wait(3)
        line = Line(start=a-5*b, end=a+5*b).set_opacity(0.7).set_z_index(0)
        self.play(Create(line), FadeOut(arrow))
        self.add_transformable_mobject(line)
        self.wait(2)

        line_tex = MathTex(r"p: \vec{a} + t\vec{b},\: t \in \mathbb{R}").add_background_rectangle().shift(3.5*UP+4.5*LEFT)
        self.play(Create(line_tex))
        self.wait(3)
        proof1 = MathTex(r"A(p) = A(\vec{a} + t\vec{b}) = ")
        proof1.add_background_rectangle().shift(2.7*UP).align_to(line_tex, LEFT).set_z_index(1)
        proof2 = MathTex(r"A(\vec{a}) + A(t\vec{b}) = ")
        proof2.add_background_rectangle().shift(proof2.get_right()+proof1.get_right()+0.2*RIGHT).set_z_index(1)
        proof3 = MathTex(r"A(\vec{a}) + tA(\vec{b})")
        proof3.add_background_rectangle().shift(proof3.get_right()+proof2.get_right()+0.2*RIGHT).set_z_index(1)
        proofs=VGroup(line_tex, proof1, proof2, proof3)
        self.play(Create(proof1))
        self.wait(2)
        self.play(Create(proof2))
        self.wait(2)
        self.play(Create(proof3))

        
        
        self.wait(2)

        matrix = np.array([[1,2],[-1,1]])
        self.apply_matrix(matrix)
        self.wait(3)

        transformed_a, transformed_b = [np.array((*np.matmul(matrix,vec[0:2]),0)) for vec in [a,b]]
        arr_b = Vector(transformed_b).shift(transformed_a).set_color(BLUE)
        self.play(GrowArrow(arr_b))
        self.wait(3)
        arrows = [Vector(t*transformed_b).shift(transformed_a).set_color(BLUE) for t in [1.5,1.3,0.5,-0.2,-0.8,-1.5]]
        arrow_old = arr_b
        for arrow in arrows:
            self.play(ReplacementTransform(arrow_old, arrow))
            self.wait(1)
            arrow_old = arrow
        self.wait(5)

        self.play(FadeOut(vec_a, vec_b, arrow, line, proofs))
        self.wait(1)

class NonEquidistant(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        self.wait(2)
        def func(vec):
            return np.array([vec[0], np.sign(vec[1])*(vec[1]**2)/4, 0])
        grid = self.plane
        grid.prepare_for_nonlinear_transform()
        self.play(grid.animate.apply_function(func), run_time=2)
        self.wait(5)

class Linear(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        self.wait(2)
        def func(vec):
            return np.array([2*vec[0] + 1*vec[1], 1*vec[0]+2*vec[1], 0])
        grid = self.plane
        self.play(grid.animate.apply_function(func), run_time=2)
        self.wait(5)

class ToLine(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        self.wait(2)
        def func(vec):
            return np.array([2*vec[0] + 2*vec[1], 1*vec[0]+1*vec[1], 0])
        grid = self.plane
        grid.prepare_for_nonlinear_transform()
        self.play(grid.animate.apply_function(func), run_time=2)
        self.wait(5)

class ToZero(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        self.wait(2)
        grid = self.plane
        grid.prepare_for_nonlinear_transform()
        dot = Dot()
        self.play(ReplacementTransform(grid, dot), run_time=2)
        self.wait(5)

class EquidistantProof(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False,
            foreground_plane_kwargs= {
                "x_range": np.array([-20, 20, 1.0]),
                "y_range": np.array([-20, 20, 1.0]),
                "faded_line_ratio": 1,
            }
        )
    def construct(self):
        line_tex = MathTex(r"p: \vec{a} + t\vec{b},\ t \in \mathbb{R}").add_background_rectangle().shift(3.5*UP+2*RIGHT)
        line_tex.set_z_index(2)
        self.play(Create(line_tex))
        
        a = np.array((-1.5,0.3,0))
        vec_a = self.add_vector(a, color=RED)
        self.add_transformable_label(vec_a, MathTex(r"\vec{a}"), animate=False, transformation_name="A")
        b = np.array((1,1.5,0))
        line = Line(start=a-10*b, end=a+10*b).set_opacity(0.7).set_z_index(0)
        self.play(Create(line))

        line2_tex = MathTex(r"q: \vec{a} + t\vec{b} + \vec{c},\ t \in \mathbb{R}").add_background_rectangle()
        line2_tex.shift(line_tex.get_bottom() + 0.5*DOWN).align_to(line_tex, LEFT).set_z_index(2)
        self.play(Create(line2_tex))

        c = np.array((-1,1,0))
        c_arrows = VGroup(*[Vector(c).shift(a+p*b).set_color(YELLOW) for p in np.arange(-10,10,0.4)])
        self.play(*(GrowArrow(c_arrow) for c_arrow in c_arrows))
        self.wait(5)

        line2 = Line(start=a+c-10*b, end=a+c+10*b).set_opacity(0.7).set_z_index(0)
        self.play(Create(line2))
        self.wait(2)
        self.play(ApplyMethod(c_arrows.set_opacity, 0.5))

        line3_tex = MathTex(r"r: \vec{a} + t\vec{b} + 2\vec{c},\ t \in \mathbb{R}").add_background_rectangle()
        line3_tex.shift(line2_tex.get_bottom() + 0.5*DOWN).align_to(line_tex, LEFT).set_z_index(2)
        self.play(Create(line3_tex))
        texts = VGroup(line_tex, line2_tex, line3_tex)
        
        c2_arrows = VGroup(*[Vector(c).shift(a+c+p*b).set_color(YELLOW) for p in np.arange(-10,10,0.4)])
        self.play(*(GrowArrow(c_arrow) for c_arrow in c2_arrows))
        self.wait(5)
        self.add_transformable_mobject(c_arrows, c2_arrows)

        line3 = Line(start=a+2*c-10*b, end=a+2*c+10*b).set_opacity(0.7).set_z_index(0)
        self.play(Create(line3))
        self.wait(2)
        self.play(ApplyMethod(c2_arrows.set_opacity, 0.5))
        self.add_transformable_mobject(line, line2, line3)

        self.wait(5)

        t1_line_tex = MathTex(r"A(p): A(\vec{a} + t\vec{b}),\ t \in \mathbb{R}").add_background_rectangle().shift(3.5*UP+2*RIGHT)
        t1_line_tex.set_z_index(2)
        t1_line2_tex = MathTex(r"A(q): A(\vec{a} + t\vec{b} + \vec{c}),\ t \in \mathbb{R}").add_background_rectangle()
        t1_line2_tex.shift(t1_line_tex.get_bottom() + 0.5*DOWN).align_to(t1_line_tex, LEFT).set_z_index(2)
        t1_line3_tex = MathTex(r"A(r): A(\vec{a} + t\vec{b} + 2\vec{c}),\ t \in \mathbb{R}").add_background_rectangle()
        t1_line3_tex.shift(t1_line2_tex.get_bottom() + 0.5*DOWN).align_to(t1_line_tex, LEFT).set_z_index(2)
        t1_texts = VGroup(t1_line_tex, t1_line2_tex, t1_line3_tex)
        self.play(ReplacementTransform(texts, t1_texts))
        self.wait(3)
        t2_line_tex = MathTex(r"A(p): A(\vec{a}) + tA(\vec{b}),\ t \in \mathbb{R}").add_background_rectangle().shift(3.5*UP+2*RIGHT)
        t2_line_tex.set_z_index(2)
        t2_line2_tex = MathTex(r"A(q): A(\vec{a}) + tA(\vec{b}) + A(\vec{c}),\ t \in \mathbb{R}").add_background_rectangle()
        t2_line2_tex.shift(t2_line_tex.get_bottom() + 0.5*DOWN).align_to(t2_line_tex, LEFT).set_z_index(2)
        t2_line3_tex = MathTex(r"A(r): A(\vec{a}) + tA(\vec{b}) + 2A(\vec{c}),\ t \in \mathbb{R}").add_background_rectangle()
        t2_line3_tex.shift(t2_line2_tex.get_bottom() + 0.5*DOWN).align_to(t2_line_tex, LEFT).set_z_index(2)
        t2_texts = VGroup(t2_line_tex, t2_line2_tex, t2_line3_tex)
        self.play(ReplacementTransform(t1_texts, t2_texts))
        self.wait(5)
        t3_line_tex = MathTex(r"A(p): A(\vec{a}) + tA(\vec{b}),\: t \in \mathbb{R}").add_background_rectangle().shift(3.5*UP+2*RIGHT)
        t3_line_tex.set_z_index(2)
        t3_line2_tex = MathTex(r"A(q): A(p) + A(\vec{c}),\ t \in \mathbb{R}").add_background_rectangle()
        t3_line2_tex.shift(t3_line_tex.get_bottom() + 0.5*DOWN).align_to(t3_line_tex, LEFT).set_z_index(2)
        t3_line3_tex = MathTex(r"A(r): A(p) + 2A(\vec{c}),\ t \in \mathbb{R}").add_background_rectangle()
        t3_line3_tex.shift(t3_line2_tex.get_bottom() + 0.5*DOWN).align_to(t3_line_tex, LEFT).set_z_index(2)
        t3_texts = VGroup(t3_line_tex, t3_line2_tex, t3_line3_tex)
        self.play(ReplacementTransform(t2_texts, t3_texts))
        self.wait(5)

        matrix=0.7*np.array([[-1,0],[1,-1]])
        self.apply_matrix(matrix)
        self.wait(3)

