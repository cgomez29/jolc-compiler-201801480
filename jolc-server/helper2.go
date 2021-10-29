fmt.Printf("%d", int(heap[int(0)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(1)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(2)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(3)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(4)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(5)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(6)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(7)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(8)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(9)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(10)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(11)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(12)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(13)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(14)]));
fmt.Printf("%c", int(10));
fmt.Printf("%d", int(heap[int(15)]));












/*----HEADER----*/
package main;

import (
        "fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 float64;
var P, H float64;
var stack [29101998]float64;
var heap [29101998]float64;

/*-----NATIVES-----*/
func printString(){
        t7 = P+1;
        t8 = stack[int(t7)];
        L6:
        t9 = heap[int(t8)];
        if t9 == -1 {goto L5;}
        fmt.Printf("%c", int(t9));
        t8 = t8+1;
        goto L6;
        L5:
        return;
}


func main(){
        stack[int(0)] = 0;

        /* start while */
        L0:
        /* Start relational expression */
        t0 = stack[int(0)];

        if t0 < 5 {goto L1;}
        goto L2;
        /* FIN DE EXPRESION RELACIONAL */

        L1:
        t1 = stack[int(0)];

        t2 = t1+1;
        t3 = P+1;
        stack[int(t3)] = t2;

        /* Start if */
        /* Start relational expression */
        t5 = P+1;
        t4 = stack[int(t5)];

        if t4 == 2 {goto L3;}
			goto L4;
			/* FIN DE EXPRESION RELACIONAL */

			L3:
			t6 = H;
			heap[int(H)] = 98;
			H = H + 1;
			heap[int(H)] = -1;
			H = H + 1;
			/* String print start */
			t10 = P+2;
			t10 = t10+1;
			stack[int(t10)] = t6;
			P = P + 2;
			printString();
			t11 = stack[int(P)];
			P = P - 2;
			/* String print end */
			fmt.Printf("%c", int(10));
			goto L2;
        L4:
        /* Fin if */
        t12 = H;
        heap[int(H)] = 118;
        H = H + 1;
        heap[int(H)] = 32;
        H = H + 1;
        heap[int(H)] = 101;
        H = H + 1;
        heap[int(H)] = 115;
        H = H + 1;
        heap[int(H)] = 58;
        H = H + 1;
        heap[int(H)] = 32;
        H = H + 1;
        heap[int(H)] = -1;
        H = H + 1;
        /* String print start */
        t13 = P+2;
        t13 = t13+1;
        stack[int(t13)] = t12;
        P = P + 2;
        printString();
        t14 = stack[int(P)];
        P = P - 2;
        /* String print end */
        fmt.Printf("%c", int(10));
        t16 = P+1;
        t15 = stack[int(t16)];

        fmt.Printf("%d", int(t15));
        fmt.Printf("%c", int(10));
        goto L0;
        L2:
        /* fin while */

        return;
}