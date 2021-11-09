/*----HEADER----*/
package main;

import (
        "fmt"
);

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24 float64;
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
func native_print_string(){
        t20 = P+1;
        t21 = stack[int(t20)];
        L8:
        t22 = heap[int(t21)];
        if t22 == -1 {goto L7;}
        fmt.Printf("%c", int(t22));
        t21 = t21+1;
        goto L8;
        L7:
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
        t6 = t5-1;
        t0 = H;
        heap[int(H)] = 1;
        H = H + 1;
        heap[int(H)] = t6;
        H = H + 1;

        t8 = heap[int(t0)];
        t0 = t0+1;
        t9 = heap[int(t0)];
        L2:
        t7 = P+2;
        stack[int(t7)] = t8;
        if t8 > t9 {goto L3;}
        t8 = t8+1;
        t14 = P+2;
        t13 = stack[int(t14)];

        t11 = t13;
        t12 = stack[int(1)];
        t10 = heap[int(t12)];
        if t11 < 1 {goto L4;}
        if t11 > t10 {goto L4;}
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
        t10 = 0;
        goto L6;
        L5:
        t12 = t12+t11;
        t10 = heap[int(t12)];
        L6:
        fmt.Printf("%d", int(t10));
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
        t15 = H;
        t16 = t15;
        H = H+6;
        heap[int(t16)] = 5;
        t16 = t16+1;
        heap[int(t16)] = 10;
        t16 = t16+1;
        heap[int(t16)] = 15;
        t16 = t16+1;
        heap[int(t16)] = 20;
        t16 = t16+1;
        heap[int(t16)] = 25;
        t16 = t16+1;
        heap[int(t16)] = 30;
        /***** END ARRAY *****/
        stack[int(0)] = t15;

        t17 = stack[int(0)];

        t18 = P+2;
        stack[int(t18)] = t17;
        P = P + 1;
        bubbleSort();
        t18 = stack[int(P)];
        P = P - 1;
        t19 = H;
        heap[int(H)] = 115;
        H = H + 1;
        heap[int(H)] = 111;
        H = H + 1;
        heap[int(H)] = 111;
        H = H + 1;
        heap[int(H)] = 111;
        H = H + 1;
        heap[int(H)] = -1;
        H = H + 1;
        /***** BEGIN PRINT STRING *****/
        t23 = P+1;
        t23 = t23+1;
        stack[int(t23)] = t19;
        P = P + 1;
        native_print_string();
        t24 = stack[int(P)];
        P = P - 1;
        /***** END PRINT STRING *****/
        fmt.Printf("%c", int(10));


}