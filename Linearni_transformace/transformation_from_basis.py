from manim import *

class Introduction(Scene):
    def construct(self):
        title = Tex("Zadání lineárního zobrazení").scale(1.5)
        title.add_background_rectangle()
        self.add(title)
        self.wait(9)


class BasisIsEnough(LinearTransformationScene):
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
        rect_w = 6.3
        rect_h=1.5
        rect = Rectangle(color=BLACK, height=rect_h, width=rect_w, fill_opacity=1).shift(rect_w/2*LEFT+0.8*LEFT+(4-(rect_h/2))*UP).set_z_index(1).set_opacity(0.7)
        self.add(rect)
        text = MathTex(r"\textcolor{blue}{A\begin{pmatrix}x\\y\end{pmatrix}}").shift((4-(rect_h/2))*UP).align_to(rect, LEFT).set_z_index(2)
        self.add(text)
        self.wait(1)
        x = 3.47
        y = 1.3
        x_array = np.array((x,y,0))
        vec_x = self.add_vector(x_array).set_z_index(2)
        self.add_transformable_label(vec_x, MathTex(r"\begin{pmatrix}x\\y\end{pmatrix}"), new_label=r"A\begin{pmatrix}x\\y\end{pmatrix}", animate=False, at_tip=True)
        self.wait(2)
        text2 = MathTex(r" = A(x\begin{pmatrix}1\\0\end{pmatrix}+y\begin{pmatrix}0\\1\end{pmatrix})")
        text2.align_to(rect, LEFT).shift((4-(1.5/2))*UP+text.width*RIGHT+0.25*RIGHT).set_z_index(2)
        self.play(Write(text2))
        self.wait(3)    

        e1 = np.array((1,0,0))       
        e2 = np.array((0,1,0))
        
        vec_e1 = self.add_vector(e1, color=GREEN).set_z_index(2)
        vec_e1_label = self.label_vector(vec_e1, MathTex(r"\begin{pmatrix}1\\0\end{pmatrix}"), animate=False, at_tip = True)
        vec_e2 = self.add_vector(e2, color=RED).set_z_index(2)
        vec_e2_label = self.label_vector(vec_e2, MathTex(r"\begin{pmatrix}0\\1\end{pmatrix}"), animate=False, at_tip = True)
        vecs_group = VGroup(vec_e1, vec_e1_label, vec_e2, vec_e2_label)

        

        line_e1 = Line(x_array, x*e1).set_opacity(0.5)
        line_e2 = Line(x_array, y*e2).set_opacity(0.5)
        self.add_transformable_mobject(line_e1, line_e2)
        self.play(Create(line_e1), Create(line_e2))


        vec_alpha_e1 = Vector(x*e1, color=GREEN).set_z_index(2)
        vec_alpha_e1_label = self.get_vector_label(vec_alpha_e1, MathTex(r"x\begin{pmatrix}1\\0\end{pmatrix}"), 
                                                    color=GREEN,
                                                    at_tip = True)
        self.moving_vectors.append(vec_alpha_e1)
        vec_alpha_e1_label.target_text = r"x A\begin{pmatrix}1\\0\end{pmatrix}"
        vec_alpha_e1_label.vector = vec_alpha_e1
        vec_alpha_e1_label.kwargs = {}
        self.transformable_labels.append(vec_alpha_e1_label)
        vec_beta_e2 = Vector(y*e2, color=RED).set_z_index(2)
        self.moving_vectors.append(vec_beta_e2)
        vec_beta_e2_label = self.get_vector_label(vec_beta_e2, MathTex(r"y\begin{pmatrix}0\\1\end{pmatrix}"))
        vec_beta_e2_label.target_text = r"y A\begin{pmatrix}0\\1\end{pmatrix}"
        vec_beta_e2_label.vector = vec_beta_e2
        vec_beta_e2_label.kwargs = {"at_tip": True}
        self.transformable_labels.append(vec_beta_e2_label)
        vecs_group2 = VGroup(vec_alpha_e1, vec_alpha_e1_label, vec_beta_e2, vec_beta_e2_label)
        self.play(ReplacementTransform(vecs_group, vecs_group2))

        self.wait(5)

        text3 = MathTex(r" = xA\begin{pmatrix}1\\0\end{pmatrix}+yA\begin{pmatrix}0\\1\end{pmatrix}")
        text3.align_to(rect, LEFT).shift((4-(1.5/2))*UP+text.width*RIGHT+0.25*RIGHT).set_z_index(2)
        text_gr = VGroup(text3, text)
        self.play(ReplacementTransform(text2, text3))
        self.wait(5)

        matrix = 0.3*np.array([[1.5,-3],[-2,-1]])
        self.apply_matrix(matrix)
        self.wait(5)

        self.play(*[FadeOut(mob)for mob in self.mobjects if mob!=text3 and mob!=text], ApplyMethod(text_gr.move_to, ORIGIN+2*UP))
        self.wait(2)
        Ae1 = MathTex(r"A\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}a_{11}\\a_{12}\end{pmatrix}").shift(0.5*UP+2*LEFT).set_color(GREEN)
        Ae2 = MathTex(r"A\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}a_{21}\\a_{22}\end{pmatrix}").shift(0.5*UP+2*RIGHT).set_color(RED)
        self.play(Write(Ae1))
        self.wait(1)
        self.play(Write(Ae2))
        self.wait(2)

        matrix_tex = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN), MathTex(r"a_{12}").set_color(RED)], [MathTex(r"a_{21}").set_color(GREEN), MathTex(r"a_{22}").set_color(RED)]],
            left_bracket="(",
            right_bracket=")").shift(1.5*DOWN)
        self.play(Write(matrix_tex))
        self.wait(7)


class AnotherBasis(LinearTransformationScene):
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
        rect_w = 7
        rect_h=1.5
        rect = Rectangle(color=BLACK, height=rect_h, width=rect_w, fill_opacity=1).shift(rect_w/2*LEFT+(4-(rect_h/2))*UP).set_z_index(1)
        self.add(rect)
        text = MathTex(r"A(\vec{x})").shift((4-(rect_h/2))*UP).align_to(rect, LEFT).set_z_index(2)
        self.add(text)
        self.wait(1)
        x1 = np.array((2,-1,0))       
        x2 = np.array((1,1,0))
        alpha = 1.2
        beta = 1.8
        x_array = alpha*x1 + beta*x2
        vec_x = self.add_vector(x_array).set_z_index(2)
        self.add_transformable_label(vec_x, MathTex(r"\vec{x}"), transformation_name="A", animate=False, at_tip=True)
        self.wait(2)
          

        vec_x1 = self.add_vector(x1, color=GREEN).set_z_index(2)
        vec_x1_label = self.label_vector(vec_x1, MathTex(r"\vec{x}_1"), animate=False)
        vec_x2 = self.add_vector(x2, color=RED).set_z_index(2)
        vec_x2_label = self.label_vector(vec_x2, MathTex(r"\vec{x}_2"), animate=False)
        vecs_group = VGroup(vec_x1, vec_x1_label, vec_x2, vec_x2_label)
        
        text2 = MathTex(r" = A(\alpha\vec{x}_1+\beta\vec{x}_2)")
        text2.align_to(rect, LEFT).shift((4-(1.5/2))*UP+text.width*RIGHT+0.25*RIGHT).set_z_index(2)
        self.play(Write(text2))
        self.wait(1)  

        x1 = np.array((2,-1,0))       
        x2 = np.array((1,1,0))
        line_xx1 = Line(x_array, beta*x2).set_opacity(0.5)
        line_xx2 = Line(x_array, alpha*x1).set_opacity(0.5)
        line_x1 = Line(-10*x1, 10*x1).set_opacity(0.5)
        line_x2 = Line(-10*x2, 10*x2).set_opacity(0.5)
        self.add_transformable_mobject(line_xx1, line_xx2, line_x1, line_x2)
        self.play(Create(line_xx1), Create(line_xx2), Create(line_x1), Create(line_x2))

        self.wait(1)

        vec_alpha_x1 = Vector(alpha*x1, color=GREEN).set_z_index(2)
        vec_alpha_x1_label = self.get_vector_label(vec_alpha_x1, MathTex(r"\alpha\vec{x}_1"), color=GREEN)
        self.moving_vectors.append(vec_alpha_x1)
        vec_alpha_x1_label.target_text = r"\alpha A(\vec{x}_1)"
        vec_alpha_x1_label.vector = vec_alpha_x1
        vec_alpha_x1_label.kwargs = {}
        self.transformable_labels.append(vec_alpha_x1_label)
        vec_beta_x2 = Vector(beta*x2, color=RED).set_z_index(2)
        self.moving_vectors.append(vec_beta_x2)
        vec_beta_x2_label = self.get_vector_label(vec_beta_x2, MathTex(r"\beta\vec{x}_2"))
        vec_beta_x2_label.target_text = r"\beta A(\vec{x}_2)"
        vec_beta_x2_label.vector = vec_beta_x2
        vec_beta_x2_label.kwargs = {}
        self.transformable_labels.append(vec_beta_x2_label)
        vecs_group2 = VGroup(vec_alpha_x1, vec_alpha_x1_label, vec_beta_x2, vec_beta_x2_label)
        self.play(ReplacementTransform(vecs_group, vecs_group2))
        self.wait(2)


        text3 = MathTex(r" = \alpha A(\vec{x}_1) + \beta A(\vec{x}_2)")
        text3.align_to(rect, LEFT).shift((4-(1.5/2))*UP+text.width*RIGHT+0.25*RIGHT).set_z_index(2)
        
        matrix = 0.6*np.array([[2,1],[0.7,-2]])
        self.apply_matrix(matrix, added_anims=[ReplacementTransform(text2, text3)])


        self.wait(9)