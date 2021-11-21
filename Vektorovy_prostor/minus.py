from manim import *
class Minus(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        self.wait(5)
        theorem = MathTex(r"(\forall \alpha \in T)(\forall \vec{a} \in V)(-(\alpha\vec{a}) = (-\alpha)\vec{a} = \alpha(-\vec{a}))")
        theorem.to_corner(UL)
        theorem.add_background_rectangle()
        self.play(FadeIn(theorem))
        self.wait(16)

        # Gets arrow or vector and np.array of that vector with zero in 3rd dimension
        def label_position(vec, a):
            return vec.get_end()+0.35*a/np.linalg.norm(a)

        a = np.array([3,2,0])
        alpha = 1.3
        vec_a = self.add_vector(a, color = BLUE)
        label_a = Tex(r"{\small $\vec{a}$}")
        label_a.add_background_rectangle()
        label_a.shift(label_position(vec_a, a))
        self.play(FadeIn(label_a))
        a_group = VGroup(vec_a, label_a)
        
        self.wait(2)
        
        scaled_a = alpha*a
        vec_scaled_a = Vector(scaled_a, color=BLUE)
        label_scaled_a = Tex(r"{\small $\alpha\vec{a}$}")
        label_scaled_a.add_background_rectangle()
        label_scaled_a.shift(label_position(vec_scaled_a, scaled_a))
        scaled_a_group = VGroup(vec_scaled_a, label_scaled_a)
        self.play(ReplacementTransform(a_group, scaled_a_group))
        
        self.wait(3)

        minus_sc_a = -scaled_a
        vec_minus_sc_a = Vector(minus_sc_a, color=GREEN)
        label_minus_sc_a = Tex(r"{\small $-(\alpha\vec{a})$}")
        label_minus_sc_a.add_background_rectangle()
        label_minus_sc_a.shift(label_position(vec_minus_sc_a, minus_sc_a))
        minus_sc_a_group = VGroup(vec_minus_sc_a, label_minus_sc_a)
        self.play(ReplacementTransform(scaled_a_group, minus_sc_a_group))
        self.wait(2)
        self.play(ApplyMethod(vec_minus_sc_a.set_opacity, 0.5), FadeOut(label_minus_sc_a))


        a = np.array([3,2,0])
        alpha = 1.3
        vec_a = self.add_vector(a, color = BLUE)
        label_a = Tex(r"{\small $\vec{a}$}")
        label_a.add_background_rectangle()
        label_a.shift(label_position(vec_a, a))
        self.play(FadeIn(label_a))
        a_group = VGroup(vec_a, label_a)

        self.wait(3)

        scaled_a = -alpha*a
        vec_scaled_a = Vector(scaled_a, color=GREEN)
        label_scaled_a = Tex(r"{\small $-(\alpha\vec{a}) = (-\alpha)\vec{a}$}")
        label_scaled_a.add_background_rectangle()
        label_scaled_a.shift(label_position(vec_scaled_a, scaled_a))
        scaled_a_group = VGroup(vec_scaled_a, label_scaled_a)
        self.play(ReplacementTransform(a_group, scaled_a_group))
        self.wait(2)
        self.play(FadeOut(vec_scaled_a), FadeOut(label_scaled_a))

        self.wait(1)

        a = np.array([3,2,0])
        alpha = 1.3
        vec_a = self.add_vector(a, color = BLUE)
        label_a = Tex(r"{\small $\vec{a}$}")
        label_a.add_background_rectangle()
        label_a.shift(label_position(vec_a, a))
        self.play(FadeIn(label_a))
        a_group = VGroup(vec_a, label_a)

        self.wait(1)

        minus_a = -a
        vec_minus_a = Vector(minus_a, color=BLUE)
        label_minus_a = Tex(r"{\small $-\vec{a}$")
        label_minus_a.add_background_rectangle()
        label_minus_a.shift(label_position(vec_minus_a, minus_a))
        minus_a_group = VGroup(vec_minus_a, label_minus_a)
        self.play(ReplacementTransform(a_group, minus_a_group))

        self.wait(1)

        minus_sc_a = alpha*minus_a
        vec_minus_sc_a = Vector(minus_sc_a, color=GREEN)
        label_minus_sc_a = Tex(r"{\small $-(\alpha\vec{a}) = (-\alpha)\vec{a} = \alpha(-\vec{a})$}")
        label_minus_sc_a.add_background_rectangle()
        label_minus_sc_a.shift(label_position(vec_minus_sc_a, minus_sc_a))
        minus_sc_a_group = VGroup(vec_minus_sc_a, label_minus_sc_a)
        self.play(ReplacementTransform(minus_a_group, minus_sc_a_group))
        self.wait(5)