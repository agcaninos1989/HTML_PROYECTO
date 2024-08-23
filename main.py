from manim import *

class leccion1(Scene):
    def construct(self):
        texto1 = Text("hola mundo")
        self.add(texto1)
        self.wait(5)


class leccion2(Scene):
    def construct(self):
        texto = Text("Curso De Manim")
        self.add(texto)
        self.wait(3)
        self.remove(texto)
        self.wait(3)


class leccion3(Scene):
    def construct(self):
        texto = Text("f(x) = x^2")
        self.play(FadeIn(texto))
        self.wait(3)
        self.play(FadeOut(texto))
        self.wait(3)
        self.play(Write(texto))
        self.wait(3)


class leccio8(Scene):
    def construct(self):
        texto1 = Text("Curso De Manim", color=PURPLE).move_to(UP * 3.5)
        texto2 = Text("Curso De Manim", color=BLUE).move_to(UP * 2.5)
        texto3 = Text("Curso De Manim", color=GREEN).move_to(UP * 1.5)
        self.play(Write(texto1))
        self.play(Write(texto2))
        self.play(Write(texto3))
        self.wait(3)


class leccio9(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        self.camera.background_color=color1
        texto1 = Text("Curso De Manim", color=color2).move_to(UP * 3.5).scale(2)
        texto2 = Text("Curso De Manim", color=color2).move_to(UP * 2.5).scale(1.5)
        texto3 = Text("Curso De Manim", color=color3).move_to(DOWN * 2).scale(1)
        texto4 = Text("Curso De Manim", color=color4).move_to(DOWN * 3).scale(0.5)
        self.play(Write(texto1))
        self.play(Write(texto2))
        self.play(Write(texto3))
        self.play(Write(texto4))
        self.wait(3)


class leccio10(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        texto1 =Text("PITAGORAS").scale(2).set_color_by_gradient(color1,color2,color3)
        self.play(Write(texto1))
        self.wait(4)




class leccion15(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        self.camera.background_color = color1
        esqn = MathTex("X==", "2.5").move_to(UP * 2 + LEFT * 2).scale(1.5)
        esqn2 = MathTex("Y==", "1.5").move_to(UP * 2 + RIGHT * 2).scale(1.5)
        esqn.set_color(color3)
        esqn2.set_color(color2)
        esqn3 = MathTex("Z=(", "2.5", ")^2+(", "1.5", ")^2", color=color4).move_to(DOWN).scale(1.5)
        self.play(Write(esqn))
        self.wait(3)
        self.play(Write(esqn2))
        self.wait(3)
        self.play(Write(esqn3[0]), Write(esqn3[2]), Write(esqn3[4]))
        self.wait(3)
        self.play(Transform(esqn[0],esqn3[1]), Transform(esqn2[0],esqn3[3]))
        self.wait(3)





class leccion17(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        self.camera.background_color = color1

        # Crear los textos matemáticos
        esqn = MathTex("X==", "2.5").move_to(UP * 2 + LEFT * 2).scale(1.5)
        esqn2 = MathTex("Y==", "1.5").move_to(UP * 2 + RIGHT * 2).scale(1.5)
        esqn3 = MathTex("Z=(", "2.5", ")^2+(", "1.5", ")^2", color=color4).move_to(DOWN).scale(1.5)

        # Establecer los colores de los textos
        esqn.set_color(color3)
        esqn2.set_color(color2)

        # Añadir y animar los textos
        self.play(Write(esqn))
        self.wait(3)
        self.play(Write(esqn2))
        self.wait(3)
        self.play(Write(esqn3[0]), Write(esqn3[2]), Write(esqn3[4]))
        self.wait(3)

        # Crear copias de los valores a transformar
        esqn_copy = esqn[1].copy()
        esqn2_copy = esqn2[1].copy()

        # Añadir las copias a la escena
        self.add(esqn_copy, esqn2_copy)

        # Transformar las copias
        self.play(Transform(esqn_copy, esqn3[1]), Transform(esqn2_copy, esqn3[3]))
        self.wait(3)


# Para renderizar la escena, usa el siguiente comando en la terminal:
# manim -pql nombre_del_archivo.py leccion15


class leccion16(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        self.camera.background_color = color1
        eqn0 = MathTex("x=", "2.5").move_to(UP * 2 + LEFT * 2).scale(1.5)
        eqn1 = MathTex("y=", "1.5").move_to(UP * 2 + RIGHT * 2).scale(1.5)
        eqn0.set_color(color3)
        eqn1.set_color(color2)
        eqn2 = MathTex("z=(", "2.5", ")^2+(", "1.5", ")^2", color=color4).move_to(DOWN).scale(1.5)
        self.play(Write(eqn0))
        self.wait(1)
        self.play(Write(eqn1))
        self.wait(3)
        self.play(Write(eqn2[0]), Write(eqn2[2]), Write(eqn2[4]))
        self.wait(3)
        self.play(Transform(eqn0[1],eqn2[1]),Transform(eqn1[1],eqn2[3]))
        self.wait(3)


from manim import *


class VectorArrow(Scene):
    def construct(self):
        # Crear el plano de coordenadas
        numberplane = NumberPlane()

        # Crear el punto de origen y el vector inicial
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0, color=BLUE)
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text_initial = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)

        # Añadir el plano de coordenadas, el punto de origen, el vector inicial y el texto
        self.add(numberplane, dot, arrow, origin_text, tip_text_initial)

        # Definir las nuevas posiciones del vector en cada cuadrante y sus colores
        new_positions = [[-2, 2, 0], [-2, -2, 0], [2, -2, 0], [2, 2, 0]]
        tip_texts = ["(-2, 2)", "(-2, -2)", "(2, -2)", "(2, 2)"]
        colors = [RED, GREEN, YELLOW, BLUE]

        # Animaciones para mover el vector a través de los cuadrantes con cambios de color
        for new_pos, tip_text, color in zip(new_positions, tip_texts, colors):
            tip_text_final = Text(tip_text).next_to(new_pos, RIGHT)
            self.play(
                arrow.animate.put_start_and_end_on(ORIGIN, new_pos).set_color(color),
                Transform(tip_text_initial, tip_text_final)
            )
            self.wait(2)


# Ejecutar la escena
if __name__ == "__main__":
    from manim import config

    config.media_width = "100%"
    config.verbosity = "WARNING"
    config.output_file = "VectorArrow"
    scene = VectorArrow()
    scene.render()






from manim import *

class PlanoInclinado(Scene):
    def construct(self):
        # Crear el plano inclinado
        plano = Polygon(
            [-4, 0, 0],
            [4, 0, 0],
            [4, 2.31, 0], # 2.31 es aproximadamente 4 * tan(30°)
            [-4, 0, 0],
            fill_opacity=0.2,
            color=BLUE
        )

        # Crear las masas
        masa1 = Square(side_length=0.5, color=RED, fill_opacity=1)
        masa1.move_to([-2, 0.75, 0])  # Ubicación aproximada para m1 en el plano inclinado
        masa2 = Square(side_length=0.5, color=GREEN, fill_opacity=1)
        masa2.move_to([2.8, 1.55, 0])  # Ubicación aproximada para m2 en el plano inclinado

        # Crear etiquetas para las masas
        label_m1 = Tex("m1").next_to(masa1, UP)
        label_m2 = Tex("m2").next_to(masa2, UP)

        # Crear ángulos
        angulo_theta = MathTex(r"\theta").move_to([-3.5, 0.25, 0])
        angulo_gamma = MathTex(r"\gamma").move_to([3.75, 1.9, 0])

        # Animar elementos
        self.play(Create(plano))
        self.play(Create(masa1), Create(masa2))
        self.play(Write(label_m1), Write(label_m2))
        self.play(Write(angulo_theta), Write(angulo_gamma))

        # Mantener la escena por unos segundos
        self.wait(2)
