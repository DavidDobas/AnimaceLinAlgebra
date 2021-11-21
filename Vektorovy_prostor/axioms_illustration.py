from manim import *
class OpeningText(Scene):
    def construct(self):
        title = Tex(r"Ilustrace axiomů v $\mathbb{R}^2$")
        self.add(title)
        self.wait(5)

class FirstAxiom(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self): 
        title = Tex(r"{\large 1. axiom}")
        axiom = MathTex(r"(\forall \vec{a}, \vec{b} \in V)(\vec{a} \oplus \vec{b} = \vec{b} \oplus \vec{a})")
        title.to_corner(UL)
        axiom.to_corner(UL)
        axiom.shift(0.5*DOWN)
        self.add(title, axiom)
        self.wait(10)
        
        a = np.array([1,2])
        vec_a = self.add_vector(a, color = BLUE)
        label_a = Tex(r"{\small $\vec{a}$}")
        label_a.add_background_rectangle()
        label_a.shift(0.2*RIGHT+1.1*UP)
        self.play(FadeIn(label_a), run_time=0.3)
        labeled_a = VGroup(vec_a, label_a)

        b = np.array([2, -3])
        vec_b = self.add_vector(b, color = RED)       
        label_b = Tex(r"{\small $\vec{b}$}")
        label_b.shift(1.4*RIGHT+1.5*DOWN)
        label_b.add_background_rectangle()
        self.play(FadeIn(label_b), run_time=0.3)
        labeled_b = VGroup(vec_b, label_b)

        self.wait(1)

        self.play(ApplyMethod(labeled_b.shift, vec_a.get_end()))

        c = a + b
        vec_c = self.add_vector(c, color = GREEN)
        label_c = Tex(r"{\small $\vec{a} + \vec{b}$}")
        label_c.shift(1*RIGHT+0.8*DOWN)
        label_c.add_background_rectangle()
        self.play(FadeIn(label_c), run_time=0.3)

        self.wait(2)

        self.play(FadeOut(label_c), run_time=0.3)
        self.play(ApplyMethod(vec_c.set_opacity, 0.5))

        self.play(ApplyMethod(labeled_b.shift, -vec_a.get_end()))
        self.play(ApplyMethod(labeled_a.shift, vec_b.get_end()))
        self.play(ApplyMethod(vec_c.set_opacity, 1))
        label_c = Tex(r"{\small $\vec{b} + \vec{a}$}")
        label_c.shift(1.7*RIGHT)
        label_c.add_background_rectangle()
        self.play(FadeIn(label_c), run_time=0.3)

        self.wait(4)

class SecondAxiom(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self): 

        title = Tex(r"{\large 2. axiom}")
        axiom = MathTex(r"(\forall \vec{a}, \vec{b}, \vec{c} \in V)(\vec{a} \oplus (\vec{b} \oplus \vec{c})= (\vec{a} \oplus \vec{b}) \oplus \vec{c})")
        title.to_corner(UL)
        axiom.to_corner(UL)
        axiom.shift(0.5*DOWN)
        title.add_background_rectangle()
        axiom.add_background_rectangle()
        self.add(title, axiom)
        self.wait(12)
        
        a = np.array([2,1])
        vec_a = self.add_vector(a, color = BLUE)
        label_a = Tex(r"{\small $\vec{a}$}")
        label_a.add_background_rectangle()
        label_a.shift(1*RIGHT+0.9*UP)
        self.play(FadeIn(label_a), run_time=0.3)

        b = np.array([-4, 1])
        vec_b = self.add_vector(b, color = RED)       
        label_b = Tex(r"{\small $\vec{b}$}")
        label_b.shift(2*LEFT+0.9*UP)
        label_b.add_background_rectangle()
        self.play(FadeIn(label_b), run_time=0.3)
        labeled_b = VGroup(vec_b, label_b)

        c = np.array([5, -4])
        vec_c = self.add_vector(c, color = YELLOW)       
        label_c = Tex(r"{\small $\vec{c}$}")
        label_c.shift(1.7*RIGHT+1.7*DOWN)
        label_c.add_background_rectangle()
        self.play(FadeIn(label_c), run_time=0.3)
        labeled_c = VGroup(vec_c, label_c)
        
        self.wait(2)

        self.play(ApplyMethod(labeled_c.shift, vec_b.get_end()))
        
        d = b + c
        vec_d = self.add_vector(d, color = PINK)       
        label_d = Tex(r"{\small $\vec{b} + \vec{c}$}")
        label_d.shift(1*RIGHT+0.8*DOWN)
        label_d.add_background_rectangle()
        self.play(FadeIn(label_d), run_time=0.3)
        labeled_d = VGroup(vec_d, label_d)

        self.play(ApplyMethod(labeled_b.set_opacity, 0.3), ApplyMethod(labeled_c.set_opacity, 0.3))

        self.play(ApplyMethod(labeled_d.shift, vec_a.get_end()))

        e = a + d
        vec_e = self.add_vector(e, color = GREEN)       
        label_e = Tex(r"{\small $\vec{a} + (\vec{b} + \vec{c})$}")
        label_e.shift(1*DOWN)
        label_e.add_background_rectangle()
        self.play(FadeIn(label_e), run_time=0.3)
        labeled_e = VGroup(vec_e, label_e)

        self.wait(2)

        self.play(ApplyMethod(labeled_e.set_opacity, 0.3))
        self.play(FadeOut(labeled_d))
        self.play(ApplyMethod(labeled_b.set_opacity, 1), ApplyMethod(labeled_c.set_opacity, 1))
        
        self.play(ApplyMethod(labeled_b.shift, vec_a.get_end()))
        self.play(ApplyMethod(labeled_c.shift, -vec_c.get_start() + vec_b.get_end()))

        self.play(ApplyMethod(labeled_e.set_opacity, 1))
        label_e_new = Tex(r"{\small $(\vec{a} + \vec{b}) + \vec{c}$}")
        label_e_new.shift(1*DOWN)
        label_e_new.add_background_rectangle()
        self.play(ReplacementTransform(label_e, label_e_new))
        self.wait(5)


class EighthAxiom(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False,
        )
    def construct(self): 
        self.transformable_mobjects=[]
        title = Tex(r"{\large 8. axiom}")
        title.add_background_rectangle()
        axiom = MathTex(r"(\forall \alpha \in T)(\forall \vec{a}, \vec{b} \in V)(\alpha \odot (\vec{a} \oplus \vec{b}) = (\alpha \odot \vec{a}) \oplus (\alpha \odot \vec{b}))")
        axiom.add_background_rectangle()
        title.to_corner(UL)
        axiom.to_corner(UL)
        axiom.shift(0.5*DOWN)
        self.add(title, axiom)

        self.wait(15)
        
        a = np.array([2,1,0])
        vec_a = self.add_vector(a, color = BLUE)
        #self.add_transformable_label(vec_a, MathTex(r"\vec{a}"), animate=False, new_label=MathTex(r"\alpha \cdot \vec{a}"))

        b = np.array([4, -2,0])
        vec_b = self.add_vector(b, color = RED)       
        #self.add_transformable_label(vec_b, MathTex(r"\vec{b}"), animate=False, new_label=MathTex(r"\alpha \cdot \vec{b}"))

        line_a = Line(a, a+b)
        line_b = Line(b, a+b)
        self.play(FadeIn(line_a), FadeIn(line_b))
        self.add_transformable_mobject(line_a, line_b)
        c = a + b
        vec_c = self.add_vector(c, color = GREEN)
        #self.add_transformable_label(vec_c, MathTex(r"\vec{a} + \vec{b}"), animate=False, new_label=MathTex(r"\alpha \cdot (\vec{a} + \vec{b})"))
        self.wait(5)

        matrix = [[1.2, 0], 
                 [0, 1.2]]
        self.apply_matrix(matrix)

        self.wait(3)

        #self.add_transformable_label(vec_a, MathTex(r"\alpha \cdot \vec{a}"), animate=False, new_label=MathTex(r"\beta \cdot \vec{a}"))
        #self.add_transformable_label(vec_a, MathTex(r"\alpha \cdot \vec{b}"), animate=False, new_label=MathTex(r"\beta \cdot \vec{b}"))
        #self.add_transformable_label(vec_c, MathTex(r"\alpha \cdot (\vec{a} + \vec{b})"), animate=False, new_label=MathTex(r"\beta \cdot (\vec{a} + \vec{b})"))
        
        matrix = [[-0.8, 0], 
                 [0, -0.8]]
        self.apply_matrix(matrix)
        self.wait(3)

        matrix = [[-0.7, 0], 
                 [0, -0.7]]
        self.apply_matrix(matrix)
        self.wait(5)