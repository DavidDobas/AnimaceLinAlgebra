from manim import *
class Opening3DScene(Scene):
    def construct(self):
        title = Tex(r"Lineární obaly v $\mathbb{R}^3$ nad $\mathbb{R}$")
        title.add_background_rectangle()
        self.add(title)
        self.wait(5)


class Span3D(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        labels = VGroup(axes.get_x_axis_label(Tex("$x$")), 
                        axes.get_y_axis_label(Tex("$y$")),       
                        axes.get_z_axis_label(Tex("$z$")))
        self.set_camera_orientation(phi=60 * DEGREES, theta=-20 * DEGREES)

        def param_plane(u, v):
            x = u
            y = v
            z = 2*x-y
            return np.array([x, y, z])

        plane = Surface(
            param_plane,
            #resolution=(resolution_fa, resolution_fa),
            v_range=[-3, +3],
            u_range=[-3, +3]
        )

        #plane.scale_about_point(2, ORIGIN)
        plane.set_style(fill_opacity=0.5, fill_color=GREY, stroke_width=0)
        #plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)

        self.add(axes, labels)


        def scale_vec(original_vec, previous_vec, scalar, color):
            scaled = Arrow3D(start=np.array([0, 0, 0]), end=scalar*original_vec.get_end(), color=color)
            self.play(ReplacementTransform(previous_vec, scaled))
            return scaled

        self.begin_ambient_camera_rotation(rate=0.15)

        u = np.array([2,3,1])
        norm_u = 1.7*u/np.linalg.norm(u)
        vec_u=Arrow3D(start=np.array([0, 0, 0]), end=norm_u, color=BLUE)
        self.play(FadeIn(vec_u))
        self.wait(3)

        scaled = scale_vec(vec_u, vec_u,  1.8, color=BLUE)
        self.wait(3)

        scaled = scale_vec(vec_u, scaled, -1.3, color=BLUE)
        self.wait(3)

        scaled = scale_vec(vec_u, scaled, 1.7, color=BLUE)
        self.wait(3)

        line_u = Line3D(start=-5*u, end=5*u, thickness=0.01)
        self.play(FadeIn(line_u))
        self.wait(5)

        self.play(FadeOut(line_u, scaled))
        self.wait(5)

        u = np.array([2,3,1])
        v = np.array([1,-1,3])
        norm_u,norm_v=1.5*u/np.linalg.norm(u),1.5*v/np.linalg.norm(v)
        vec_u=Arrow3D(start=np.array([0, 0, 0]), end=norm_u, color=BLUE)
        vec_v=Arrow3D(start=np.array([0, 0, 0]), end=norm_v, color=RED)
        self.play(FadeIn(vec_u))
        self.play(FadeIn(vec_v))
        
        
        #self.begin_3dillusion_camera_rotation(rate=1)
        #self.play(self.camera.set_phi, 70 * DEGREES, run_time=6, rate_func=there_and_back)
        
        line_u = Line3D(start=-5*u, end=5*u, thickness=0.01)
        line_v = Line3D(start=-5*v, end=5*v, thickness=0.01)

        self.wait(4)
        self.play(FadeIn(line_u))
        self.play(FadeIn(line_v))
        self.wait(2)
        self.play(FadeIn(plane))
        self.wait(6)
        start_comb = [1.5, 1.2]
        
        def vector_with_projections(combination, u, v):
            w = combination[0]*u+combination[1]*v
            vec_w=Arrow3D(start=np.array([0, 0, 0]), end=w, color=PINK)
            line_wu = Line3D(start=combination[0]*u, end=w)
            line_wv = Line3D(start=combination[1]*v, end=w)
            return [vec_w, line_wu, line_wv]

        start_comb = [1.5, 1.2]
        w_with_projections = vector_with_projections(start_comb, norm_u, norm_v)
        
        self.add(w_with_projections[0])
        self.wait(1)
        self.add(w_with_projections[1], w_with_projections[2])
        w_group = VGroup(w_with_projections[0],w_with_projections[1], w_with_projections[2])
        self.wait(3)
        
        next_comb = [1.3, -1.8]
        next_w = vector_with_projections(next_comb, norm_u, norm_v)
        #vec_next_w=Arrow3D(start=np.array([0, 0, 0]), end=next_w, color=PINK)
        #u_scalars = range(start_comb[0], start_comb[0]-3, 0.5)
        #v_scalars = range(start_comb[1], start_comb[1]+3, 0.5)
        #v_groups = [i*norm_u + j*norm_v for (i, j) in list(zip(u_scalars, v_scalars))]
        #self.play(ReplacementTransform(u_group, v_group)) for v_group in v_groups
        next_w_group = VGroup(next_w[0],next_w[1],next_w[2])
        self.play(ReplacementTransform(w_group, next_w_group))
        self.wait(2)

        next_comb = [-1.3, -1.8]
        next_w2 = vector_with_projections(next_comb, norm_u, norm_v)
        next_w2_group = VGroup(next_w2[0],next_w2[1],next_w2[2])
        self.play(ReplacementTransform(next_w_group, next_w2_group))

        self.wait(2)
        next_comb = [-1.3, -1.8]
        next_w3 = vector_with_projections(next_comb, norm_u, norm_v)
        next_w3_group = VGroup(next_w3[0],next_w3[1],next_w3[2])
        self.play(ReplacementTransform(next_w2_group, next_w3_group))
        self.wait(5)

        """

        self.stop_ambient_camera_rotation()
        """



class Span2D(VectorScene):
    def construct(self):
        title = Tex(r"Lineární obaly v $\mathbb{R}^2$ nad $\mathbb{R}$")
        title.add_background_rectangle()
        self.add(title)
        self.wait(5)

        one_span = MathTex(r"[\vec{x}]_{\lambda} = \alpha\cdot\vec{x} \quad \alpha \in \mathbb{R}")
        one_span.shift(0.6*UP)
        two_span = MathTex(r"[\vec{x}, \vec{y}]_{\lambda} = \alpha\cdot\vec{x} + \beta\cdot\vec{y} \quad \alpha, \beta \in \mathbb{R}")
        two_span.shift(0.2*DOWN)
        self.play(ApplyMethod(title.shift, 1.5*UP))
        self.play(Write(one_span))
        self.wait(5)
        self.play(Write(two_span))
        self.wait(10)


        self.play(FadeOut(title, one_span, two_span))
        self.wait(1)

        plane = NumberPlane()
        plane.add_coordinates()
        plane.set_z_index(0)
        self.play(Create(plane))

        self.wait(3)
        
        def create_vect(array, color, label):
            x = array
            vec = Vector(x, color=color).set_z_index(2)
            vec_label = label
            shift = [0,0.3,0] if x[1]>0 else [0,-0.3,0]
            vec_label.move_to(x+0.3*x/np.linalg.norm(x)+shift)
            return vec, vec_label

        def scale_vec(previous_vec_group, original_vec_array, scalar, label, color=GREEN):
            alpha_x_vec, alpha_x_label = create_vect(scalar*original_vec_array, color, label)
            alpha_x = VGroup(alpha_x_vec, alpha_x_label)           
            self.play(ReplacementTransform(previous_vec_group, alpha_x))
            self.wait(1)
            return alpha_x

        def eng_to_cz_number(number):
            numbers=str(number).split(".")
            return(numbers[0]+','+numbers[1])

        ### One Vector
        x_array = np.array([4,-2,0])
        x_vec, x_label = create_vect(x_array, GREEN, MathTex(r"\vec{x}"))
        x = VGroup(x_vec, x_label)
        self.play(GrowArrow(x_vec), FadeIn(x_label))
        self.wait(5)
       
        scalars = [1.2, 1.3, 0.8, -0.5, -0.9, -1.4]
        new = scale_vec(x, x_array, 1.1, MathTex(r"1,1\cdot\vec{x}"))
        for scalar in scalars:
            new = scale_vec(new, x_array, scalar, MathTex(eng_to_cz_number(scalar)+r"\cdot\vec{x}"))

        

        x_array = np.array([4,-2,0])
        x_vec, x_label = create_vect(x_array, GREEN, MathTex(r"\vec{x}"))
        x = VGroup(x_vec, x_label)

        self.play(ReplacementTransform(new, x))
        self.wait(2)

        y_array = -1.2*x_array
        y_vec, y_label = create_vect(y_array, RED, MathTex(r"\vec{y}"))
        y_label.shift(0.7*RIGHT)
        self.play(GrowArrow(y_vec), FadeIn(y_label))
        y = VGroup(y_vec, y_label)
        self.wait(3)

        target_x_vec, target_x_label = create_vect(y_array, GREEN, MathTex(r"\vec{y} = -1,2\cdot\vec{x}"))
        target_x_vec.set_z_index(3)
        target_x_label.shift(1.5*RIGHT)
        target_x = VGroup(target_x_vec, target_x_label)

        self.play(ReplacementTransform(x, target_x), FadeOut(y_label))
        self.wait(5)

        line = Line(start=-5*x_array, end=5*x_array, color=WHITE).set_z_index(1)
        self.play(FadeIn(line))
        self.wait(3)

        self.play(FadeOut(y_vec, target_x, line))
        
        ### Two Vectors
        x_array = np.array([4,-2,0])
        x_vec, x_label = create_vect(x_array, GREEN, MathTex(r"\vec{x}"))
        line_x = Line(start=-5*x_array, end=5*x_array, color=WHITE).set_z_index(1).set_opacity(0.5)
        x = VGroup(x_vec, x_label)
        self.play(GrowArrow(x_vec), FadeIn(x_label, line_x))
        self.wait(1)

        y_array = np.array([3,2,0])
        y_vec, y_label = create_vect(y_array, RED, MathTex(r"\vec{y}"))
        line_y = Line(start=-5*y_array, end=5*y_array, color=WHITE).set_z_index(1).set_opacity(0.5)
        y = VGroup(y_vec, y_label)
        self.play(GrowArrow(y_vec), FadeIn(y_label, line_y))
        self.wait(1)

        alpha = 1.2
        beta=0.5
        alpha_x = scale_vec(x, x_array, alpha, MathTex(eng_to_cz_number(alpha)+r"\cdot\vec{x}"))
        self.wait(2)
        beta_y = scale_vec(y, y_array, beta, MathTex(eng_to_cz_number(beta)+r"\cdot\vec{y}"), color=RED)
        self.wait(2)
        z_array = alpha*x_array + beta*y_array
        z_vec, z_label = create_vect(z_array, YELLOW, MathTex(r"\vec{z}"))
        x_line = Line(start=z_array, end=alpha*x_array, color=WHITE).set_opacity(0.3)
        y_line = Line(start=z_array, end=beta*y_array, color=WHITE).set_opacity(0.3)
        group = VGroup(alpha_x[0], alpha_x[1], beta_y[0], beta_y[1], z_vec, z_label, x_line, y_line)
        self.play(FadeIn(x_line, y_line))
        self.wait(3)
        self.play(GrowArrow(z_vec), FadeIn(z_label))
        self.wait(5)

        

        def vector_and_base(previous_group, x_array, y_array, alpha, beta):
            z_array = alpha*x_array + beta*y_array
            x_vec, x_label = create_vect(alpha*x_array, GREEN, MathTex(eng_to_cz_number(alpha)+r"\vec{x}"))
            y_vec, y_label = create_vect(beta*y_array, RED, MathTex(eng_to_cz_number(beta)+r"\vec{y}"))
            z_vec, z_label = create_vect(z_array, YELLOW, MathTex(r"\vec{z}"))
            x_line = Line(start=z_array, end=alpha*x_array, color=WHITE).set_opacity(0.3)
            y_line = Line(start=z_array, end=beta*y_array, color=WHITE).set_opacity(0.3)
            z_group = VGroup(x_vec, x_label, y_vec, y_label, z_vec, z_label, x_line, y_line)
            self.play(ReplacementTransform(previous_group, z_group))
            return z_group
        
        
        

        group = vector_and_base(group, x_array, y_array, 0.7, 1.1)
        self.wait(3)
        group = vector_and_base(group, x_array, y_array, 0.7, -0.8)
        self.wait(3)
        group = vector_and_base(group, x_array, y_array, -0.5, -0.8)
        self.wait(3)
        group = vector_and_base(group, x_array, y_array, -0.8, 0.4)
        self.wait(3)
        group = vector_and_base(group, x_array, y_array, -0.7, 0.9)
        self.wait(3)


        x_array = np.array([4,-2,0])
        x_vec, x_label = create_vect(x_array, GREEN, MathTex(r"\vec{x}"))
        y_array = np.array([3,2,0])
        y_vec, y_label = create_vect(y_array, RED, MathTex(r"\vec{y}"))
        xy_group = VGroup(x_vec, x_label, y_vec, y_label)
        self.play(ReplacementTransform(group, xy_group))
        self.wait(5)
        alpha = -0.7
        beta = -0.5
        z_array = alpha*x_array + beta*y_array
        z_vec, z_label = create_vect(z_array, YELLOW, MathTex(r"\vec{z}"))
        self.play(GrowArrow(z_vec), FadeIn(z_label))
        self.wait(2)
        x_line = Line(start=z_array, end=alpha*x_array, color=WHITE).set_opacity(0.3)
        y_line = Line(start=z_array, end=beta*y_array, color=WHITE).set_opacity(0.3)
        self.play(Create(x_line))
        self.play(Create(y_line))
        
        x = VGroup(x_vec, x_label)
        y = VGroup(y_vec, y_label)
        scale_vec(x, x_array, alpha, MathTex(eng_to_cz_number(alpha)+r"\cdot\vec{x}"))
        scale_vec(y, y_array, beta, MathTex(eng_to_cz_number(beta)+r"\cdot\vec{y}"), RED)

        self.wait(10)



class ScaleTest(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        labels = VGroup(axes.get_x_axis_label(Tex("$x$")), 
                        axes.get_y_axis_label(Tex("$y$")),       
                        axes.get_z_axis_label(Tex("$z$")))
        self.set_camera_orientation(phi=60 * DEGREES, theta=-20 * DEGREES)
        self.add(axes, labels)
        
        w = np.array([1,1,0])
        vec_w = Arrow3D(start=np.array([0, 0, 0]), end=w, color=GREY)
        self.add(vec_w)

        u = np.array([2,3,1])/2
        vec_u=Arrow3D(start=np.array([0, 0, 0]), end=u, color=BLUE)
        
        project_u = self.count_projection(u, w)
        line_ux = Line3D(start=project_u, end=u)
        vec_project_u = Arrow3D(start=np.array([0, 0, 0]), end=project_u, color=PINK)

        u_group = VGroup(vec_u, line_ux, vec_project_u)

        self.add(u_group)
        self.wait(2)
        v = np.array([2,3,1])
        w = np.array([1,1,0])
        
        vec_v=Arrow3D(start=np.array([0, 0, 0]), end=v, color=BLUE)
        project_v = self.count_projection(v, w)
        vec_project_v = Arrow3D(start=np.array([0, 0, 0]), end=project_v, color=PINK)
        line_vx = Line3D(start=project_v, end=v)

        v_group = VGroup(vec_v, line_vx, vec_project_v)
        self.play(ReplacementTransform(u_group, v_group))
        self.wait(2)

    # u is input vector, v vector to project on
    def count_projection(self, u, v):
        v_norm = np.linalg.norm(v)
        return (np.dot(u, v)/v_norm**2)*v