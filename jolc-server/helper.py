#=========================================================
#
#=========================================================


type Cosa = {
  name:string,
  edadCosa:number
};

type Persona = {
    nombre:string,
    edad:number,
    cosa:Cosa
};

let c:Cosa = {
    name: "c",
    edadCosa: 56
};

let p:Persona = {
    nombre: "cr",
    edad: 22,
    cosa: c
};

console.log(p.nombre);

function factorial(n:number):number {
    if (n == 0) {
        return 1;
    }
    
    return n * factorial(n-1);
}

console.log(factorial(5));


 function ackermann( m:number,  n:number):number {
        if (m == 0) {
            return (n + 1);
        } else if (m > 0 && n == 0) {
           return ackermann(m - 1, 1);
        } else {
            return ackermann(m - 1, ackermann(m, n - 1));
        }
    
}
console.log(ackermann(3,8)); //2045 se tardo 6 segundos