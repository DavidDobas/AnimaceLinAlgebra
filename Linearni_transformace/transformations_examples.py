from manim import *

class IntroExamples(Scene):
    def construct(self):
        title = Tex(r"Příklady").scale(1.5)
        title.add_background_rectangle()
        self.add(title)
        self.wait(5)

class Rotation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        title = Tex("Rotace").scale(1.2).add_background_rectangle()
        title.shift(5*LEFT + 3*UP)
        print(title.get_left())
        self.add(title)
        self.wait(2)
        x = self.add_vector([1,2,0], color=GREEN)
        self.add_transformable_label(x, 
                                    MathTex(r'\vec{x}', color=GREEN), 
                                    transformation_name="A", 
                                    animate=False)
        matrix = ([[np.cos(1),-np.sin(1)],[np.sin(1),np.cos(1)]])
        self.apply_matrix(matrix)
        self.wait(2)

class Shear(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        title = Tex("Zkosení").scale(1.2).add_background_rectangle()
        title.shift(5.88152942*LEFT + title.get_right()*RIGHT + 3*UP)
        self.add(title)
        self.wait(2)
        x = self.add_vector([1,2,0], color=GREEN)
        self.add_transformable_label(x, 
                                    MathTex(r'\vec{x}', color=GREEN), 
                                    transformation_name="A", 
                                    animate=False)
        matrix = ([[1,1.2],[0,1]])
        self.apply_matrix(matrix)
        self.wait(2)

class Stretch(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        title = Tex("Protažení ve směru x").scale(1.2).add_background_rectangle()
        title.shift(5.88152942*LEFT + title.get_right()*RIGHT + 3*UP)
        self.add(title)
        self.wait(2)
        x = self.add_vector([1,2,0], color=GREEN)
        self.add_transformable_label(x, 
                                    MathTex(r'\vec{x}', color=GREEN), 
                                    transformation_name="A", 
                                    animate=False)
        matrix = ([[2,0],[0,1]])
        self.apply_matrix(matrix)
        self.wait(2)


class AxisReflection(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        title = Tex("Zrcadlení podle osy").scale(1.2).add_background_rectangle()
        title.shift(5.88152942*LEFT + title.get_right()*RIGHT + 3*UP)
        self.add(title)
        self.wait(2)
        x = self.add_vector([1,2,0], color=GREEN)
        self.add_transformable_label(x, 
                                    MathTex(r'\vec{x}', color=GREEN), 
                                    transformation_name="A", 
                                    animate=False)
        self.wait(2)
        v = np.array([3,1,0])
        v = v/np.linalg.norm(v)
        axis = Line(-10*v, 10*v)
        self.play(Create(axis))
        self.wait(1)
        y = self.add_vector([3,1,0], color=RED)
        self.add_transformable_label(y, 
                                    MathTex(r'\vec{y}', color=RED), 
                                    transformation_name="A", 
                                    animate=False)
        self.wait(2)
        matrix = 1/5*np.array([[4,3],[3,-4]])
        self.apply_matrix(matrix)
        self.wait(2)

class PointReflection(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )
    def construct(self):
        title = Tex("Středová souměrnost podle počátku").scale(1.2).add_background_rectangle()
        title.shift(5.88152942*LEFT + title.get_right()*RIGHT + 3*UP)
        self.add(title)
        self.wait(4)
        x = self.add_vector([1,2,0], color=GREEN)
        self.add_transformable_label(x, 
                                    MathTex(r'\vec{x}', color=GREEN), 
                                    transformation_name="A", 
                                    animate=False)
        self.wait(2)
        matrix = np.array([[-1,0],[0,-1]])
        self.apply_matrix(matrix)
        self.wait(2)

