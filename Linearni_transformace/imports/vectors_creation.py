from manim import *

def create_vect(self, array, color, label, add=False):
        """
        Creates vector and its label.

        Parameters
        ----------
        array : Union[list, numpy.ndarray]
            Array of the vector
        color : str
            The color of the vector
        label : MathTex
            The label of the vector
        add: Bool, optional
            Whether to add to the Scene
        """
        x = np.array(array)
        vec = Vector(x, color=color).set_z_index(2)
        vec_label = label
        shift = np.array([0,0.4,0]) if x[1]>0 else np.array([0,-0.4,0])
        vec_label.move_to(x+0.1*x/np.linalg.norm(x)+shift)
        if add: self.play(GrowArrow(vec), FadeIn(label))
        return vec, vec_label

def create_sum_lines(self, x, y, opacity=0.5, add=False):
        """
        Creates lines connecting vectors with their sum.

        Parameters
        ----------
        x : Union[list, numpy.ndarray]
            First vector
        y : Union[list, numpy.ndarray]
            Second vector
        opacity : float, optional
            opacity of lines
        add: Bool, optional
            Whether to add to the Scene
        """
        x_arr = np.array(x)
        y_arr = np.array(y)
        sum_arr = x_arr + y_arr
        line_x = Line(x_arr, sum_arr).set_opacity(opacity)
        line_y = Line(y_arr, sum_arr).set_opacity(opacity)
        if add: self.play(Create(line_x), Create(line_y))
        return line_x, line_y

def change_linear_combination(self, x_array, y_array, x_label, y_label, z_label, x_color, y_color, z_color, x_scalar, y_scalar):
    """
        Scales two vectors, creates their sum and its parallelogram

        Parameters
        ----------
        self : VectorScene
        x_array : Union[list, numpy.ndarray]
            First vector
        y_array : Union[list, numpy.ndarray]
            Second vector
        x_label : MathTex
            Desired label of x
        y_label : MethTex
            Desired label of y
        z_label : MethTex
            Desired label of z
        """
    alpha_x, alpha_x_label = create_vect(self, x_scalar*x_array, x_color, x_label)
    beta_y, alpha_y_label = create_vect(self, y_scalar*y_array, y_color, y_label)
    line_alpha_x, line_alpha_y = create_sum_lines(self, x_scalar*x_array, y_scalar*y_array, opacity=0.5, add=False)
    new_z = x_scalar*x_array + y_scalar*y_array
    new_z_vec, new_z_label = create_vect(self, new_z, z_color, z_label)
    group = VGroup(alpha_x, alpha_x_label, beta_y, alpha_y_label, new_z_vec, new_z_label, line_alpha_x, line_alpha_y)
    return group
