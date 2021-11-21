from manim import *
import numpy as np

class LinearIndependence(Scene):
    def construct(self):
        title = Tex(r"Lineární závislost a nezávislost v $\mathbb{R}^2$ nad $\mathbb{R}$")
        self.add(title)
        self.wait(5)

        two_vectors = Tex(r"$\vec{x}, \vec{y}$ jsou LN, pokud $(\forall \alpha, \beta \in \mathbb{R})"
                            +r"(\alpha\vec{x}+\beta\vec{y}=\vec{0} \Rightarrow \alpha=\beta=0)$").scale(0.8)
        two_vectors.shift(0.6*DOWN)
        self.play(ApplyMethod(title.shift, 0.5*UP))
        self.play(Write(two_vectors))
        two_vectors.add_background_rectangle().set_z_index(2)

        self.wait(10)

        self.play(FadeOut(title), ApplyMethod(two_vectors.move_to, (0, 3.5, 0)))
        self.wait(1)

        plane = NumberPlane()
        plane.add_coordinates()
        plane.set_z_index(0)
        self.play(Create(plane))
        self.wait(3)

        def create_vect(array, color, label):
            x = array
            vec = Vector(x, color=color).set_z_index(3)
            vec_label = label
            vec_label.set_z_index(3)
            vec_label.add_background_rectangle()
            shift = [0,0.3,0] if x[1]>=0 else [0,-0.3,0]
            vec_label.move_to(x+0.3*x/np.linalg.norm(x)+shift if np.linalg.norm(x)!=0 else shift)
            return vec, vec_label

        def scale_vec(previous_vec_group, original_vec_array, scalar, label, color=GREEN):
            alpha_x_vec, alpha_x_label = create_vect(scalar*original_vec_array, color, label)
            alpha_x = VGroup(alpha_x_vec, alpha_x_label)           
            self.play(ReplacementTransform(previous_vec_group, alpha_x))
            self.wait(1)
            return alpha_x

        def eng_to_cz_number(number):
            numbers=str(number).split(".")
            return numbers[0]+','+numbers[1] if len(numbers)==2 else numbers[0]

        def vector_and_base(previous_group, x_array, y_array, alpha, beta, line=None):
            z_array = alpha*x_array + beta*y_array
            if alpha == 0 or beta == 0:
                tex = MathTex(r"\vec{z} = 0\vec{x}+"+eng_to_cz_number(beta)+r"\vec{y}") if alpha==0 else MathTex(r"\vec{z} = "+eng_to_cz_number(alpha)+r"\vec{x}+0\vec{y}")
                z_vec, z_label = create_vect(z_array, YELLOW, tex)
                x_vec, x_label = create_vect(alpha*x_array, GREEN, Tex(""))
                y_vec, y_label = create_vect(beta*y_array, RED, Tex(""))
            else:
                x_vec, x_label = create_vect(alpha*x_array, GREEN, MathTex(eng_to_cz_number(alpha)+r"\vec{x}"))
                y_vec, y_label = create_vect(beta*y_array, RED, MathTex(eng_to_cz_number(beta)+r"\vec{y}"))
                z_vec, z_label = create_vect(z_array, YELLOW, MathTex(r"\vec{z}"))
            x_line = Line(start=z_array, end=alpha*x_array, color=WHITE).set_opacity(0.3)
            y_line = Line(start=z_array, end=beta*y_array, color=WHITE).set_opacity(0.3)
            z_group = VGroup(x_vec, x_label, y_vec, y_label, z_vec, z_label, x_line, y_line)
            if line: z_group.add(line)
            self.play(ReplacementTransform(previous_group, z_group))
            return z_group

        x_array = np.array([3,-2,0])
        x_vec, x_label = create_vect(x_array, GREEN, MathTex(r"\vec{x}"))
        x = VGroup(x_vec, x_label)
        y_array = np.array([2,2,0])
        y_vec, y_label = create_vect(y_array, RED, MathTex(r"\vec{y}"))
        y = VGroup(y_vec, y_label)
        alpha = 1.2
        beta=0.8   
        
        z_array = alpha*x_array + beta*y_array
        z_vec, z_label = create_vect(z_array, YELLOW, MathTex(r"\vec{z}"))
        x_line = Line(start=z_array, end=alpha*x_array, color=WHITE).set_opacity(0.3)
        y_line = Line(start=z_array, end=beta*y_array, color=WHITE).set_opacity(0.3)

        self.play(GrowArrow(x_vec), GrowArrow(y_vec), FadeIn(x_label, y_label))
        self.wait(1)
        alpha_x = scale_vec(x, x_array, alpha, MathTex(eng_to_cz_number(alpha)+r"\cdot\vec{x}"))
        beta_y = scale_vec(y, y_array, beta, MathTex(eng_to_cz_number(beta)+r"\cdot\vec{y}"), color=RED)   
        self.play(Create(x_line), Create(y_line))
        self.play(GrowArrow(z_vec), FadeIn(z_label))
        
        group = VGroup(alpha_x[0], alpha_x[1], beta_y[0], beta_y[1], z_vec, z_label, x_line, y_line)

        coefficients = [(0.9, -0.6), (0.7, 0.5), (-0.6, 0.5), (0.7, 1.1), (0.6, 0.6), (-0.6, 0.4)]
        for coef in coefficients:
            self.wait(1)
            group = vector_and_base(group, x_array, y_array, *coef)
        
        self.wait(5)
        #Fix x
        coefficients = [0.8, 0.6, -0.4, 1.2]
        for coef in coefficients:
            group = vector_and_base(group, x_array, y_array, 0.8, coef)
            self.wait(2)
        
        line_fixed_x = Line(start=0.8*x_array + 5*y_array, end=0.8*x_array - 5*y_array).set_opacity(0.5).set_z_index(2)
        group.add(line_fixed_x)
        self.play(FadeIn(line_fixed_x))
        self.wait(6)
        line_fixed_x2 = Line(start=0.6*x_array + 5*y_array, end=0.6*x_array - 5*y_array).set_opacity(0.5).set_z_index(2)
        
        coefficients = [1.2, 0.7, -0.4, 0.8]
        for coef in coefficients:
            group = vector_and_base(group, x_array, y_array, 0.6, coef, line_fixed_x2)
            self.wait(2)
        
        self.wait(1)
        line_fixed_x0 = Line(start=5*y_array, end=- 5*y_array).set_opacity(0.5).set_z_index(2)
        
        coefficients = [1.2, 0.8, 0.4, 0]
        for coef in coefficients:
            group = vector_and_base(group, x_array, y_array, 0, coef, line_fixed_x0)
            self.wait(3)
        
        self.wait(2)

        self.play(FadeOut(group))

        x_array = np.array([3,2,0])
        x_vec, x_label = create_vect(x_array, GREEN, MathTex(r"\vec{x}"))
        x = VGroup(x_vec, x_label)
        y_array = -0.7*np.array([3,2,0])
        y_vec, y_label = create_vect(y_array, RED, MathTex(r"\vec{y}"))
        y = VGroup(y_vec, y_label)
        xy_line = Line(start=5*x_array, end=-5*x_array).set_opacity(0.3)
        self.play(GrowArrow(x_vec), FadeIn(x_label))
        self.wait(1)
        self.play(GrowArrow(y_vec), FadeIn(y_label))
        self.wait(1)
        self.play(FadeIn(xy_line))
        self.wait(5)
        scaled_x = scale_vec(x, x_array, 0.7, MathTex(r"-\vec{y} = 0,7\vec{x}"))
        self.wait(1)
        zeros = VGroup(Vector([0,0]), MathTex(r"\vec{y} - 0,7\vec{x} = \vec{0}").add_background_rectangle(), Vector([0,0]))
        self.play(ReplacementTransform(VGroup(scaled_x[0], scaled_x[1], y_vec), zeros), FadeOut(y_label))
        self.wait(15)