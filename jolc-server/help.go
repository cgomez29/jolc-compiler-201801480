/*----HEADER----*/
package main;

import (
        "fmt"
);

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12 float64;
var P, H float64;
var stack [29101998]float64;
var heap [29101998]float64;

/*-----NATIVES-----*/
func native_print_string(){
        t7 = P+1;
        t8 = stack[int(t7)];
        L2:
        t9 = heap[int(t8)];
        if t9 == -1 {goto L1;}
        fmt.Printf("%c", int(t9));
        t8 = t8+1;
        goto L2;
        L1:
        return;
}

/*-----FUNCS-----*/
func contratos(){
        t0 = H;
        t1 = t0;
        H = H+2;
        t2 = H;
        heap[int(H)] = 99;
        H = H + 1;
        heap[int(H)] = 114;
        H = H + 1;
        heap[int(H)] = 105;
        H = H + 1;
        heap[int(H)] = 115;
        H = H + 1;
        heap[int(H)] = -1;
        H = H + 1;
        heap[int(t1)] = t2;
        t1 = t1+1;
        heap[int(t1)] = 38;
        t1 = t1+1;
        t3 = P+1;
        stack[int(t3)] = t0;

        t5 = P+1;
        t4 = stack[int(t5)];

        t4 = t4+0;
        t6 = heap[int(t4)];
        /***** BEGIN PRINT STRING *****/
        t10 = P+2;
        t10 = t10+1;
        stack[int(t10)] = t6;
        P = P + 2;
        native_print_string();
        t11 = stack[int(P)];
        P = P - 2;
        /***** END PRINT STRING *****/
        fmt.Printf("%c", int(10));
        goto L0;
        L0:
        return;
}

func main(){
        P = P + 0;
        contratos();
        t12 = stack[int(P)];
        P = P - 0;


}