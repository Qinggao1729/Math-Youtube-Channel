from manimlib.imports import *

class mainAnimation(Scene):
    def construct(self):
        # print(ORIGIN)
        ORIGIN=0.8*DOWN
        BUFFER=1.2
        # PURE_RED= "#FF0000"
        self.wait()

        line_10=self.line_seg(10)
        line_10.shift(ORIGIN, UP*2*BUFFER)
        self.play(ShowCreation(line_10))

        line_7 = self.line_seg(7)
        line_7.shift(ORIGIN, UP*BUFFER).align_to(line_10, LEFT)
        line_7.set_color(BLUE)
        self.play(ShowCreation(line_7))
        self.wait()

        # title
        left_para = TexMobject("gcd(")
        comma = TexMobject(",")
        right_para = TexMobject(")")
        a=self.line_seg(1)
        b=self.line_seg(1).set_color(BLUE)
        title=VGroup(left_para, a, comma, b, right_para)
        for i in range(1, 5):
            title[i].next_to(title[i-1])
        title.next_to(TOP, DOWN, buff=0.75)
        self.play(FadeIn(title))
        self.wait(2)

        line_7_copy=line_7.copy()
        line_7_copy.align_to(line_10, UP)
        self.play(TransformFromCopy(line_7, line_7_copy))
        self.wait()

        line_3= self.line_seg(3)
        self.next_to_line_seg(line_7_copy, line_3)
        line_3.set_color(PINK)
        self.play(FadeIn(line_3))
        self.wait()

        line_7_copy.generate_target()
        line_7_copy.target.shift(DOWN*2*BUFFER)
        line_7_copy_transform=MoveToTarget(line_7_copy)
        line_3.generate_target()
        line_3.target.shift(DOWN * 2 * BUFFER)
        line_3_transform = MoveToTarget(line_3)
        self.play(line_7_copy_transform, line_3_transform)
        self.wait(2)

        line_3_copy_1=line_3.copy()
        line_3_copy_2=line_3.copy()
        line_3_copy_1.align_to(line_7_copy, LEFT)
        self.next_to_line_seg(line_3_copy_1, line_3_copy_2)
        self.play(TransformFromCopy(line_3, line_3_copy_1))
        self.play(TransformFromCopy(line_3, line_3_copy_2))
        self.wait()

        line_1=self.line_seg(1)
        self.next_to_line_seg(line_3_copy_2, line_1)
        line_1.set_color(ORANGE)
        self.play(FadeIn(line_1))
        self.wait()

        vg_3_3_1=VGroup(line_3_copy_1, line_3_copy_2, line_1)
        self.play(vg_3_3_1.shift, DOWN*BUFFER)
        self.wait()

        vg_1_1_1=self.divide(line_3_copy_1, line_1)
        [self.play(TransformFromCopy(line_1, l)) for l in vg_1_1_1]
        self.wait()
        self.play(vg_1_1_1.shift, DOWN * BUFFER)
        self.wait()

        # shift title to the left and write down the result and the equal sign
        equal_sign=TexMobject("=")
        gcd=self.line_seg(1).set_color(ORANGE)
        answer=VGroup(equal_sign, gcd)
        gcd.next_to(equal_sign)
        answer.next_to(title)
        old_title=title.copy()
        all_title=VGroup(title, answer)
        all_title.next_to(TOP, DOWN, buff=0.75)
        self.play(TransformFromCopy(old_title, title))
        self.play(FadeIn(answer))
        self.wait(7.5)

        dividends_in_order = VGroup(line_3_copy_1, line_3_copy_2, line_7_copy, line_7,
                                    line_3, line_10)
        divided = [self.divide(x, line_1) for x in dividends_in_order]
        [self.play(FadeIn(d), runtime=1.5) for d in divided[:4]]
        self.wait(2)
        [self.play(FadeIn(d), runtime=1.5) for d in divided[4:]]
        self.wait(2)
        self.play(*[FadeOut(d) for d in divided])
        self.wait(2)

        half=self.line_seg(0.5).set_color(YELLOW)
        half.next_to(line_1,DOWN, buff=0, aligned_edge=LEFT)
        self.play(FadeIn(half))

        dividends_in_order.add_to_back(vg_1_1_1[2])
        dividends_in_order.add_to_back(vg_1_1_1[1])
        dividends_in_order.add_to_back(vg_1_1_1[0])
        dividends_in_order.add_to_back(line_1)

        divided=[self.divide(x, half) for x in dividends_in_order]
        [self.play(TransformFromCopy(half, s)) for s in divided[0]]
        [self.play(FadeIn(d)) for d in divided[1:8]]
        self.wait(1)
        [self.play(FadeIn(d)) for d in divided[8:]]
        self.wait(1)
        self.play(*[FadeOut(d) for d in divided])
        self.play(FadeOut(half))
        self.wait(2)

        # the greater than case: red line for error
        greater = self.line_seg(1.5).set_color(YELLOW)
        greater.next_to(line_1, DOWN, buff=0, aligned_edge=LEFT)
        self.play(FadeIn(greater))
        self.play(greater.align_to, line_1, UP)
        self.wait()
        self.play(greater.set_color, PURE_RED)
        self.wait(2)
        greater_copy=greater.copy()
        greater_new=self.line_seg(5).set_color(PURE_RED).align_to(greater, LEFT+UP)
        self.play(ReplacementTransform(greater, greater_new))
        self.wait(2)
        self.play(ReplacementTransform(greater_new, greater_copy))
        self.wait(2)
        self.play(FadeOut(greater_copy))
        self.wait(2)

    def line_seg(self, length):
        # TODO: maybe write it in the library
        line = Line()
        line.set_length(length)
        from_dot=Dot(line.get_start())
        to_dot=Dot(line.get_end())
        vg=VGroup(from_dot, line, to_dot) # notice the order here!
        return vg

    def next_to_line_seg(self, left, right):
        right.next_to(left[1], direction=RIGHT, buff=0, submobject_to_align=right[1])

    def divide(self, dividend, divisor):
        total=int(dividend[1].get_length()//divisor[1].get_length())
        print(total)
        partitions=VGroup()

        for i in range(total):
            partitions.add(divisor.copy())
        partitions[0].align_to(dividend, LEFT+UP)
        for i in range(1, total):
            self.next_to_line_seg(partitions[i-1], partitions[i])
        return partitions
