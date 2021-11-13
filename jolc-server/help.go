/*----HEADER----*/
package main;

import (
        "fmt"
);

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, t65, t66, t67, t68, t69, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t80, t81, t82, t83, t84, t85, t86, t87, t88, t89, t90, t91, t92, t93, t94, t95, t96, t97, t98, t99, t100, t101, t102, t103, t104, 
t105, t106, t107, t108, t109, t110, t111, t112, t113, t114, t115, t116, t117, t118, t119, t120, t121, t122, t123, t124, t125, t126, t127, t128, t129, t130, t131, t132, t133, t134, t135, t136, t137, t138, t139, t140, t141, t142, t143, t144, t145, t146, t147, t148 float64;
var P, H float64;
var stack [29101998]float64;
var heap [29101998]float64;

/*-----NATIVES-----*/
func trunc(){
        t19 = P+1;
        t21 = stack[int(t19)];
        t20 = 0;
        L9:
        t20 = t20+1;
        if t20 > t21 {goto L8;}
        goto L9;
        L8:
        t20 = t20-1;
        stack[int(P)] = t20;
        return;
}
func native_length(){
        t130 = P+1;
        t130 = stack[int(t130)];
        t130 = heap[int(t130)];
        goto L47;
        L47:
        stack[int(P)] = t130;
        return;
}

/*-----FUNCS-----*/
func quicksort(){
        t1 = P+2;
        t0 = stack[int(t1)];

        t2 = P+4;
        stack[int(t2)] = t0;

        t4 = P+3;
        t3 = stack[int(t4)];

        t5 = P+5;
        stack[int(t5)] = t3;

        /***** BEGIN IF *****/
        t7 = P+4;
        t6 = stack[int(t7)];

        t9 = P+3;
        t8 = stack[int(t9)];

        if t6 >= t8 {goto L1;}
        goto L2;

        L1:
        stack[int(P)] = 0;
        goto L0;
        L2:
        /***** END IF *****/
        t14 = P+4;
        t13 = stack[int(t14)];

        t16 = P+5;
        t15 = stack[int(t16)];

        t17 = t13+t15;
        if 2 != 0 {goto L6;}
        fmt.Printf("%c", int(77));
        fmt.Printf("%c", int(97));
        fmt.Printf("%c", int(116));
        fmt.Printf("%c", int(104));
        fmt.Printf("%c", int(69));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(10));
        t18 = 0;
        goto L7;
        L6:
        t18 = t17/2;
        L7:
        t22 = P+6;
        t22 = t22+1;
        stack[int(t22)] = t18;
        P = P + 6;
        trunc();
        t23 = stack[int(P)];
        P = P - 6;
        t11 = t23;
        t12 = stack[int(1)];
        t10 = heap[int(t12)];
        if t11 < 1 {goto L3;}
        if t11 > t10 {goto L3;}
        goto L4;
        L3:
        fmt.Printf("%c", int(66));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(117));
        fmt.Printf("%c", int(110));
        fmt.Printf("%c", int(100));
        fmt.Printf("%c", int(115));
        fmt.Printf("%c", int(69));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(10));
        t10 = 0;
        goto L5;
        L4:
        t12 = t12+t11;
        t10 = heap[int(t12)];
        L5:
        t24 = P+6;
        stack[int(t24)] = t10;

        t26 = P+6;
        t25 = stack[int(t26)];

        fmt.Printf("%d", int(t25));
        fmt.Printf("%c", int(10));
        /***** BEGIN WHILE *****/
        L10:
        t28 = P+4;
        t27 = stack[int(t28)];

        t30 = P+5;
        t29 = stack[int(t30)];

        if t27 < t29 {goto L11;}
        goto L12;

        L11:
        /***** BEGIN WHILE *****/
        L13:
        t32 = P+4;
        t31 = stack[int(t32)];

        t34 = P+5;
        t33 = stack[int(t34)];

        if t31 < t33 {goto L16;}
        goto L15;

        L16:
        t39 = P+4;
        t38 = stack[int(t39)];

        t36 = t38;
        t37 = stack[int(1)];
        t35 = heap[int(t37)];
        if t36 < 1 {goto L17;}
        if t36 > t35 {goto L17;}
        goto L18;
        L17:
        fmt.Printf("%c", int(66));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(117));
        fmt.Printf("%c", int(110));
        fmt.Printf("%c", int(100));
        fmt.Printf("%c", int(115));
        fmt.Printf("%c", int(69));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(10));
        t35 = 0;
        goto L19;
        L18:
        t37 = t37+t36;
        t35 = heap[int(t37)];
        L19:
        t41 = P+6;
        t40 = stack[int(t41)];

        if t35 < t40 {goto L14;}
        goto L15;


        L14:
        t43 = P+4;
        t42 = stack[int(t43)];

        t44 = t42+1;
        stack[int(4)] = t44;

        goto L13;
        L15:
        /***** END WHILE *****/
        /***** BEGIN WHILE *****/
        L20:
        t46 = P+4;
        t45 = stack[int(t46)];

        t48 = P+5;
        t47 = stack[int(t48)];

        if t45 < t47 {goto L23;}
        goto L22;

        L23:
        t53 = P+5;
        t52 = stack[int(t53)];

        t50 = t52;
        t51 = stack[int(1)];
        t49 = heap[int(t51)];
        if t50 < 1 {goto L24;}
        if t50 > t49 {goto L24;}
        goto L25;
        L24:
        fmt.Printf("%c", int(66));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(117));
        fmt.Printf("%c", int(110));
        fmt.Printf("%c", int(100));
        fmt.Printf("%c", int(115));
        fmt.Printf("%c", int(69));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(10));
        t49 = 0;
        goto L26;
        L25:
        t51 = t51+t50;
        t49 = heap[int(t51)];
        L26:
        t55 = P+6;
        t54 = stack[int(t55)];

        if t49 > t54 {goto L21;}
        goto L22;


        L21:
        t57 = P+5;
        t56 = stack[int(t57)];

        t58 = t56-1;
        stack[int(5)] = t58;

        goto L20;
        L22:
        /***** END WHILE *****/
        /***** BEGIN IF *****/
        t60 = P+4;
        t59 = stack[int(t60)];

        t62 = P+5;
        t61 = stack[int(t62)];

        if t59 < t61 {goto L27;}
        goto L28;

        L27:
        t67 = P+4;
        t66 = stack[int(t67)];

        t64 = t66;
        t65 = stack[int(1)];
        t63 = heap[int(t65)];
        if t64 < 1 {goto L29;}
        if t64 > t63 {goto L29;}
        goto L30;
        L29:
        fmt.Printf("%c", int(66));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(117));
        fmt.Printf("%c", int(110));
        fmt.Printf("%c", int(100));
        fmt.Printf("%c", int(115));
        fmt.Printf("%c", int(69));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(10));
        t63 = 0;
        goto L31;
        L30:
        t65 = t65+t64;
        t63 = heap[int(t65)];
        L31:
        t68 = P+7;
        stack[int(t68)] = t63;

        t69 = P+1;
        t69 = stack[int(t69)];
        /***** BEGIN ACCESS ARRAY *****/
        t74 = P+4;
        t73 = stack[int(t74)];

        t71 = t73;
        t72 = t69;
        t70 = heap[int(t72)];
        if t71 < 1 {goto L32;}
        if t71 > t70 {goto L32;}
        goto L33;
        L32:
        fmt.Printf("%c", int(66));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(117));
        fmt.Printf("%c", int(110));
        fmt.Printf("%c", int(100));
        fmt.Printf("%c", int(115));
        fmt.Printf("%c", int(69));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(10));
        t70 = 0;
        goto L34;
        L33:
        t70 = t72+t71;
        t79 = P+5;
        t78 = stack[int(t79)];

        t76 = t78;
        t77 = stack[int(1)];
        t75 = heap[int(t77)];
        if t76 < 1 {goto L35;}
        if t76 > t75 {goto L35;}
        goto L36;
        L35:
        fmt.Printf("%c", int(66));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(117));
        fmt.Printf("%c", int(110));
        fmt.Printf("%c", int(100));
        fmt.Printf("%c", int(115));
        fmt.Printf("%c", int(69));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(10));
        t75 = 0;
        goto L37;
        L36:
        t77 = t77+t76;
        t75 = heap[int(t77)];
        L37:
        heap[int(t70)] = t75;
        L34:
        /***** END ACCESS ARRAY *****/
        t80 = P+1;
        t80 = stack[int(t80)];
        /***** BEGIN ACCESS ARRAY *****/
        t85 = P+5;
        t84 = stack[int(t85)];

        t82 = t84;
        t83 = t80;
        t81 = heap[int(t83)];
        if t82 < 1 {goto L38;}
        if t82 > t81 {goto L38;}
        goto L39;
        L38:
        fmt.Printf("%c", int(66));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(117));
        fmt.Printf("%c", int(110));
        fmt.Printf("%c", int(100));
        fmt.Printf("%c", int(115));
        fmt.Printf("%c", int(69));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(10));
        t81 = 0;
        goto L40;
        L39:
        t81 = t83+t82;
        t87 = P+7;
        t86 = stack[int(t87)];

        heap[int(t81)] = t86;
        L40:
        /***** END ACCESS ARRAY *****/
        L28:
        /***** END IF *****/
        goto L10;
        L12:
        /***** END WHILE *****/
        /***** BEGIN IF *****/
        t89 = P+5;
        t88 = stack[int(t89)];

        t91 = P+4;
        t90 = stack[int(t91)];

        if t88 < t90 {goto L41;}
        goto L42;

        L41:
        t93 = P+5;
        t92 = stack[int(t93)];

        t94 = P+7;
        stack[int(t94)] = t92;

        t96 = P+4;
        t95 = stack[int(t96)];

        stack[int(5)] = t95;

        t98 = P+7;
        t97 = stack[int(t98)];

        stack[int(4)] = t97;

        L42:
        /***** END IF *****/

        /***** BEGIN SAVING TEMPS *****/
        t99 = P+8;
        stack[int(t99)] = t0;
        t99 = t99+1;
        stack[int(t99)] = t2;
        t99 = t99+1;
        stack[int(t99)] = t3;
        t99 = t99+1;
        stack[int(t99)] = t5;
        t99 = t99+1;
        stack[int(t99)] = t18;
        t99 = t99+1;
        stack[int(t99)] = t24;
        t99 = t99+1;
        stack[int(t99)] = t44;
        t99 = t99+1;
        stack[int(t99)] = t58;
        t99 = t99+1;
        stack[int(t99)] = t68;
        t99 = t99+1;
        stack[int(t99)] = t92;
        t99 = t99+1;
        stack[int(t99)] = t94;
        t99 = t99+1;
        stack[int(t99)] = t95;
        t99 = t99+1;
        stack[int(t99)] = t97;
        /***** END SAVING TEMPS *****/

        t101 = P+1;
        t100 = stack[int(t101)];

        t103 = P+2;
        t102 = stack[int(t103)];

        t105 = P+4;
        t104 = stack[int(t105)];

        t106 = P+22;
        stack[int(t106)] = t100;
        t106 = t106+1;
        stack[int(t106)] = t102;
        t106 = t106+1;
        stack[int(t106)] = t104;
        t106 = t106+1;
        P = P + 21;
        quicksort();
        t106 = stack[int(P)];
        P = P - 21;

        /***** BEGIN RECOVERING TEMPS *****/
        t107 = P+8;
        t0 = stack[int(t107)];
        t107 = t107+1;
        t2 = stack[int(t107)];
        t107 = t107+1;
        t3 = stack[int(t107)];
        t107 = t107+1;
        t5 = stack[int(t107)];
        t107 = t107+1;
        t18 = stack[int(t107)];
        t107 = t107+1;
        t24 = stack[int(t107)];
        t107 = t107+1;
        t44 = stack[int(t107)];
        t107 = t107+1;
        t58 = stack[int(t107)];
        t107 = t107+1;
        t68 = stack[int(t107)];
        t107 = t107+1;
        t92 = stack[int(t107)];
        t107 = t107+1;
        t94 = stack[int(t107)];
        t107 = t107+1;
        t95 = stack[int(t107)];
        t107 = t107+1;
        t97 = stack[int(t107)];
        /***** END RECOVERING TEMPS *****/

        t108 = P+8;
        stack[int(t108)] = 0;

        /***** BEGIN IF *****/
        t110 = P+4;
        t109 = stack[int(t110)];

        t112 = P+2;
        t111 = stack[int(t112)];

        if t109 == t111 {goto L43;}
        goto L44;

        L43:
        t114 = P+4;
        t113 = stack[int(t114)];

        t115 = t113+1;
        stack[int(8)] = t115;

        goto L45;
        L44:
        t117 = P+4;
        t116 = stack[int(t117)];

        stack[int(8)] = t116;

        L45:
        /***** END IF *****/

        /***** BEGIN SAVING TEMPS *****/
        t118 = P+9;
        stack[int(t118)] = t0;
        t118 = t118+1;
        stack[int(t118)] = t2;
        t118 = t118+1;
        stack[int(t118)] = t3;
        t118 = t118+1;
        stack[int(t118)] = t5;
        t118 = t118+1;
        stack[int(t118)] = t18;
        t118 = t118+1;
        stack[int(t118)] = t24;
        t118 = t118+1;
        stack[int(t118)] = t44;
        t118 = t118+1;
        stack[int(t118)] = t58;
        t118 = t118+1;
        stack[int(t118)] = t68;
        t118 = t118+1;
        stack[int(t118)] = t92;
        t118 = t118+1;
        stack[int(t118)] = t94;
        t118 = t118+1;
        stack[int(t118)] = t95;
        t118 = t118+1;
        stack[int(t118)] = t97;
        t118 = t118+1;
        stack[int(t118)] = t106;
        t118 = t118+1;
        stack[int(t118)] = t108;
        t118 = t118+1;
        stack[int(t118)] = t115;
        t118 = t118+1;
        stack[int(t118)] = t116;
        /***** END SAVING TEMPS *****/

        t120 = P+1;
        t119 = stack[int(t120)];

        t122 = P+8;
        t121 = stack[int(t122)];

        t124 = P+3;
        t123 = stack[int(t124)];

        t125 = P+27;
        stack[int(t125)] = t119;
        t125 = t125+1;
        stack[int(t125)] = t121;
        t125 = t125+1;
        stack[int(t125)] = t123;
        t125 = t125+1;
        P = P + 26;
        quicksort();
        t125 = stack[int(P)];
        P = P - 26;

        /***** BEGIN RECOVERING TEMPS *****/
        t126 = P+9;
        t0 = stack[int(t126)];
        t126 = t126+1;
        t2 = stack[int(t126)];
        t126 = t126+1;
        t3 = stack[int(t126)];
        t126 = t126+1;
        t5 = stack[int(t126)];
        t126 = t126+1;
        t18 = stack[int(t126)];
        t126 = t126+1;
        t24 = stack[int(t126)];
        t126 = t126+1;
        t44 = stack[int(t126)];
        t126 = t126+1;
        t58 = stack[int(t126)];
        t126 = t126+1;
        t68 = stack[int(t126)];
        t126 = t126+1;
        t92 = stack[int(t126)];
        t126 = t126+1;
        t94 = stack[int(t126)];
        t126 = t126+1;
        t95 = stack[int(t126)];
        t126 = t126+1;
        t97 = stack[int(t126)];
        t126 = t126+1;
        t106 = stack[int(t126)];
        t126 = t126+1;
        t108 = stack[int(t126)];
        t126 = t126+1;
        t115 = stack[int(t126)];
        t126 = t126+1;
        t116 = stack[int(t126)];
        /***** END RECOVERING TEMPS *****/

        goto L0;
        L0:
        return;
}
func printArray(){
        /***** BEGIN FOR *****/
        t129 = P+1;
        t128 = stack[int(t129)];

        t131 = P+2;
        t131 = t131+1;
        stack[int(t131)] = t128;
        P = P + 2;
        native_length();
        t132 = stack[int(P)];
        P = P - 2;
        t127 = H;
        heap[int(H)] = 1;
        H = H + 1;
        heap[int(H)] = t132;
        H = H + 1;

        t134 = heap[int(t127)];
        t127 = t127+1;
        t135 = heap[int(t127)];
        L48:
        t133 = P+2;
        stack[int(t133)] = t134;
        if t134 > t135 {goto L49;}
        t134 = t134+1;
        t140 = P+2;
        t139 = stack[int(t140)];

        t137 = t139;
        t138 = stack[int(1)];
        t136 = heap[int(t138)];
        if t137 < 1 {goto L50;}
        if t137 > t136 {goto L50;}
        goto L51;
        L50:
        fmt.Printf("%c", int(66));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(117));
        fmt.Printf("%c", int(110));
        fmt.Printf("%c", int(100));
        fmt.Printf("%c", int(115));
        fmt.Printf("%c", int(69));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(111));
        fmt.Printf("%c", int(114));
        fmt.Printf("%c", int(10));
        t136 = 0;
        goto L52;
        L51:
        t138 = t138+t137;
        t136 = heap[int(t138)];
        L52:
        fmt.Printf("%d", int(t136));
        fmt.Printf("%c", int(10));
        goto L48;
        L49:

        /***** END FOR *****/
        goto L46;
        L46:
        return;
}

func main(){
        /***** BEGIN ARRAY *****/
        t141 = H;
        t142 = t141;
        H = H+7;
        heap[int(t142)] = 6;
        t142 = t142+1;
        heap[int(t142)] = 15;
        t142 = t142+1;
        heap[int(t142)] = 21;
        t142 = t142+1;
        heap[int(t142)] = 10;
        t142 = t142+1;
        heap[int(t142)] = 25;
        t142 = t142+1;
        heap[int(t142)] = 12;
        t142 = t142+1;
        heap[int(t142)] = 45;
        /***** END ARRAY *****/
        stack[int(0)] = t141;

        t143 = stack[int(0)];

        t144 = P+2;
        stack[int(t144)] = 0; //t46
        t144 = t144+1;
        stack[int(t144)] = 1;
        t144 = t144+1;
        stack[int(t144)] = 6;
        t144 = t144+1;
        P = P + 1;
        quicksort();
        t144 = stack[int(P)];
        P = P - 1;

        /***** BEGIN SAVING TEMPS *****/
        t145 = P+1;
        stack[int(t145)] = t144;
        /***** END SAVING TEMPS *****/

        t146 = stack[int(0)];

        t147 = P+3;
        stack[int(t147)] = 0; //t46
        P = P + 2;
        printArray();
        t147 = stack[int(P)];
        P = P - 2;

        /***** BEGIN RECOVERING TEMPS *****/
        t148 = P+1;
        t144 = stack[int(t148)];
        /***** END RECOVERING TEMPS *****/



}