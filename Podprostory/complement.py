from manim import *
from imports.vectors_creation import create_vect, create_sum_lines, change_linear_combination

class Complement(VectorScene):
    def construct(self):
        title = Tex(r"Doplněk podprostoru v $\mathbb{R}^2$ nad $\mathbb{R}$").scale(1.2)
        self.add(title)
        self.wait(5)

        first = MathTex(r"P,Q \subset\subset \mathbb{R}^2").shift(0.6*UP)
        second = Tex(r"$Q$ je doplňkem $P\ \iff \ P \oplus Q = \mathbb{R}^2$").shift(0.4*DOWN)
        
        self.play(ApplyMethod(title.shift, 1.6*UP))
        self.play(Write(first))
        self.wait(4)
        self.play(Write(second))
        self.wait(5)

        self.play(FadeOut(title, first, second))
        self.wait(1)

        plane = NumberPlane(x_range=[-20, 20, 1],
                            y_range=[-20, 20, 1])
        plane.add_coordinates()
        plane.set_z_index(0)
        self.play(Create(plane))
        self.wait(1)
        u = 1/2*np.array([2,3,0])
        v = 1/2*np.array([-3,1,0])
        P_line = Line(-10*u, 10*u)
        P_tag = MathTex('P').shift(2*u + 0.3*RIGHT)
        P = VGroup(P_line, P_tag)
        Q_line = Line(-10*v, 10*v)
        Q_tag = MathTex('Q').shift(4*v + 0.3*RIGHT + 0.3*UP)
        Q = VGroup(Q_line, Q_tag)
        self.play(Create(P), Create(Q))
        self.wait(3)

        u_vec, u_label = create_vect(self, u, GREEN, MathTex(r"\vec{u}"), add=True)
        v_vec, v_label = create_vect(self, v, BLUE, MathTex(r"\vec{v}"), add=True)

        z = u + v
        line_u, line_v = create_sum_lines(self, u, v, add=True)
        z_vec, z_label = create_vect(self, u+v, YELLOW, MathTex(r"\vec{z}"), add=True)
        group = VGroup(u_vec, u_label, v_vec, v_label, z_vec, z_label, line_u, line_v)
        self.wait(2)

        u_scalars = [1.2, 1.5, -0.2, 2, -1.4, 0.2, 1]
        v_scalars = [0.9, 0.4, -2, -1.7, 1.2, 1.2, 1]
        def dif_scalars(u, v, group, u_scalars, v_scalars):
            old_group = group
            for u_scalar, v_scalar in zip(u_scalars, v_scalars):
                new_group = change_linear_combination(self, u, v, MathTex(r"\vec{u}"), MathTex(r"\vec{v}"), MathTex(r"\vec{z}"), GREEN, BLUE, YELLOW, u_scalar, v_scalar)
                self.play(ReplacementTransform(old_group, new_group))
                self.wait(1)
                old_group = new_group
            return new_group
        group = dif_scalars(u, v, group, u_scalars, v_scalars)
        
        self.wait(3)
        new_vs = [[-3,-1,0], [2,1,0], [-1,1.5,0], -1.2*u]
        for nev_v_arr in new_vs:
            new_v = 1.5*np.array(nev_v_arr)/np.linalg.norm(nev_v_arr)
            new_Q_line = Line(-10*new_v, 10*new_v)
            new_Q_tag = MathTex('Q').shift(4*new_v/np.linalg.norm(new_v) + 0.3*RIGHT + 0.3*UP)
            new_Q = VGroup(new_Q_line, new_Q_tag)
            new_group = change_linear_combination(self, u, new_v, MathTex(r"\vec{u}"), MathTex(r"\vec{v}"), MathTex(r"\vec{z}"), GREEN, BLUE, YELLOW, 1, 1)
            self.play(ReplacementTransform(group, new_group), ReplacementTransform(Q, new_Q))
            group = new_group
            Q = new_Q
            u_scalars = [1.2, 0.5, 1]
            v_scalars = [0.9, -2, 1]
            group = dif_scalars(u, new_v, group, u_scalars, v_scalars)
            self.wait(2)
        self.wait(6)