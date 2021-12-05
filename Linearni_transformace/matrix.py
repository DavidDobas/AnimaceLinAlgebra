from manim import *

class Introduction(Scene):
    def construct(self):
        title = Tex("Matice lineárního zobrazení").scale(1.5)
        title.add_background_rectangle()
        self.add(title)
        self.wait(6)
        self.play(ApplyMethod(title.shift, 2.5*UP))

        Ae1_1 = MathTex(r"A\begin{pmatrix}1\\0\end{pmatrix}=")
        Ae1_2 = MathTex(r"\begin{pmatrix}a_{11}\\a_{21}\end{pmatrix}").next_to(Ae1_1, RIGHT).set_color(GREEN)
        Ae1 = VGroup(Ae1_1, Ae1_2).move_to(0.5*UP+2*LEFT)
        Ae2_1 = MathTex(r"A\begin{pmatrix}0\\1\end{pmatrix}=")
        Ae2_2 = MathTex(r"\begin{pmatrix}a_{12}\\a_{22}\end{pmatrix}").next_to(Ae2_1, RIGHT).set_color(RED)
        Ae2 = VGroup(Ae2_1, Ae2_2).move_to(0.5*UP+2*RIGHT)

        self.play(Write(Ae1))
        self.wait(1)
        self.play(Write(Ae2))
        self.wait(12)

        matrix1 = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN), MathTex(r"a_{12}").set_color(RED)], [MathTex(r"a_{21}").set_color(GREEN), MathTex(r"a_{22}").set_color(RED)]],
            left_bracket="(",
            right_bracket=")").shift(1.5*DOWN)
        self.play(Write(matrix1))
        self.wait(3)

        self.play(ApplyMethod(matrix1[0][1].move_to, matrix1[0][2].get_center()), ApplyMethod(matrix1[0][2].move_to, matrix1[0][1].get_center()))
        self.wait(3)
        self.play(ApplyMethod(matrix1[0][1].move_to, matrix1[0][0].get_center()), ApplyMethod(matrix1[0][0].move_to, matrix1[0][1].get_center()))
        self.wait(1)
        matrix2 = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN), MathTex(r"a_{12}").set_color(RED), MathTex(r"a_{21}").set_color(GREEN), MathTex(r"a_{22}").set_color(RED)]],
            left_bracket="(",
            right_bracket=")").shift(1.5*DOWN)
        self.play(ReplacementTransform(matrix1, matrix2))
        self.wait(3)
        matrix = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN), MathTex(r"a_{12}").set_color(RED)], [MathTex(r"a_{21}").set_color(GREEN), MathTex(r"a_{22}").set_color(RED)]],
            left_bracket="(",
            right_bracket=")").shift(1.5*DOWN)
        self.play(ReplacementTransform(matrix2, matrix))
        self.wait(11)
        self.play(ApplyMethod(matrix.shift, 2.5*LEFT))
        e1 = Matrix([[1],[0]],
                    left_bracket="(",
                    right_bracket=")").next_to(matrix)
        self.play(Write(e1))
        equals = MathTex(r"=").next_to(e1)
        self.play(Write(equals))
        self.wait(2)
        result = MobjectMatrix([[MathTex(r'a_{11}').set_color(GREEN)], [Rectangle(color=BLACK, height=0.5, width=1)]],
            left_bracket="(",
            right_bracket=")",
            element_alignment_corner=DL).next_to(equals)
        circle1 = Circle(radius=0.45, color=RED).move_to(matrix[0][0].get_center())
        circle2 = Circle(radius=0.45, color=RED).move_to(e1[0][0].get_center())
        self.play(Write(circle1), Write(circle2), Write(result))
        self.wait(1)
        result2 = MobjectMatrix([[MathTex(r'a_{11}', '+', '0')], [Rectangle(color=BLACK, height=0.5, width=1)]],
            left_bracket="(",
            right_bracket=")",
            element_alignment_corner=DL).next_to(equals)
        result2[0][0][0].set_color(GREEN)
        result2[0][0][2].set_color(RED)
        self.play(ApplyMethod(circle1.move_to, matrix[0][1].get_center()),
                    ApplyMethod(circle2.move_to, e1[0][1].get_center()), 
                    ReplacementTransform(result, result2))
        self.wait(1)
        result3 = MobjectMatrix([[MathTex(r'a_{11}', '+', '0')], [MathTex(r'a_{21}').set_color(GREEN)]],
            left_bracket="(",
            right_bracket=")",
            element_alignment_corner=DL).next_to(equals)
        result3[0][0][0].set_color(GREEN)
        result3[0][0][2].set_color(RED)
        self.play(ApplyMethod(circle1.move_to, matrix[0][2].get_center()),
                    ApplyMethod(circle2.move_to, e1[0][0].get_center()), 
                    ReplacementTransform(result2, result3))
        self.wait(1)
        result4 = MobjectMatrix([[MathTex(r'a_{11}', '+', '0')], [MathTex(r'a_{21}', '+', '0')]],
            left_bracket="(",
            right_bracket=")",
            element_alignment_corner=DL).next_to(equals)
        result4[0][0][0].set_color(GREEN)
        result4[0][0][2].set_color(RED)
        result4[0][1][0].set_color(GREEN)
        result4[0][1][2].set_color(RED)
        self.play(ApplyMethod(circle1.move_to, matrix[0][3].get_center()),
                    ApplyMethod(circle2.move_to, e1[0][1].get_center()), 
                    ReplacementTransform(result3, result4))
        self.wait(1)
        result = MobjectMatrix([[MathTex(r'a_{11}').set_color(GREEN)], [MathTex(r'a_{21}').set_color(GREEN)]],
            left_bracket="(",
            right_bracket=")").next_to(equals)
        self.play(ReplacementTransform(result4, result), FadeOut(circle1, circle2))
        self.play(ApplyMethod(VGroup(matrix, e1, equals, result).move_to, [0,-1.5,0]))
        self.wait(5)
        result_e2 = MobjectMatrix([[MathTex(r'a_{12}').set_color(RED)], [MathTex(r'a_{22}').set_color(RED)]],
            left_bracket="(",
            right_bracket=")").next_to(equals)
        self.play(ApplyMethod(e1[0][0].move_to, e1[0][1].get_center()),
                    ApplyMethod(e1[0][1].move_to, e1[0][0].get_center()), 
                    ReplacementTransform(result, result_e2))
        self.wait(5)
        
        vec = MobjectMatrix([[MathTex("x")],[MathTex("y")]],
                    left_bracket="(",
                    right_bracket=")").next_to(matrix)
        
        res1 = MathTex(r"a_{11}", r"\cdot", r"x", r"+", r"a_{12}", r'\cdot', r'y')
        res1[0].set_color(GREEN)
        res1[4].set_color(RED)
        res1.set_opacity(0)
        res2 = MathTex(r"a_{21}", r"\cdot", r"x", r"+", r"a_{22}", r'\cdot', r'y')
        res2[0].set_color(GREEN)
        res2[4].set_color(RED)
        res2.set_opacity(0)
        result = MobjectMatrix([[res1],[res2]],
                    left_bracket="(",
                    right_bracket=")").next_to(equals)
        self.play(ReplacementTransform(e1, vec), ReplacementTransform(result_e2, result))
        self.play(ApplyMethod(VGroup(matrix, vec, equals, result).move_to, [0,-1.5,0]))

        circle1 = Circle(radius=0.45, color=RED).move_to(matrix[0][0].get_center())
        circle2 = Circle(radius=0.45, color=RED).move_to(vec[0][0].get_center())
        self.play(Write(circle1), Write(circle2),ApplyMethod(res1[0:3].set_opacity, 1))
        self.wait(1)

        self.play(ApplyMethod(circle1.move_to, matrix[0][1].get_center()),
                    ApplyMethod(circle2.move_to, vec[0][1].get_center()), 
                    ApplyMethod(res1.set_opacity, 1))
        self.wait(1)
        self.play(ApplyMethod(circle1.move_to, matrix[0][2].get_center()),
                    ApplyMethod(circle2.move_to, vec[0][0].get_center()), 
                    ApplyMethod(res2[0:3].set_opacity, 1))
        self.wait(1)
        self.play(ApplyMethod(circle1.move_to, matrix[0][3].get_center()),
                    ApplyMethod(circle2.move_to, vec[0][1].get_center()), 
                    ApplyMethod(res2.set_opacity, 1))
        self.wait(5)

        vec1 = MobjectMatrix([[VGroup(res1[0].copy(), res1[1].copy(), res1[2].copy())],[VGroup(res2[0].copy(), res2[1].copy(), res2[2].copy())]],
                    left_bracket="(",
                    right_bracket=")").next_to(equals)
        plus = MathTex("+").next_to(vec1)
        vec2 = MobjectMatrix([[VGroup(res1[4].copy(), res1[5].copy(), res1[6].copy())],[VGroup(res2[4].copy(), res2[5].copy(), res2[6].copy())]],
                    left_bracket="(",
                    right_bracket=")").next_to(plus)

        self.play(ReplacementTransform(result.get_brackets()[0], vec1.get_brackets()[0]),
                    ReplacementTransform(VGroup(res1[0], res1[1], res1[2]), vec1.get_entries()[0]),
                    ReplacementTransform(VGroup(res2[0], res2[1], res2[2]), vec1.get_entries()[1]),
                    ReplacementTransform(res1[3], plus),
                    ReplacementTransform(res2[3], vec1.get_brackets()[1]),
                    FadeIn(vec2.get_brackets()[0]),
                    ReplacementTransform(VGroup(res1[4], res1[5], res1[6]), vec2.get_entries()[0]),
                    ReplacementTransform(VGroup(res2[4], res2[5], res2[6]), vec2.get_entries()[1]),
                    ReplacementTransform(result.get_brackets()[1], vec2.get_brackets()[1]),
                    FadeOut(circle1, circle2))
        self.wait(3)


        x = MathTex("x").next_to(equals)   
        Ae1_vec = MobjectMatrix([[MathTex(r"a_{11}").set_color(GREEN)], [MathTex(r"a_{21}").set_color(GREEN)]],
                    left_bracket="(",
                    right_bracket=")")
        Ae1_vec.next_to(x)
        plus2 = MathTex("+").next_to(Ae1_vec)
        y = MathTex("y").next_to(plus2)
        Ae2_vec = MobjectMatrix([[MathTex(r"a_{12}").set_color(RED)], [MathTex(r"a_{22}").set_color(RED)]],
                    left_bracket="(",
                    right_bracket=")")
        Ae2_vec.next_to(y)
        result3 = VGroup(VGroup(x, Ae1_vec), plus2, VGroup(y, Ae2_vec))
        self.play(ReplacementTransform(vec1.get_brackets()[0], Ae1_vec.get_brackets()[0]),
                    ReplacementTransform(vec1.get_entries()[0][0], Ae1_vec.get_entries()[0]),
                    ReplacementTransform(vec1.get_entries()[1][0], Ae1_vec.get_entries()[1]),
                    FadeOut(vec1.get_entries()[0][1], vec1.get_entries()[1][1], vec1.get_entries()[1][2]),
                    ReplacementTransform(vec1.get_entries()[0][2], x),
                    ReplacementTransform(plus, plus2),
                    ReplacementTransform(vec1.get_brackets()[1], Ae1_vec.get_brackets()[1]),
                    ReplacementTransform(vec2.get_brackets()[0], Ae2_vec.get_brackets()[0]),
                    ReplacementTransform(vec2.get_entries()[0][0], Ae2_vec.get_entries()[0]),
                    ReplacementTransform(vec2.get_entries()[1][0], Ae2_vec.get_entries()[1]),
                    FadeOut(vec2.get_entries()[0][1], vec2.get_entries()[1][1], vec2.get_entries()[1][2]),
                    ReplacementTransform(vec2.get_entries()[0][2], y),
                    ReplacementTransform(vec2.get_brackets()[1], Ae2_vec.get_brackets()[1]))
        self.wait(3)

        Ae1_tex = MathTex(r"A", r"\begin{pmatrix}1\\0\end{pmatrix}").move_to(Ae1_vec.get_center())
        Ae2_tex = MathTex(r"A", r"\begin{pmatrix}0\\1\end{pmatrix}").move_to(Ae2_vec.get_center())
        self.play(ReplacementTransform(Ae1_vec, Ae1_tex), ReplacementTransform(Ae2_vec, Ae2_tex))
        result2 = VGroup(x, Ae1_tex, plus2, y, Ae2_tex)
        self.wait(4)

        A_sum_xy = MathTex(r"A", r"(", r"x", r"\cdot", r"\begin{pmatrix}1\\0\end{pmatrix}", r"+", "y", r"\cdot", r"\begin{pmatrix}0\\1\end{pmatrix}", ")").next_to(equals)
        self.play(ReplacementTransform(x, A_sum_xy[2]),
                    ReplacementTransform(Ae1_tex[0], A_sum_xy[0]),
                    FadeIn(A_sum_xy[1], A_sum_xy[3]),
                    ReplacementTransform(Ae1_tex[1], A_sum_xy[4]),
                    ReplacementTransform(plus2, A_sum_xy[5]),
                    ReplacementTransform(y, A_sum_xy[6]),
                    FadeIn(A_sum_xy[7]),
                    ReplacementTransform(Ae2_tex[1], A_sum_xy[8]),
                    ReplacementTransform(Ae2_tex[0], A_sum_xy[9]))
        self.wait(3)

        Ax = MathTex(r"A\begin{pmatrix}x\\y\end{pmatrix}").next_to(equals)
        self.play(ReplacementTransform(A_sum_xy, Ax))
        self.play(ApplyMethod(VGroup(matrix, vec, equals, Ax).move_to, [0,-1.5,0]))
        self.wait(5)

        self.play(FadeOut(vec, equals, Ax, Ae1, Ae2), ApplyMethod(matrix.move_to, ORIGIN))
        self.wait(3)
        rect_e1 = Rectangle(color=GREEN, height = 1.8, width = 0.8).move_to([matrix[0][0].get_center()[0],0,0])
        rect_e2 = Rectangle(color=RED, height = 1.8, width = 0.8).move_to([matrix[0][1].get_center()[0],0,0])
        Ae1 = MathTex(r"A\vec{e}_1").next_to(matrix, DOWN).shift(0.8*DOWN + 1*LEFT)
        Ae2 = MathTex(r"A\vec{e}_2").next_to(matrix, DOWN).shift(0.8*DOWN + 1*RIGHT)
        line_Ae1 = DashedLine(start=rect_e1.get_bottom()+0.1*DOWN, end=Ae1.get_top()+0.1*UP, dash_length=0.05, dashed_ratio=0.5)
        line_Ae2 = DashedLine(start=rect_e2.get_bottom()+0.1*DOWN, end=Ae2.get_top()+0.1*UP, dash_length=0.05, dashed_ratio=0.5)
        self.play(Create(rect_e1), Create(rect_e2), Write(Ae1), Write(Ae2), Create(line_Ae1), Create(line_Ae2))
        self.wait(6)

class RotationMatrix(LinearTransformationScene, MovingCameraScene):
    def __init__(self):
        LinearTransformationScene.__init__(
                self,
                show_coordinates=False,
                show_basis_vectors=False,
                foreground_plane_kwargs= {
                "x_range": np.array([-20, 20, 1.0]),
                "y_range": np.array([-20, 20, 1.0]),
                "faded_line_ratio": 1,
                },
                background_plane_kwargs= {
                "x_range": np.array([-20, 20, 1.0]),
                "y_range": np.array([-20, 20, 1.0]),
                "faded_line_ratio": 1,
                }
            )
    def construct(self):
        self.camera.frame.scale(1.4)
        title = Tex("Rotace").scale(1.2).add_background_rectangle()
        title.shift(8*LEFT + 4*UP)
        self.wait(3)
        self.play(Create(title))
        self.wait(1)
        circle = Circle(radius=4, color=YELLOW)
        e1 = self.add_vector([4,0], color=GREEN)
        self.add_transformable_label(e1, r"\vec{e}_1", transformation_name="A", animate=False, at_tip=True)
        e2 = self.add_vector([0,4], color=RED)
        self.add_transformable_label(e2, r"\vec{e}_2", transformation_name="A", animate=False, at_tip=True)
        self.wait(2)
        self.play(Create(circle))
        self.wait(1)
        alpha = 1
        matrix = np.array([[np.cos(alpha), -np.sin(alpha)], 
                            [np.sin(alpha), np.cos(alpha)]])
        self.apply_matrix(matrix)
        arc = Arc(angle=alpha)
        arc_label = MathTex(r"\alpha").shift(0.3*UP+0.5*RIGHT)
        self.play(Create(arc), Write(arc_label))
        self.wait(5)
        line_Ae1_x = DashedLine((*np.matmul(matrix, (4,0)), 0), (np.cos(alpha)*4, 0,0))
        Ae1_x_label = MathTex(r"cos(\alpha)").next_to(line_Ae1_x, DOWN).add_background_rectangle()
        line_Ae1_y = DashedLine((*np.matmul(matrix, (4,0)), 0), (0, np.sin(alpha)*4, 0))
        Ae1_y_label = MathTex(r"sin(\alpha)").next_to(line_Ae1_y, LEFT).add_background_rectangle()
        self.play(Create(line_Ae1_x))
        self.play(Create(Ae1_x_label))
        self.wait(1)
        self.play(Create(line_Ae1_y))
        self.play(Create(Ae1_y_label))
        self.wait(2)
        cos = MathTex(r"cos(\alpha)").set_color(GREEN).set_opacity(0)
        sin = MathTex(r"sin(\alpha)").set_color(GREEN).set_opacity(0)
        minus_sin = MathTex(r"-sin(\alpha)").set_color(RED).set_opacity(0)
        cos2 = MathTex(r"cos(\alpha)").set_color(RED).set_opacity(0)
        A_matrix = MobjectMatrix([[cos, minus_sin],
                                [sin, cos2]],
                                left_bracket="(",
                                right_bracket=")",
                                h_buff=2)
        A_matrix.move_to([7,4,0])
        self.play(Write(A_matrix))
        self.play(ApplyMethod(cos.set_opacity, 1), ApplyMethod(sin.set_opacity, 1))
        self.wait(2)
        self.play(FadeOut(line_Ae1_x, Ae1_x_label, line_Ae1_y, Ae1_y_label))
        line_Ae2_x = DashedLine((*np.matmul(matrix, (0,4)), 0), (-np.sin(alpha)*4, 0,0))
        Ae2_x_label = MathTex(r"-sin(\alpha)").next_to(line_Ae2_x, DOWN).add_background_rectangle()
        line_Ae2_y = DashedLine((*np.matmul(matrix, (0,4)), 0), (0, np.cos(alpha)*4, 0))
        Ae2_y_label = MathTex(r"cos(\alpha)").next_to(line_Ae2_y, RIGHT).add_background_rectangle()
        self.play(Create(line_Ae2_x))
        self.play(Create(Ae2_x_label))
        self.wait(1)
        self.play(Create(line_Ae2_y))
        self.play(Create(Ae2_y_label))
        self.play(ApplyMethod(minus_sin.set_opacity, 1), ApplyMethod(cos2.set_opacity, 1))
        self.wait(7)

class ReflectionMatrix(LinearTransformationScene, MovingCameraScene):
    def __init__(self):
        LinearTransformationScene.__init__(
                self,
                show_coordinates=False,
                show_basis_vectors=False,
                foreground_plane_kwargs= {
                "x_range": np.array([-20, 20, 1.0]),
                "y_range": np.array([-20, 20, 1.0]),
                "faded_line_ratio": 1,
                },
                background_plane_kwargs= {
                "x_range": np.array([-20, 20, 1.0]),
                "y_range": np.array([-20, 20, 1.0]),
                "faded_line_ratio": 1,
                }
            )
    def construct(self):
        title = Tex("Zrcadlení podle osy").scale(1.2).add_background_rectangle()
        title.shift(5.88152942*LEFT + title.get_right()*RIGHT + 3*UP)
        self.add(title)
        self.wait(4)
        axis = Line(start=[-10,-10,0], end=[10,10,0]).set_color(WHITE)
        self.play(Create(axis))

        e1 = self.add_vector([2,0], color=GREEN)
        self.add_transformable_label(e1, r"\vec{e}_1", transformation_name="A", animate=False, at_tip=True)
        e2 = self.add_vector([0,2], color=RED)
        self.add_transformable_label(e2, r"\vec{e}_2", transformation_name="A", animate=False, at_tip=True)
        self.wait(2)

        reflection_matrix = np.array([[0,1], [1,0]])
        self.apply_matrix(reflection_matrix)
        self.wait(5)
        A_matrix = Matrix([[0, 1],
                                [1, 0]],
                                left_bracket="(",
                                right_bracket=")")
        A_matrix.move_to([5,3,0])
        
        self.play(Write(A_matrix.get_brackets()), Write(A_matrix.get_columns()[0]))
        self.wait(6)

        self.play(Write(A_matrix.get_columns()[1]))
        self.wait(8)

class DiagonalMatrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
                self,
                show_coordinates=False,
                show_basis_vectors=False,
            )
    def construct(self):
        e1 = self.add_vector([1,0], color=GREEN)
        self.add_transformable_label(e1, r"\vec{e}_1", transformation_name="A", animate=False, at_tip=True)
        e2 = self.add_vector([0,1], color=RED)
        self.add_transformable_label(e2, r"\vec{e}_2", transformation_name="A", animate=False, at_tip=True)
        self.wait(3)
        matrix = np.array([[3,0], [0,2]])
        A_matrix = Matrix(matrix,
                                left_bracket="(",
                                right_bracket=")",)
        A_matrix.move_to([4,2.5,0])
        self.play(Write(A_matrix))
        self.wait(2)
        self.apply_matrix(matrix)
        self.wait(6)