/*----HEADER----*/
package main;

import (
        "fmt"
);

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37 float64;
var P, H float64;
var stack [29101998]float64;
var heap [29101998]float64;

/*-----NATIVES-----*/
func native_print_string(){
        t19 = P+1;
        t20 = stack[int(t19)];
        L5:
        t21 = heap[int(t20)];
        if t21 == -1 {goto L4;}
        fmt.Printf("%c", int(t21));
        t20 = t20+1;
        goto L5;
        L4:
        return;
}

/*-----FUNCS-----*/
func contratar(){
        t0 = H;
        t1 = t0;
        H = H+2;
        t3 = P+1;
        t2 = stack[int(t3)];

        heap[int(t1)] = t2;
        t1 = t1+1;
        t5 = P+2;
        t4 = stack[int(t5)];

        heap[int(t1)] = t4;
        t1 = t1+1;
        stack[int(P)] = t0;
        goto L0;
        goto L0;
        L0:
        return;
}
func crearActor(){
        t6 = H;
        t7 = t6;
        H = H+2;
        t9 = P+1;
        t8 = stack[int(t9)];

        heap[int(t7)] = t8;
        t7 = t7+1;
        t11 = P+2;
        t10 = stack[int(t11)];

        heap[int(t7)] = t10;
        t7 = t7+1;
        stack[int(P)] = t6;
        goto L1;
        goto L1;
        L1:
        return;
}
func crearPelicula(){
        t12 = H;
        t13 = t12;
        H = H+2;
        t15 = P+1;
        t14 = stack[int(t15)];

        heap[int(t13)] = t14;
        t13 = t13+1;
        t17 = P+2;
        t16 = stack[int(t17)];

        heap[int(t13)] = t16;
        t13 = t13+1;
        stack[int(P)] = t12;
        goto L2;
        goto L2;
        L2:
        return;
}
func imprimir(){
        t18 = H;
        heap[int(H)] = 65;
        H = H + 1;
        heap[int(H)] = 99;
        H = H + 1;
        heap[int(H)] = 116;
        H = H + 1;
        heap[int(H)] = 111;
        H = H + 1;
        heap[int(H)] = 114;
        H = H + 1;
        heap[int(H)] = 58;
        H = H + 1;
        heap[int(H)] = 32;
        H = H + 1;
        heap[int(H)] = -1;
        H = H + 1;
        /***** BEGIN PRINT STRING *****/
        t22 = P+2;
        t22 = t22+1;
        stack[int(t22)] = t18;
        P = P + 2;
        native_print_string();
        t23 = stack[int(P)];
        P = P - 2;
        /***** END PRINT STRING *****/
        
        /***** BEGIN STRUCT ACCESS *****/
        t25 = P+1;
        t24 = stack[int(t25)];

        t26 = t26+0;
        t26 = heap[int(t26)];
        /***** END STRUCT ACCESS *****/

        /***** BEGIN PRINT STRING *****/
        t27 = P+2;
        t27 = t27+1;
        stack[int(t27)] = t26;
        P = P + 2;
        native_print_string();
        t28 = stack[int(P)];
        P = P - 2;
        /***** END PRINT STRING *****/
        fmt.Printf("%c", int(10));
        goto L3;
        L3:
        return;
}
func contratos(){
        t29 = H;
        heap[int(H)] = 115;
        H = H + 1;
        heap[int(H)] = 105;
        H = H + 1;
        heap[int(H)] = 117;
        H = H + 1;
        heap[int(H)] = -1;
        H = H + 1;
        t30 = P+2;
        stack[int(t30)] = t29;
        t30 = t30+1;
        stack[int(t30)] = 38;
        t30 = t30+1;
        P = P + 1;
        crearActor();
        t30 = stack[int(P)];
        P = P - 1;
        t31 = P+1;
        stack[int(t31)] = t30;


        /***** BEGIN SAVING TEMPS *****/
        t32 = P+2;
        stack[int(t32)] = t30;
        /***** END SAVING TEMPS *****/

        t34 = P+1;
        t33 = stack[int(t34)];

        t35 = P+4;
        stack[int(t35)] = t33;
        P = P + 3;
        imprimir();
        t35 = stack[int(P)];
        P = P - 3;

        /***** BEGIN RECOVERING TEMPS *****/
        t36 = P+2;
        t30 = stack[int(t36)];
        /***** END RECOVERING TEMPS *****/

        goto L6;
        L6:
        return;
}

func main(){
        P = P + 0;
        contratos();
        t37 = stack[int(P)];
        P = P - 0;
	
for i := 0; i < 50; i++ {
        fmt.Printf("%d", i);
        fmt.Printf("%c", ' ');
        fmt.Printf("%d", int(heap[int(i)]));
        fmt.Printf("%c", int(10));

    }


}