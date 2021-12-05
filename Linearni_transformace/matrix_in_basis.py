from manim import *

class Introduction(Scene):
    def construct(self):
        title = Tex("Matice lineárního zobrazení v bázích").scale(1.5)
        self.add(title)
        self.wait(6)

class Motivation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
                self,
                show_coordinates=True,
                show_basis_vectors=False,
                foreground_plane_kwargs= {
                "x_range": np.array([-20, 20, 1]),
                "y_range": np.array([-20, 20, 1]),
                },
                background_plane_kwargs= {
                "x_range": np.array([-20, 20, 1]),
                "y_range": np.array([-20, 20, 1]),
                }
            )
    def construct(self):
        self.wait(9)
        x1_arr = np.array([1,3])
        x1 = self.add_vector(x1_arr, color=GREEN)
        self.add_transformable_label(x1, r"\vec{x}_1", transformation_name="A", animate=False)
        x2_arr = np.array([-3,2])
        x2 = self.add_vector(x2_arr, color=RED)
        self.add_transformable_label(x2, r"\vec{x}_2", transformation_name="A", animate=False)
        self.wait(3)
        Ax1 = MathTex(r"A\vec{x}_1=\begin{pmatrix}5\\-1\end{pmatrix}").move_to([4,3,0])
        Ax2 = MathTex(r"A\vec{x}_2=\begin{pmatrix}-2\\-3\end{pmatrix}").next_to(Ax1, DOWN)
        self.play(Write(Ax1))
        self.wait(2)
        self.play(Write(Ax2))
        self.wait(2)
        basis_matrix = np.transpose(np.array([x1_arr, x2_arr]))
        basis_matrix_inverse = np.linalg.inv(basis_matrix)
        A_in_basis = np.array([[5, -2], [-1, -3]])
        A_matrix = np.matmul(A_in_basis, basis_matrix_inverse)
        self.apply_matrix(A_matrix)
        self.wait(4)

class FromBasisToStandardBasis(Scene):
    def construct(self):
        basis = MathTex(r'\mathcal{X} = (', r'\vec{x}_1', ',',  r'\vec{x}_2', ')').move_to([-4,3,0])
        basis[1].set_color(GREEN)
        basis[3].set_color(RED)
        Ax1 = MathTex(r"A", r"\vec{x}_1", "=").align_to(basis, LEFT).shift(1.6*UP)
        Ax1[1].set_color(GREEN)
        Ax1_v = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN)], [MathTex(r"a_{21}").set_color(GREEN)]], left_bracket="(", right_bracket=")")
        Ax1_v.next_to(Ax1)
        Ax2 = MathTex(r"A", r"\vec{x}_2", "=").next_to(Ax1_v, RIGHT).shift(0.3*RIGHT)
        Ax2[1].set_color(RED)
        Ax2_v = MobjectMatrix([[MathTex(r"a_{12}").set_color(RED)], [MathTex(r"a_{22}").set_color(RED)]], left_bracket="(", right_bracket=")")
        Ax2_v.next_to(Ax2)
        self.add(basis, Ax1, Ax2, Ax1_v, Ax2_v)
        self.wait(6)

        basis_matrix = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN),MathTex(r"a_{12}").set_color(RED)], 
                                    [MathTex(r"a_{21}").set_color(GREEN), MathTex(r"a_{22}").set_color(RED)]], 
                                    left_bracket="(", 
                                    right_bracket=")").shift(2.5*LEFT + 0.4*DOWN)
        self.play(Write(basis_matrix))
        self.wait(3)
        vec10 = Matrix([[1], [0]], left_bracket="(", right_bracket=")").next_to(basis_matrix, RIGHT)
        equals = MathTex("=").next_to(vec10, RIGHT)
        self.play(Write(vec10))
        self.play(Write(equals))
        self.wait(3)
        result = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN)], [MathTex(r"a_{21}").set_color(GREEN)]], left_bracket="(", right_bracket=")").next_to(equals, RIGHT)
        self.play(Write(result))
        self.wait(11)

        rect_10 = Rectangle(color=GREEN, height = 1.8, width = 0.6).move_to(vec10.get_center())
        rect_result = Rectangle(color=YELLOW, height = 1.8, width = 0.8).move_to(result.get_center())
        x1_X = MathTex(r"(", r"\vec{x}_1", r")_{\mathcal{X}}").next_to(rect_10, DOWN).shift(0.8*DOWN)
        x1_X[1].set_color(GREEN)
        Ax1_E = MathTex(r"(A", r"\vec{x}_1", r")_{\mathcal{E}}").next_to(rect_result, DOWN).shift(0.8*DOWN)
        Ax1_E[1].set_color(GREEN)
        line_10 = DashedLine(start=rect_10.get_bottom()+0.1*DOWN, end=x1_X.get_top()+0.1*UP, dash_length=0.05, dashed_ratio=0.5)
        line_Ax1_E = DashedLine(start=rect_result.get_bottom()+0.1*DOWN, end=Ax1_E.get_top()+0.1*UP, dash_length=0.05, dashed_ratio=0.5)
        self.play(Create(rect_10), Create(line_10), Create(x1_X))
        self.wait(4)
        self.play(Create(rect_result), Create(line_Ax1_E), Create(Ax1_E))
        self.wait(5)
        result2 = MobjectMatrix([[MathTex(r"a_{12}").set_color(RED)], [MathTex(r"a_{22}").set_color(RED)]], left_bracket="(", right_bracket=")").next_to(equals, RIGHT)
        rect_01 = Rectangle(color=RED, height = 1.8, width = 0.6).move_to(vec10.get_center())
        x2_X = MathTex(r"(", r"\vec{x}_2", r")_{\mathcal{X}}").next_to(rect_01, DOWN).shift(0.8*DOWN)
        x2_X[1].set_color(RED)
        Ax2_E = MathTex(r"(A", r"\vec{x}_2", r")_{\mathcal{E}}").next_to(rect_result, DOWN).shift(0.8*DOWN)
        Ax2_E[1].set_color(RED)
        self.play(ReplacementTransform(result, result2), 
                    ReplacementTransform(rect_10, rect_01),
                    ReplacementTransform(x1_X, x2_X),
                    ReplacementTransform(Ax1_E, Ax2_E),
                    ApplyMethod(vec10[0][0].move_to, vec10[0][1].get_center()),
                    ApplyMethod(vec10[0][1].move_to, vec10[0][0].get_center()))
        self.wait(6)
        vec_x_X = MathTex(r"(\vec{x})_{\mathcal{X}}").scale(1.2).next_to(basis_matrix, RIGHT)
        
        self.play(FadeOut(rect_result, rect_01, line_10, line_Ax1_E, x2_X, Ax2_E))
        self.wait(2)
        self.play(ReplacementTransform(vec10, vec_x_X), ApplyMethod(equals.next_to, vec_x_X), FadeOut(result2))
        self.wait(2)

        coords_vec = MobjectMatrix([[MathTex(r"x^{\#}_1(\vec{x})")], [MathTex(r"x^{\#}_2(\vec{x})")]], left_bracket="(", right_bracket=")").next_to(basis_matrix, RIGHT)
        self.play(ReplacementTransform(vec_x_X, coords_vec), ApplyMethod(equals.next_to, coords_vec))
        self.wait(2)
        first = MathTex(r"a_{11}", r"\cdot", r"x^{\#}_1(\vec{x})", r"+", r"a_{12}", r"\cdot", r"x^{\#}_2(\vec{x})")
        first[0].set_color(GREEN)
        first[4].set_color(RED)
        first.set_opacity(0)
        second = MathTex(r"a_{21}", r"\cdot", r"x^{\#}_1(\vec{x})", r"+", r"a_{22}", r"\cdot", r"x^{\#}_2(\vec{x})")
        second[0].set_color(GREEN)
        second[4].set_color(RED)
        second.set_opacity(0)
        result3 = MobjectMatrix([[first], [second]], left_bracket="(", right_bracket=")").next_to(equals, RIGHT)
        result3.get_brackets().set_opacity(0)
        self.play(ApplyMethod(VGroup(basis_matrix, coords_vec, equals, result3).move_to, [-0.5,-0.5,0]))
        self.play(ApplyMethod(result3.get_brackets().set_opacity, 1))
        self.wait(1)
        self.play(ApplyMethod(first.set_opacity, 1))
        self.wait(5)
        self.play(ApplyMethod(second.set_opacity, 1))
        self.wait(4)



        vec1 = MobjectMatrix([[VGroup(first[0].copy(), first[1].copy(), first[2].copy())],[VGroup(second[0].copy(), second[1].copy(), second[2].copy())]],
                    left_bracket="(",
                    right_bracket=")").next_to(equals)
        plus = MathTex("+").next_to(vec1)
        vec2 = MobjectMatrix([[VGroup(first[4].copy(), first[5].copy(), first[6].copy())],[VGroup(second[4].copy(), second[5].copy(), second[6].copy())]],
                    left_bracket="(",
                    right_bracket=")").next_to(plus)

        self.play(ReplacementTransform(result3.get_brackets()[0], vec1.get_brackets()[0]),
                    ReplacementTransform(VGroup(first[0], first[1], first[2]), vec1.get_entries()[0]),
                    ReplacementTransform(VGroup(second[0], second[1], second[2]), vec1.get_entries()[1]),
                    ReplacementTransform(first[3], plus),
                    ReplacementTransform(second[3], vec1.get_brackets()[1]),
                    FadeIn(vec2.get_brackets()[0]),
                    ReplacementTransform(VGroup(first[4], first[5], first[6]), vec2.get_entries()[0]),
                    ReplacementTransform(VGroup(second[4], second[5], second[6]), vec2.get_entries()[1]),
                    ReplacementTransform(result3.get_brackets()[1], vec2.get_brackets()[1]))
        self.wait(3)


        x1 = MathTex(r"x^{\#}_1(\vec{x})").next_to(equals)   
        Ax1_vec = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN)], [MathTex(r"a_{21}").set_color(GREEN)]],
                    left_bracket="(",
                    right_bracket=")")
        Ax1_vec.next_to(x1)
        plus2 = MathTex("+").next_to(Ax1_vec)
        x2 = MathTex(r"x^{\#}_2(\vec{x})").next_to(plus2)
        Ax2_vec = MobjectMatrix([[MathTex(r"a_{21}").set_color(RED)], [MathTex(r"a_{22}").set_color(RED)]],
                    left_bracket="(",
                    right_bracket=")")
        Ax2_vec.next_to(x2)
        result3 = VGroup(VGroup(x1, Ax1_vec), plus2, VGroup(x2, Ax2_vec))
        self.play(ReplacementTransform(vec1.get_brackets()[0], Ax1_vec.get_brackets()[0]),
                    ReplacementTransform(vec1.get_entries()[0][0], Ax1_vec.get_entries()[0]),
                    ReplacementTransform(vec1.get_entries()[1][0], Ax1_vec.get_entries()[1]),
                    FadeOut(vec1.get_entries()[0][1], vec1.get_entries()[1][1], vec1.get_entries()[1][2]),
                    ReplacementTransform(vec1.get_entries()[0][2], x1),
                    ReplacementTransform(plus, plus2),
                    ReplacementTransform(vec1.get_brackets()[1], Ax1_vec.get_brackets()[1]),
                    ReplacementTransform(vec2.get_brackets()[0], Ax2_vec.get_brackets()[0]),
                    ReplacementTransform(vec2.get_entries()[0][0], Ax2_vec.get_entries()[0]),
                    ReplacementTransform(vec2.get_entries()[1][0], Ax2_vec.get_entries()[1]),
                    FadeOut(vec2.get_entries()[0][1], vec2.get_entries()[1][1], vec2.get_entries()[1][2]),
                    ReplacementTransform(vec2.get_entries()[0][2], x2),
                    ReplacementTransform(vec2.get_brackets()[1], Ax2_vec.get_brackets()[1]))
        self.wait(8)

        Ax1_tex = MathTex(r"A", r"\vec{x}_1").move_to(Ax1_vec.get_center()).next_to(x1)
        plus3 = MathTex("+").next_to(Ax1_tex)
        x2_copy = x2.copy().next_to(plus3)
        Ax2_tex = MathTex(r"A", r"\vec{x}_2").move_to(Ax2_vec.get_center()).next_to(x2_copy)
        self.play(ReplacementTransform(Ax1_vec, Ax1_tex), 
                ReplacementTransform(plus2, plus3), 
                ReplacementTransform(Ax2_vec, Ax2_tex),
                ApplyMethod(x2.next_to, plus3))
        result2 = VGroup(x1, Ax1_tex, plus3, x2, Ax2_tex)
        self.wait(4)

        A_sum_xy = MathTex(r"A", r"(", r"x^{\#}_1(\vec{x})", r"\cdot", r"\vec{x}_1", r"+", r"x^{\#}_1(\vec{x})", r"\cdot", r"\vec{x}_1", ")").next_to(equals)
        self.play(ReplacementTransform(x1, A_sum_xy[2]),
                    ReplacementTransform(Ax1_tex[0], A_sum_xy[0]),
                    FadeIn(A_sum_xy[1], A_sum_xy[3]),
                    ReplacementTransform(Ax1_tex[1], A_sum_xy[4]),
                    ReplacementTransform(plus3, A_sum_xy[5]),
                    ReplacementTransform(x2, A_sum_xy[6]),
                    FadeIn(A_sum_xy[7]),
                    ReplacementTransform(Ax2_tex[1], A_sum_xy[8]),
                    ReplacementTransform(Ax2_tex[0], A_sum_xy[9]))
        self.wait(3)

        Ax_E = MathTex(r"(A\vec{x})_{\mathcal{E}}").scale(1.2).next_to(equals)
        self.play(ReplacementTransform(A_sum_xy, Ax_E))
        self.play(ApplyMethod(VGroup(basis_matrix, coords_vec, equals, Ax_E).move_to, [0, -0.5, 0]))

        self.wait(8)
        rect1 = Rectangle(color=GREEN, height = 1.8, width = 0.8).move_to(basis_matrix.get_columns()[0].get_center())
        rect2 = Rectangle(color=RED, height = 1.8, width = 0.8).move_to(basis_matrix.get_columns()[1].get_center())
        Ax1_tex = MathTex(r"(A", r"\vec{x}_1", r")_{\mathcal{E}}").next_to(basis_matrix[0][2], DOWN).shift(0.8*DOWN + 0.2*LEFT)
        Ax1_tex[1].set_color(GREEN)
        Ax2_tex = MathTex(r"(A", r"\vec{x}_2", r")_{\mathcal{E}}").next_to(basis_matrix[0][3], DOWN).shift(0.8*DOWN + 0.2*RIGHT)
        Ax2_tex[1].set_color(RED)
        line_Ax1 = DashedLine(start=rect1.get_bottom()+0.1*DOWN, end=Ax1_tex.get_top()+0.1*UP, dash_length=0.05, dashed_ratio=0.5)
        line_Ax2 = DashedLine(start=rect2.get_bottom()+0.1*DOWN, end=Ax2_tex.get_top()+0.1*UP, dash_length=0.05, dashed_ratio=0.5)
        self.play(Create(rect1), Create(Ax1_tex), Create(line_Ax1))
        self.play(Create(rect2), Create(Ax2_tex), Create(line_Ax2))
        self.wait(3)
        
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{leftindex}")
        brace = Brace(VGroup(Ax1_tex, Ax2_tex))
        A_X_E = MathTex(r"\leftindex[T]^{\mathcal{X}} {A} ^\mathcal{E}", tex_template=tex_template).scale(1.2).next_to(brace, DOWN)
        self.play(Create(brace), Write(A_X_E))
        self.wait(3)
        A_X_E_copy = A_X_E.copy().next_to(coords_vec, LEFT)
        vec_x_X = MathTex(r"(\vec{x})_{\mathcal{X}}").scale(1.2).next_to(A_X_E_copy, RIGHT)
        equals_copy = equals.copy().next_to(vec_x_X, RIGHT)
        self.play(FadeOut(Ax1, Ax1_v, Ax2, Ax2_v, rect1, rect2, basis_matrix, line_Ax1, line_Ax2, Ax1_tex, Ax2_tex, brace),
                    ApplyMethod(A_X_E.next_to, vec_x_X, LEFT),
                    ReplacementTransform(coords_vec, vec_x_X),
                    ApplyMethod(equals.next_to, vec_x_X, RIGHT),
                    ApplyMethod(Ax_E.next_to, equals_copy))
        self.wait(7)

class FromBasisToStandardBasisVisual(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
                self,
                show_coordinates=True,
                show_basis_vectors=False,
                foreground_plane_kwargs= {
                "x_range": np.array([-25, 25, 1]),
                "y_range": np.array([-25, 25, 1]),
                },
                background_plane_kwargs= {
                "x_range": np.array([-25, 25, 1]),
                "y_range": np.array([-25, 25, 1]),
                }
            )
    def construct(self):
        basis = MathTex(r'\mathcal{X} = (', r'\vec{x}_1', r'=\begin{pmatrix}1\\2\end{pmatrix},',  r'\vec{x}_2', r'=\begin{pmatrix}-1\\1\end{pmatrix})').move_to([-4.5,3,0])
        basis.scale(0.7).add_background_rectangle()
        basis[2].set_color(GREEN)
        basis[4].set_color(RED)
        x_tex = MathTex(r'\vec{x} = \begin{pmatrix}3\\0\end{pmatrix}').set_color(YELLOW).scale(0.7).add_background_rectangle().next_to(basis)
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{leftindex}")
        A_X_E = MathTex(r"\leftindex[T]^{\mathcal{X}} {A} ^\mathcal{E} = ", tex_template=tex_template)
        basis_matrix_arr = np.array([[-2,-2], [-3, -1]])
        basis_matrix = Matrix(basis_matrix_arr, left_bracket="(", right_bracket=")").scale(1.2).next_to(A_X_E, RIGHT)
        matrix_group = VGroup(A_X_E, basis_matrix).scale(0.7).next_to(basis, DOWN).shift(0.2*DOWN).align_to(basis, LEFT).add_background_rectangle()
        self.add(basis, x_tex, matrix_group)
        self.wait(5)
        x1_arr = np.array([1,2])
        x1 = self.add_vector(x1_arr, color=GREEN)
        x1_lab = self.add_transformable_label(x1, r"\vec{x}_1", new_label=r"(\vec{x}_1)_{\mathcal{X}}", animate=False, at_tip=True)
        x1_lab.set_z_index(1)
        x1_rect = Rectangle(color=BLACK, width = x1_lab.width , height = x1_lab.height).set_opacity(0.7).move_to(x1_lab.get_center()).set_z_index(0)
        self.add(x1_rect)
        x2_arr = np.array([-1,1])
        x2 = self.add_vector(x2_arr, color=RED)
        x2_lab = self.add_transformable_label(x2, r"\vec{x}_2", new_label=r"(\vec{x}_2)_{\mathcal{X}}", animate=False, at_tip=True)
        x2_lab.set_z_index(1)
        x2_rect = Rectangle(color=BLACK, width = x2_lab.width , height = x2_lab.height).set_opacity(0.7).move_to(x2_lab.get_center()).set_z_index(0)
        self.add(x2_rect)
        self.wait(2)
        x_arr = np.array([3,-0])
        x = self.add_vector(x_arr, color=YELLOW)
        x_lab = self.add_transformable_label(x, r"\vec{x}", new_label=r"(\vec{x})_{\mathcal{X}} = \begin{pmatrix}1\\-2\end{pmatrix}", animate=False, at_tip=True)
        x_lab.set_z_index(1)
        x_rect = Rectangle(color=BLACK, width = x_lab.width , height = x_lab.height).set_opacity(0.7).move_to(x_lab.get_center()).set_z_index(0)
        self.add(x_rect)

        self.wait(7)
        
        matrix_of_base = np.transpose([x1_arr, x2_arr])
        self.remove(x1_rect, x2_rect, x_rect)
        self.apply_inverse(matrix_of_base)
        
        x1_lab.set_z_index(1)
        x1_rect = Rectangle(color=BLACK, width = x1_lab.width , height = x1_lab.height).set_opacity(0.7).move_to(x1_lab.get_center()).set_z_index(0)
        x2_lab.set_z_index(1)
        x2_rect = Rectangle(color=BLACK, width = x2_lab.width , height = x2_lab.height).set_opacity(0.7).move_to(x2_lab.get_center()).set_z_index(0)
        x_lab.set_z_index(1)
        x_rect = Rectangle(color=BLACK, width = x_lab.width , height = x_lab.height).set_opacity(0.7).move_to(x_lab.get_center()).set_z_index(0)
        self.add(x1_rect, x2_rect, x_rect)
        self.wait(3)



        basis_matrix2 = Matrix(basis_matrix_arr, left_bracket="(", right_bracket=")").scale(0.84).align_to(basis, UP).shift(2*RIGHT).set_z_index(2)
        backgr_rect = Rectangle(color=BLACK, width=basis_matrix2.width+0.3, height = basis_matrix2.height+0.3).set_opacity(0.75).move_to(basis_matrix2.get_center())
        coords = Matrix([[1], [-2]], left_bracket="(", right_bracket=")").scale(0.84).next_to(basis_matrix2).set_z_index(2)
        group = VGroup(basis_matrix2, coords)
        backgr_rect2 = Rectangle(color=BLACK, width=group.width+0.3, height = group.height+0.3).set_opacity(0.75).move_to(group.get_center())
        equals = MathTex("=").next_to(coords).set_z_index(2)
        group.add(equals)
        backgr_rect3 = Rectangle(color=BLACK, width=group.width+0.3, height = group.height+0.3)
        backgr_rect3.set_opacity(0.75).move_to(group.get_center())
        self.play(Write(basis_matrix2), Create(backgr_rect))
        self.play(Write(coords), ReplacementTransform(backgr_rect, backgr_rect2))
        self.play(Write(equals), ReplacementTransform(backgr_rect, backgr_rect3))
        self.wait(2)
        Ax = Matrix([[2], [-1]], left_bracket="(", right_bracket=")").scale(0.84).next_to(equals).set_z_index(2)
        group.add(Ax)
        backgr_rect4 = Rectangle(color=BLACK, width=group.width, height = group.height)
        backgr_rect4.set_opacity(0.75).move_to(group.get_center())
        self.play(Write(Ax), ReplacementTransform(backgr_rect3, backgr_rect4))
        self.wait(3)

        x1_lab.target_text = MathTex(r"(A", r"\vec{x}_1", r")_{\mathcal{E}} = \begin{pmatrix}-2\\-3\end{pmatrix}").scale(0.9).set_z_index(2)
        x1_lab.target_text[1].set_color(GREEN)

        x2_lab.target_text = MathTex(r"(A", r"\vec{x}_2", r")_{\mathcal{E}} = \begin{pmatrix}-2\\-1\end{pmatrix}").scale(0.9).set_z_index(2)
        x2_lab.target_text[1].set_color(RED)

        x_lab.target_text = MathTex(r"(A", r"\vec{x}", r")_{\mathcal{E}} = \begin{pmatrix}2\\-1\end{pmatrix}").scale(0.9).set_color(YELLOW).set_z_index(2)
        
        self.remove(x1_rect, x2_rect, x_rect)
        self.apply_matrix(basis_matrix_arr)
        x1_lab.set_z_index(1)
        x1_rect = Rectangle(color=BLACK, width = x1_lab.width , height = x1_lab.height).set_opacity(0.7).move_to(x1_lab.get_center()).set_z_index(0)
        x2_lab.set_z_index(1)
        x2_rect = Rectangle(color=BLACK, width = x2_lab.width , height = x2_lab.height).set_opacity(0.7).move_to(x2_lab.get_center()).set_z_index(0)
        x_lab.set_z_index(1)
        x_rect = Rectangle(color=BLACK, width = x_lab.width , height = x_lab.height).set_opacity(0.7).move_to(x_lab.get_center()).set_z_index(0)
        self.add(x1_rect, x2_rect, x_rect)
        self.wait(4)

class Motivation2(LinearTransformationScene, MovingCameraScene):
    def __init__(self):
        LinearTransformationScene.__init__(
                self,
                show_coordinates=True,
                show_basis_vectors=False,
                foreground_plane_kwargs= {
                "x_range": np.array([-20, 20, 1]),
                "y_range": np.array([-20, 20, 1]),
                },
                background_plane_kwargs= {
                "x_range": np.array([-20, 20, 1]),
                "y_range": np.array([-20, 20, 1]),
                }
            )
    def construct(self):
        self.camera.frame.scale(1.2)
        self.wait(4)
        x1_arr = np.array([2,-2])
        x1 = self.add_vector(x1_arr, color=GREEN)
        x1_lab = self.add_transformable_label(x1, r"\vec{x}_1", transformation_name="A", animate=False, at_tip=True)
        x2_arr = np.array([-1,-2])
        x2 = self.add_vector(x2_arr, color=RED)
        x2_lab = self.add_transformable_label(x2, r"\vec{x}_2", transformation_name="A", animate=False, at_tip=True)
        Ax1 = MathTex(r"(A\vec{x}_1)_{\mathcal{Y}}=\begin{pmatrix}1\\-2\end{pmatrix}").move_to([5,3,0])
        Ax2 = MathTex(r"(A\vec{x}_1)_{\mathcal{Y}}=\begin{pmatrix}-2\\-1\end{pmatrix}").next_to(Ax1, DOWN)
        self.wait(2)
        self.play(Write(Ax1))
        self.wait(2)
        self.play(Write(Ax2))
        self.wait(5)
        basis_matrix_X = np.transpose(np.array([x1_arr, x2_arr]))
        basis_matrix_X_inverse = np.linalg.inv(basis_matrix_X)
        A_in_basis = np.array([[1, -2], [-2, -1]])
        y1_arr = np.array([-1,2])
        y2_arr = np.array([-1,-1])
        basis_matrix_X = np.transpose(np.array([x1_arr, x2_arr]))
        basis_matrix_Y = np.transpose(np.array([y1_arr, y2_arr]))
        A_E_Y_matrix = np.matmul(A_in_basis, basis_matrix_X_inverse)
        A_E_E_matrix = np.matmul(basis_matrix_Y, A_E_Y_matrix)
        self.apply_matrix(A_E_E_matrix)
        self.wait(4)

        x1_lab.target_text = MathTex(r"(A", r"\vec{x}_1", r")_{\mathcal{Y}} = \begin{pmatrix}1\\-2\end{pmatrix}").scale(0.9).set_z_index(2)
        x1_lab.target_text[1].set_color(GREEN)

        x2_lab.target_text = MathTex(r"(A", r"\vec{x}_2", r")_{\mathcal{Y}} = \begin{pmatrix}-2\\-1\end{pmatrix}").scale(0.9).set_z_index(2)
        x2_lab.target_text[1].set_color(RED)

        basis_matrix_Y_inverse = np.linalg.inv(basis_matrix_Y)
        y1 = self.add_vector(y1_arr, color=YELLOW)
        y1_lab = self.add_transformable_label(y1, r"\vec{y}_1", new_label=r"(\vec{y}_1)_{\mathcal{Y}}", animate=False, at_tip=True)
        y2 = self.add_vector(y2_arr, color=PINK)
        y2_lab = self.add_transformable_label(y2, r"\vec{y}_2", new_label=r"(\vec{y}_2)_{\mathcal{Y}}", animate=False, at_tip=True)
        self.wait(4)
        self.apply_matrix(basis_matrix_Y_inverse)
        self.wait(4)

class FromBasisToBasis(Scene):
    def construct(self):
        basis = MathTex(r'\mathcal{X} = (', r'\vec{x}_1', ',',  r'\vec{x}_2', ')').move_to([-4,3,0])
        basis[1].set_color(GREEN)
        basis[3].set_color(RED)
        basis_Y = MathTex(r'\mathcal{Y} = (', r'\vec{y}_1', ',',  r'\vec{y}_2', ')').next_to(basis, RIGHT).shift(0.3*RIGHT)
        basis_Y[1].set_color(YELLOW)
        basis_Y[3].set_color(PINK)
        Ax1 = MathTex(r"(A", r"\vec{x}_1", r")_{\mathcal{E}}=").align_to(basis, LEFT).shift(1.6*UP)
        Ax1[1].set_color(GREEN)
        Ax1_v = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN)], [MathTex(r"a_{21}").set_color(GREEN)]], left_bracket="(", right_bracket=")")
        Ax1_v.next_to(Ax1)
        Ax2 = MathTex(r"(A", r"\vec{x}_2", r")_{\mathcal{E}}=").next_to(Ax1_v, RIGHT).shift(0.3*RIGHT)
        Ax2[1].set_color(RED)
        Ax2_v = MobjectMatrix([[MathTex(r"a_{12}").set_color(RED)], [MathTex(r"a_{22}").set_color(RED)]], left_bracket="(", right_bracket=")")
        Ax2_v.next_to(Ax2)
        A_X_group = VGroup(Ax1, Ax1_v, Ax2, Ax2_v)
        self.add(basis, Ax1, Ax2, Ax1_v, Ax2_v)
        self.wait(6)
        basis_matrix = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN),MathTex(r"a_{12}").set_color(RED)], 
                                    [MathTex(r"a_{21}").set_color(GREEN), MathTex(r"a_{22}").set_color(RED)]], 
                                    left_bracket="(", 
                                    right_bracket=")").shift(2.5*LEFT + 0.4*DOWN)
        self.play(Write(basis_matrix))
        self.wait(3)
        vec_x_X = MathTex(r"(\vec{x})_{\mathcal{X}}").scale(1.2).next_to(basis_matrix)
        self.play(Write(vec_x_X))
        equals = MathTex("=").scale(1.2).next_to(vec_x_X)
        self.play(Write(equals))
        self.wait(2)
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{leftindex}")
        A_x_E = MathTex(r"(A\vec{x})_{\mathcal{E}}").scale(1.2).next_to(equals, RIGHT)
        self.play(Write(A_x_E))
        self.wait(4)
        
        self.play(Write(basis_Y))
        self.wait(4)
        Ax1_Y = MathTex(r"(A", r"\vec{x}_1", r")_{\mathcal{Y}}=").align_to(basis, LEFT).shift(1.6*UP)
        Ax1_Y[1].set_color(GREEN)
        Ax1_Y_v = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN)], [MathTex(r"a_{21}").set_color(GREEN)]], left_bracket="(", right_bracket=")")
        Ax1_Y_v.next_to(Ax1)
        Ax2_Y = MathTex(r"(A", r"\vec{x}_2", r")_{\mathcal{Y}}=").next_to(Ax1_v, RIGHT).shift(0.3*RIGHT)
        Ax2_Y[1].set_color(RED)
        Ax2_Y_v = MobjectMatrix([[MathTex(r"a_{12}").set_color(RED)], [MathTex(r"a_{22}").set_color(RED)]], left_bracket="(", right_bracket=")")
        Ax2_Y_v.next_to(Ax2)
        A_X_Y_group = VGroup(Ax1_Y, Ax1_Y_v, Ax2_Y, Ax2_Y_v)
        self.play(ReplacementTransform(A_X_group, A_X_Y_group))
        self.wait(2)
        
        A_x_Y = MathTex(r"(A\vec{x})_{\mathcal{Y}}").scale(1.2).next_to(equals, RIGHT)
        self.play(ReplacementTransform(A_x_E, A_x_Y))
        self.wait(2)

        self.wait(4)
        rect1 = Rectangle(color=GREEN, height = 1.8, width = 0.8).move_to(basis_matrix.get_columns()[0].get_center())
        rect2 = Rectangle(color=RED, height = 1.8, width = 0.8).move_to(basis_matrix.get_columns()[1].get_center())
        Ax1_tex = MathTex(r"(A", r"\vec{x}_1", r")_{\mathcal{Y}}").next_to(basis_matrix[0][2], DOWN).shift(0.8*DOWN + 0.2*LEFT)
        Ax1_tex[1].set_color(GREEN)
        Ax2_tex = MathTex(r"(A", r"\vec{x}_2", r")_{\mathcal{Y}}").next_to(basis_matrix[0][3], DOWN).shift(0.8*DOWN + 0.2*RIGHT)
        Ax2_tex[1].set_color(RED)
        line_Ax1 = DashedLine(start=rect1.get_bottom()+0.1*DOWN, end=Ax1_tex.get_top()+0.1*UP, dash_length=0.05, dashed_ratio=0.5)
        line_Ax2 = DashedLine(start=rect2.get_bottom()+0.1*DOWN, end=Ax2_tex.get_top()+0.1*UP, dash_length=0.05, dashed_ratio=0.5)
        self.play(Create(rect1), Create(Ax1_tex), Create(line_Ax1))
        self.play(Create(rect2), Create(Ax2_tex), Create(line_Ax2))
        self.wait(3)
        
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{leftindex}")
        brace = Brace(VGroup(Ax1_tex, Ax2_tex))
        A_X_Y = MathTex(r"\leftindex[T]^{\mathcal{X}} {A} ^\mathcal{Y}", tex_template=tex_template).scale(1.2).next_to(brace, DOWN)
        self.play(FadeIn(brace), Write(A_X_Y))
        self.wait(6)







class GetStandardMatrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
                self,
                show_coordinates=True,
                show_basis_vectors=False,
                foreground_plane_kwargs= {
                "x_range": np.array([-25, 25, 1]),
                "y_range": np.array([-25, 25, 1]),
                },
                background_plane_kwargs= {
                "x_range": np.array([-25, 25, 1]),
                "y_range": np.array([-25, 25, 1]),
                }
            )
    def construct(self):
        basis = MathTex(r'\mathcal{X} = (', r'\vec{x}_1', ',',  r'\vec{x}_2', r')').move_to([-5.5,3,0])
        basis.scale(0.8).add_background_rectangle()
        basis[2].set_color(GREEN)
        basis[4].set_color(RED)
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{leftindex}")
        A = MathTex(r"\leftindex[T]^{\mathcal{X}} {A} ^\mathcal{E}", r", \leftindex[T]^{\mathcal{E}} {A} ^\mathcal{E} = \ ?", tex_template=tex_template).scale(0.8).next_to(basis)
        self.add(basis, A[0])
        x1_arr = np.array([1,2])
        x1 = self.add_vector(x1_arr, color=GREEN)
        x1_lab = self.add_transformable_label(x1, r"\vec{x}_1", new_label=r"(\vec{x}_1)_{\mathcal{X}}", animate=False, at_tip=True)
        x2_arr = np.array([-1,1])
        x2 = self.add_vector(x2_arr, color=RED)
        x2_lab = self.add_transformable_label(x2, r"\vec{x}_2", new_label=r"(\vec{x}_2)_{\mathcal{X}}", animate=False, at_tip=True)
        x_arr = np.array([3,1])
        x = self.add_vector(x_arr, color=YELLOW)
        x_lab = self.add_transformable_label(x, r"\vec{x}", new_label=r"(\vec{x})_{\mathcal{X}}", animate=False, at_tip=True)
        
        e1 = self.add_vector([1,0], color=BLUE)
        e1_lab = self.add_transformable_label(e1, r'\vec{e}_1', new_label=r"(\vec{e}_1)_{\mathcal{X}}", animate=False, at_tip=True)
        e2 = self.add_vector([0,1], color=PINK)
        e2_lab = self.add_transformable_label(e2, r'\vec{e}_2', new_label=r"(\vec{e}_2)_{\mathcal{X}}", animate=False, at_tip=True)


        self.wait(2)
        self.play(Write(A[1]))
        self.wait(5)
        A_on_x_E = MathTex(r"\leftindex[T]^{\mathcal{E}} {A} ^\mathcal{E} (\vec{x})_{\mathcal{E}}", tex_template=tex_template).scale(0.8).align_to(basis, LEFT).shift(2*UP)
        self.play(Write(A_on_x_E))
        self.wait(2)
        A_on_x_X = MathTex(r"=\leftindex[T]^{\mathcal{X}} {A} ^\mathcal{E}", r"(\vec{x})_{\mathcal{X}}", tex_template=tex_template).scale(0.8).next_to(A_on_x_E)
        self.play(Write(A_on_x_X))
        self.wait(3)
        
        rect = Rectangle(color=YELLOW, width = A_on_x_X[1].width+0.15, height=A_on_x_X[1].height+0.15).move_to(A_on_x_X[1].get_center())
        self.play(Create(rect))
        self.moving_mobjects.remove(rect)
          
        matrix_of_base = np.transpose([x1_arr, x2_arr])
        self.apply_inverse(matrix_of_base)
        self.wait(3)

        change_of_basis = MathTex(r"\leftindex[T]^{\mathcal{E}} {I} ^\mathcal{X} = ", r"((", r"\vec{e}_1", r")_{\mathcal{X}}, (", r"\vec{e}_1", r")_{\mathcal{X}})", tex_template=tex_template)
        change_of_basis[2].set_color(BLUE)
        change_of_basis[4].set_color(PINK)
        change_of_basis.scale(0.8).align_to(basis, UP).shift(4*RIGHT).set_z_index(2)
        backgr_rect = Rectangle(color=BLACK, width = VGroup(change_of_basis[1:]).width, height=VGroup(change_of_basis[1:]).height).move_to(VGroup(change_of_basis[1:]).get_center()).set_opacity(0.75)
        self.play(Write(change_of_basis[1:]), Create(backgr_rect))
        self.wait(2)
        backgr_rect2 = Rectangle(color=BLACK, width = change_of_basis.width, height=change_of_basis.height).move_to(change_of_basis.get_center()).set_opacity(0.75)
        self.play(Write(change_of_basis[0]), ReplacementTransform(backgr_rect, backgr_rect2))
        self.wait(3)

        basis_change = MathTex(r" = \leftindex[T]^{\mathcal{X}} {A} ^\mathcal{E} \leftindex^{\mathcal{E}} {I} ^\mathcal{X} (\vec{x})_{\mathcal{E}}", tex_template=tex_template).scale(0.8).align_to(A_on_x_X, LEFT).shift(UP)
        self.play(Write(basis_change))
        self.wait(3)