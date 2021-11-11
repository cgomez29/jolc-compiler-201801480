/*----HEADER----*/
package main;

import (
        "fmt"
);

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, t65, t66, t67, t68, t69, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t80, t81, t82, t83, t84, t85, t86, t87, t88, t89, t90, t91 float64;
var P, H float64;
var stack [29101998]float64;
var heap [29101998]float64;

/*-----NATIVES-----*/
func native_length(){
        t28 = P+1;
        t28 = stack[int(t28)];
        t28 = heap[int(t28)];
        goto L14;
        L14:
        stack[int(P)] = t28;
        return;
}
func native_power(){
        t68 = P+1;
        t69 = stack[int(t68)];
        t68 = t68+1;
        t70 = stack[int(t68)];
        t68 = t69;
        if t70 == 0 {goto L29;}
        L27:
        if t70 <= 1 {goto L28;}
        t69 = t69*t68;
        t70 = t70-1;
        goto L27;
        L29:
        t69 = 1;
        L28:
        stack[int(P)] = t69;
        return;
}
func native_print_string(){
        t78 = P+1;
        t79 = stack[int(t78)];
        L31:
        t80 = heap[int(t79)];
        if t80 == -1 {goto L30;}
        fmt.Printf("%c", int(t80));
        t79 = t79+1;
        goto L31;
        L30:
        return;
}

/*-----FUNCS-----*/
func swap(){
        t4 = P+1;
        t3 = stack[int(t4)];

        t1 = t3;
        t2 = stack[int(3)];
        t0 = heap[int(t2)];
        if t1 < 1 {goto L1;}
        if t1 > t0 {goto L1;}
        goto L2;
        L1:
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
        t0 = 0;
        goto L3;
        L2:
        t2 = t2+t1;
        t0 = heap[int(t2)];
        L3:
        t5 = P+4;
        stack[int(t5)] = t0;

        t6 = P+3;
        t6 = stack[int(t6)];
        /***** BEGIN ACCESS ARRAY *****/
        t11 = P+1;
        t10 = stack[int(t11)];

        t8 = t10;
        t9 = t6;
        t7 = heap[int(t9)];
        if t8 < 1 {goto L4;}
        if t8 > t7 {goto L4;}
        goto L5;
        L4:
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
        t7 = 0;
        goto L6;
        L5:
        t7 = t9+t8;
        t16 = P+2;
        t15 = stack[int(t16)];

        t13 = t15;
        t14 = stack[int(3)];
        t12 = heap[int(t14)];
        if t13 < 1 {goto L7;}
        if t13 > t12 {goto L7;}
        goto L8;
        L7:
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
        t12 = 0;
        goto L9;
        L8:
        t14 = t14+t13;
        t12 = heap[int(t14)];
        L9:
        heap[int(t7)] = t12;
        L6:
        /***** END ACCESS ARRAY *****/
        t17 = P+3;
        t17 = stack[int(t17)];
        /***** BEGIN ACCESS ARRAY *****/
        t22 = P+2;
        t21 = stack[int(t22)];

        t19 = t21;
        t20 = t17;
        t18 = heap[int(t20)];
        if t19 < 1 {goto L10;}
        if t19 > t18 {goto L10;}
        goto L11;
        L10:
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
        t18 = 0;
        goto L12;
        L11:
        t18 = t20+t19;
        t24 = P+4;
        t23 = stack[int(t24)];

        heap[int(t18)] = t23;
        L12:
        /***** END ACCESS ARRAY *****/
        goto L0;
        L0:
        return;
}
func bubbleSort(){
        /***** BEGIN FOR *****/
        t27 = P+1;
        t26 = stack[int(t27)];

        t29 = P+2;
        t29 = t29+1;
        stack[int(t29)] = t26;
        P = P + 2;
        native_length();
        t30 = stack[int(P)];
        P = P - 2;
        t31 = t30-1;
        t25 = H;
        heap[int(H)] = 0;
        H = H + 1;
        heap[int(H)] = t31;
        H = H + 1;

        t33 = heap[int(t25)];
        t25 = t25+1;
        t34 = heap[int(t25)];
        L15:
        t32 = P+2;
        stack[int(t32)] = t33;
        if t33 > t34 {goto L16;}
        t33 = t33+1;
        /***** BEGIN FOR *****/
        t37 = P+1;
        t36 = stack[int(t37)];

        t38 = P+3;
        t38 = t38+1;
        stack[int(t38)] = t36;
        P = P + 3;
        native_length();
        t39 = stack[int(P)];
        P = P - 3;
        t40 = t39-1;
        t35 = H;
        heap[int(H)] = 1;
        H = H + 1;
        heap[int(H)] = t40;
        H = H + 1;

        t42 = heap[int(t35)];
        t35 = t35+1;
        t43 = heap[int(t35)];
        L17:
        t41 = P+3;
        stack[int(t41)] = t42;
        if t42 > t43 {goto L18;}
        t42 = t42+1;
        /***** BEGIN IF *****/
        t48 = P+3;
        t47 = stack[int(t48)];

        t45 = t47;
        t46 = stack[int(1)];
        t44 = heap[int(t46)];
        if t45 < 1 {goto L19;}
        if t45 > t44 {goto L19;}
        goto L20;
        L19:
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
        t44 = 0;
        goto L21;
        L20:
        t46 = t46+t45;
        t44 = heap[int(t46)];
        L21:
        t53 = P+3;
        t52 = stack[int(t53)];

        t54 = t52+1;
        t50 = t54;
        t51 = stack[int(1)];
        t49 = heap[int(t51)];
        if t50 < 1 {goto L22;}
        if t50 > t49 {goto L22;}
        goto L23;
        L22:
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
        goto L24;
        L23:
        t51 = t51+t50;
        t49 = heap[int(t51)];
        L24:
        if t44 > t49 {goto L25;}
        goto L26;

        L25:

        /***** BEGIN SAVING TEMPS *****/
        t55 = P+4;
        stack[int(t55)] = t26;
        t55 = t55+1;
        stack[int(t55)] = t36;
        /***** END SAVING TEMPS *****/

        t57 = P+3;
        t56 = stack[int(t57)];

        t59 = P+3;
        t58 = stack[int(t59)];

        t60 = t58+1;
        t62 = P+1;
        t61 = stack[int(t62)];

        t63 = P+7;
        stack[int(t63)] = t56;
        t63 = t63+1;
        stack[int(t63)] = t60;
        t63 = t63+1;
        stack[int(t63)] = t61;
        t63 = t63+1;
        P = P + 6;
        swap();
        t63 = stack[int(P)];
        P = P - 6;

        /***** BEGIN RECOVERING TEMPS *****/
        t64 = P+4;
        t26 = stack[int(t64)];
        t64 = t64+1;
        t36 = stack[int(t64)];
        /***** END RECOVERING TEMPS *****/

        L26:
        /***** END IF *****/
        goto L17;
        L18:

        /***** END FOR *****/
        goto L15;
        L16:

        /***** END FOR *****/
        goto L13;
        L13:
        return;
}

func main(){
        /***** BEGIN ARRAY *****/
        t65 = H;
        t66 = t65;
        H = H+17;
        heap[int(t66)] = 16;
        t66 = t66+1;
        heap[int(t66)] = 32;
        t66 = t66+1;
        t67 = 7*3;
        heap[int(t66)] = t67;
        t66 = t66+1;
        heap[int(t66)] = 7;
        t66 = t66+1;
        heap[int(t66)] = 89;
        t66 = t66+1;
        heap[int(t66)] = 56;
        t66 = t66+1;
        heap[int(t66)] = 909;
        t66 = t66+1;
        heap[int(t66)] = 109;
        t66 = t66+1;
        heap[int(t66)] = 2;
        t66 = t66+1;
        heap[int(t66)] = 9;
        t66 = t66+1;
        t71 = P+0;
        t71 = t71+1;
        stack[int(t71)] = 9874;
        t72 = t71+1;
        stack[int(t72)] = 0;
        P = P + 0;
        native_power();
        t73 = stack[int(P)];
        P = P - 0;
        heap[int(t66)] = t73;
        t66 = t66+1;
        heap[int(t66)] = 44;
        t66 = t66+1;
        heap[int(t66)] = 3;
        t66 = t66+1;
        t74 = 820*10;
        heap[int(t66)] = t74;
        t66 = t66+1;
        heap[int(t66)] = 11;
        t66 = t66+1;
        t75 = 8*0;
        t76 = t75+8;
        heap[int(t66)] = t76;
        t66 = t66+1;
        heap[int(t66)] = 10;
        /***** END ARRAY *****/
        stack[int(0)] = t65;

        t77 = H;
        heap[int(H)] = 66;
        H = H + 1;
        heap[int(H)] = 117;
        H = H + 1;
        heap[int(H)] = 98;
        H = H + 1;
        heap[int(H)] = 98;
        H = H + 1;
        heap[int(H)] = 108;
        H = H + 1;
        heap[int(H)] = 101;
        H = H + 1;
        heap[int(H)] = 83;
        H = H + 1;
        heap[int(H)] = 111;
        H = H + 1;
        heap[int(H)] = 114;
        H = H + 1;
        heap[int(H)] = 116;
        H = H + 1;
        heap[int(H)] = 32;
        H = H + 1;
        heap[int(H)] = 61;
        H = H + 1;
        heap[int(H)] = 62;
        H = H + 1;
        heap[int(H)] = 32;
        H = H + 1;
        heap[int(H)] = -1;
        H = H + 1;
        /***** BEGIN PRINT STRING *****/
        t81 = P+1;
        t81 = t81+1;
        stack[int(t81)] = t77;
        P = P + 1;
        native_print_string();
        t82 = stack[int(P)];
        P = P - 1;
        /***** END PRINT STRING *****/
        t83 = stack[int(0)];

        fmt.Printf("%f", t83);
        fmt.Printf("%c", int(10));

        /***** BEGIN SAVING TEMPS *****/
        t84 = P+1;
        stack[int(t84)] = t77;
        t84 = t84+1;
        stack[int(t84)] = t82;
        /***** END SAVING TEMPS *****/

        t85 = stack[int(0)];

        t86 = P+4;
        stack[int(t86)] = t85;
        P = P + 3;
        bubbleSort();
        t86 = stack[int(P)];
        P = P - 3;

        /***** BEGIN RECOVERING TEMPS *****/
        t87 = P+1;
        t77 = stack[int(t87)];
        t87 = t87+1;
        t82 = stack[int(t87)];
        /***** END RECOVERING TEMPS *****/

        t88 = H;
        heap[int(H)] = 66;
        H = H + 1;
        heap[int(H)] = 117;
        H = H + 1;
        heap[int(H)] = 98;
        H = H + 1;
        heap[int(H)] = 98;
        H = H + 1;
        heap[int(H)] = 108;
        H = H + 1;
        heap[int(H)] = 101;
        H = H + 1;
        heap[int(H)] = 83;
        H = H + 1;
        heap[int(H)] = 111;
        H = H + 1;
        heap[int(H)] = 114;
        H = H + 1;
        heap[int(H)] = 116;
        H = H + 1;
        heap[int(H)] = 32;
        H = H + 1;
        heap[int(H)] = 61;
        H = H + 1;
        heap[int(H)] = 62;
        H = H + 1;
        heap[int(H)] = 32;
        H = H + 1;
        heap[int(H)] = -1;
        H = H + 1;
        /***** BEGIN PRINT STRING *****/
        t89 = P+1;
        t89 = t89+1;
        stack[int(t89)] = t88;
        P = P + 1;
        native_print_string();
        t90 = stack[int(P)];
        P = P - 1;
        /***** END PRINT STRING *****/
        t91 = stack[int(0)];

        fmt.Printf("%f", t91);
        fmt.Printf("%c", int(10));


}