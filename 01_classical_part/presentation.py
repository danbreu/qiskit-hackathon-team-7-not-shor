import sys
from manim import *
from manim_fontawesome import *
from manim_presentation import Slide
import math
import math as m

def find_r(k,N,q=1, i=1):
    a=k*q % N

    if(a==1):
        return i

    return find_r(k,N,a,i+1)

def algo(k,N):
    a=math.gcd(k,N)

    if a!=1:
        return (a)

    if N % k == 0:
        return None

    r = find_r(k,N)
    if (k == 11 ):
        print(r)

    if r % 2 == 1:
        return None

    a = k**(r//2) + 1
    if a % N == 0:
        return None

    return (math.gcd(N,a), math.gcd(N,a-2))



def is_prime(n):
    if(n in [2,3]):
        return True

    return all([n%x != 0 for x in range(2,math.ceil(math.sqrt(n)+1))])


class Title(Slide):
    sys.setrecursionlimit(100000)

    def start_slide(self):
            text0 = Text("Shor's Algorithm", font="Roboto").set_color(RED).scale(2)
            text1 = Text("Team Not Shor", font="Roboto").scale(0.75).to_edge(DOWN)
            self.play(Write(text0))
            self.play(Write(text1))
            self.pause()
            self.clear()

    def rsa_slide(self):
            t = Text("What does Shor's Algorithm do exactly?", font="Roboto").set_color(WHITE).scale(1).to_edge(UP)
            self.add(t)

            text0 = Text("Shor's Algorithm is an algorithm for", font="Roboto").set_color(WHITE).scale(1).set_y(0.5)
            self.play(Write(text0))
            text1 = Text("factoring integers", font="Roboto").set_color(BLUE).scale(1).set_y(-0.5)
            self.play(Write(text1))

            self.pause()
            self.clear()

            # text0 = Text("RSA", font="Roboto").set_color(WHITE).scale(1).to_edge(UP)
            # self.add(text0)

            # alice_bob = [
            #     Write(solid.person.set_color(WHITE).scale(0.8).set_x(-3)),
            #     Write(Text("Alice").scale(0.8).set_x(-3).set_y(-1.2)),
            #     Write(solid.person.set_color(WHITE).scale(0.8).set_x(3)),
            #     Write(Text("Bob").scale(0.8).set_x(3).set_y(-1.2)),
            # ]

            # self.play(*alice_bob)

            # self.pause()
            # self.clear()

            text0 = Text("RSA", font="Roboto").set_color(WHITE).scale(1).to_edge(UP)
            self.add(text0)

            private_key = [
                Write(solid.key.set_color(RED).scale(0.5).set_x(-3).set_y(0)),
                Write(Text("Private Key").scale(0.5).set_color(RED).set_x(-3).set_y(-1.5)),
                Write(MathTex("= (N, d)").scale(0.7).set_x(-1.5).set_y(0)),

                Write(solid.key.set_color(GREEN).scale(0.5).set_x(2.5).set_y(0)),
                Write(Text("Public Key").scale(0.5).set_color(GREEN).set_x(2.5).set_y(-1.5)),
                Write(MathTex("= (N, e)").scale(0.7).set_x(4).set_y(0)),
            ]
            self.play(*private_key)

            annotation = [
                GrowArrow(Arrow(np.array([-1, -0.4, 0.1]), np.array([0.25, -1.8, 0.1]), buff=0)),
                Write(Text("derived from").scale(0.2).set_x(-1).set_y(-1.5)),
                Write(MathTex("N = p * q").set_color(BLUE).scale(0.75).to_edge(DOWN).set_y(-2)),
            ]
            self.pause()
            self.play(*annotation)

            self.pause()
            self.play(Write(Text("N is part of both the public and private key").set_color(BLUE).scale(0.75).to_edge(DOWN)))

            self.pause()
            self.clear()

    def complexity_slide(self):
        caption = Text("Runtime Complexity", font = "Roboto").to_edge(UP)
        axes = Axes(
            x_range = [0.001, 12.0, 1],
            y_range = [0.3, 9.0, 1],
            axis_config={"color": WHITE},
            x_axis_config = {
                # "numbers_to_include": np.arange(0, 12.01, 2),
                "numbers_with_elongated_ticks": np.arange(0, 3.01, 2)
            },
            y_axis_config = {
                "numbers_with_elongated_ticks": None
            },
            tips = False
        )
        axes_labels = axes.get_axis_labels()

        exp_curve = axes.plot(lambda x: 1.25 ** x + 0.1, color = RED)
        log_curve = axes.plot(lambda x: m.log(x + 1) + 0.3, color = BLUE)

        exp_curve_label = axes.get_graph_label(exp_curve, "Classical Computer").set_y(1).set_x(4.5)
        log_curve_label = axes.get_graph_label(log_curve, "Quantum Computer").set_y(-1).set_x(4.5)

        self.add_foreground_mobject(caption)
        self.play(Create(caption), run_time = 1)
        self.play(Create(axes), run_time = 1)
        self.play(Create(exp_curve), run_time = 3)
        self.play(Create(exp_curve_label), run_time = 1)
        self.play(Create(log_curve), run_time = 5)
        self.play(Create(log_curve_label), run_time = 1)
        self.wait(1)
        self.pause()
        self.clear()

    def primes_slide(self):
            number = 127 * 59
            numbers = [*filter(is_prime, range(2,128))]
            prime_fac = [127, 59]
            elig = [*filter(lambda x: algo(x,number) is not None, numbers)]
            rows = 4
            columns = len(numbers) / rows
            spacing = 1

            prim_fac_obj = []
            prim_fac_circle_obj = []
            elig_obj = []
            elig_circle_obj = []
            i = 0

            t = Text(f"Finding prime factors of N={number}", font="Roboto").set_color(WHITE).scale(1).to_edge(UP)
            self.add(t)
            for n in numbers:
                x = (i % columns - (columns-1)/2)*spacing
                y = (i // columns - (rows-1)/2)*spacing - 1
                number = Integer(n).set_x(x).set_y(y).set_color(WHITE).scale(0.8)
                if n in prime_fac:
                    prim_fac_obj.append(number)
                    prim_fac_circle_obj.append(Circle(radius=0.3, color=YELLOW, fill_opacity=0).move_to(x*RIGHT+y*UP))
                if n in elig:
                    elig_obj.append(number)
                    elig_circle_obj.append(Circle(radius=0.3, color=BLUE, fill_opacity=0).move_to(x*RIGHT+y*UP))

                self.add(number)

                i += 1

            self.pause()


            i  =0
            animations = []
            for n in prim_fac_obj:
                animations.append(FadeToColor(n, color=YELLOW))
                animations.append(FadeIn(prim_fac_circle_obj[i]))
                i += 1

            self.play(*animations)

            self.pause()

            i = 0
            animations = []
            for n in elig_obj:
                animations.append(FadeToColor(n, color=BLUE))
                animations.append(FadeIn(elig_circle_obj[i]))

                i += 1

            self.play(*animations)
            self.pause()
            self.clear()

    def explanation_slide(self):
        title = Tex("The algorithm to factorize $N$").set_color(WHITE).scale(1).to_edge(UP)
        tex = Tex("\\begin{enumerate}\\item Pick a random number $a < N$ \\item Calculate $K = gcd(a,N)$ \\item If $K \\neq 1$ we find a factor, algorithm finishes\\\\ $\\Rightarrow$ whilst possible this is extremely unlikely \\item Use Quantum Period finding on $a$ to get $r$ \\\\  $\\hspace{10pt}a^r \\equiv 1 \\mod N$\\item If $r$ is odd or if $a^{\\frac{r}{2}} \equiv -1\\mod N$, go back to step $1$.  \\item Otherwise both $gcd(a^{\\frac{r}{2}}+1,N)$ and $gcd(a^{\\frac{r}{2}}+1,N)$ are factors of N.\\\\ $\\Rightarrow$ We are done.\\end{enumerate}")
        self.add(title)
        self.add(tex.arrange(RIGHT, center=False, allign_edge=LEFT).scale(0.5))

        a = Integer(11)
        aCircle = Circle(radius=0.2, color=BLUE, fill_opacity=0)
        a.scale(0.75)
        a.set_x(-4.5)
        a.set_y(1.75) #0.5 line distance
        aCircle.surround(a)
        self.play(FadeToColor(a,color=BLUE), FadeIn(aCircle))
        self.pause()
        # gcd 7543 11 = 1
        k = Integer(1)
        kCircle = Circle(radius=0.2, color=BLUE, fill_opacity=0)
        k.scale(0.75)
        k.set_x(-4.5)
        k.set_y(1.25)
        kCircle.surround(k)
        self.play(FadeToColor(k,color=BLUE), FadeIn(kCircle))
        self.pause()

        # r = 2654
        r = Integer(2654)
        rCircle = Circle(radius=0.2, color=BLUE, fill_opacity=0)
        r.scale(0.75)
        r.set_x(-4.5)
        r.set_y(-0.2)
        rCircle.surround(r)
        self.play(FadeToColor(r,color=BLUE), FadeIn(rCircle))
        self.pause()
        # 59, 127
        tp = MathTex("59 \\cdot 127 = 7493")
        tp.scale(0.75)
        tp.set_y(-3)
        self.play(FadeToColor(tp,color=RED))
        self.pause()

    def construct(self):
        text0 = Text("_ ")
        self.play(Write(text0))
        self.pause()
        self.clear()

        self.start_slide()
        self.rsa_slide()
        self.complexity_slide()
        self.primes_slide()
        self.explanation_slide()


