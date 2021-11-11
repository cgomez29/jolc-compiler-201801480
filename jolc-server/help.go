/*----HEADER----*/
package main;

import (
        "fmt"
);

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29 float64;
var P, H float64;
var stack [29101998]float64;
var heap [29101998]float64;

/*-----NATIVES-----*/
func native_length(){
        t3 = P+1;
        t3 = stack[int(t3)];
        t3 = heap[int(t3)];
        goto L1;
        L1:
        stack[int(P)] = t3;
        return;
}
func native_power(){
        t17 = P+1;
        t18 = stack[int(t17)];
        t17 = t17+1;
        t19 = stack[int(t17)];
        t17 = t18;
        if t19 == 0 {goto L9;}
        L7:
        if t19 <= 1 {goto L8;}
        t18 = t18*t17;
        t19 = t19-1;
        goto L7;
        L9:
        t18 = 1;
        L8:
        stack[int(P)] = t18;
        return;
}

/*-----FUNCS-----*/
func bubbleSort(){
        /***** BEGIN FOR *****/
        t2 = P+1;
        t1 = stack[int(t2)];

        t4 = P+2;
        t4 = t4+1;
        stack[int(t4)] = t1;
        P = P + 2;
        native_length();
        t5 = stack[int(P)];
        P = P - 2;
        t0 = H;
        heap[int(H)] = 1;
        H = H + 1;
        heap[int(H)] = t5;
        H = H + 1;

        t7 = heap[int(t0)];
        t0 = t0+1;
        t8 = heap[int(t0)];
        L2:
        t6 = P+2;
        stack[int(t6)] = t7;
        if t7 > t8 {goto L3;}
        t7 = t7+1;
        t13 = P+2;
        t12 = stack[int(t13)];

        t10 = t12;
        t11 = stack[int(1)];
        t9 = heap[int(t11)];
        if t10 < 1 {goto L4;}
        if t10 > t9 {goto L4;}
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
        t9 = 0;
        goto L6;
        L5:
        t11 = t11+t10;
        t9 = heap[int(t11)];
        L6:
        fmt.Printf("%d", int(t9));
        fmt.Printf("%c", int(10));
        goto L2;
        L3:

        /***** END FOR *****/
        goto L0;
        L0:
        return;
}

func main(){
        /***** BEGIN ARRAY *****/
        t14 = H;
        t15 = t14;
        H = H+17;
        heap[int(t15)] = 16;
        t15 = t15+1;
        heap[int(t15)] = 32;
        t15 = t15+1;
        t16 = 7*3;
        heap[int(t15)] = t16;
        t15 = t15+1;
        heap[int(t15)] = 7;
        t15 = t15+1;
        heap[int(t15)] = 89;
        t15 = t15+1;
        heap[int(t15)] = 56;
        t15 = t15+1;
        heap[int(t15)] = 909;
        t15 = t15+1;
        heap[int(t15)] = 109;
        t15 = t15+1;
        heap[int(t15)] = 2;
        t15 = t15+1;
        heap[int(t15)] = 9;
        t15 = t15+1;
        t20 = P+0;
        t20 = t20+1;
        stack[int(t20)] = 9874;
        t21 = t20+1;
        stack[int(t21)] = 0;
        P = P + 0;
        native_power();
        t22 = stack[int(P)];
        P = P - 0;
        heap[int(t15)] = t22;
        t15 = t15+1;
        heap[int(t15)] = 44;
        t15 = t15+1;
        heap[int(t15)] = 3;
        t15 = t15+1;
        t23 = 820*10;
        heap[int(t15)] = t23;
        t15 = t15+1;
        heap[int(t15)] = 11;
        t15 = t15+1;
        t24 = 8*0;
        t25 = t24+8;
        heap[int(t15)] = t25;
        t15 = t15+1;
        heap[int(t15)] = 10;
        /***** END ARRAY *****/
        stack[int(0)] = t14;


        /***** BEGIN SAVING TEMPS *****/
        t26 = P+1;
        stack[int(t26)] = t21;
        /***** END SAVING TEMPS *****/

        t27 = stack[int(0)];

        t28 = P+3;
        stack[int(t28)] = t27;
        P = P + 2;
        bubbleSort();
        t28 = stack[int(P)];
        P = P - 2;

        /***** BEGIN RECOVERING TEMPS *****/
        t29 = P+1;
        t21 = stack[int(t29)];
        /***** END RECOVERING TEMPS *****/



}