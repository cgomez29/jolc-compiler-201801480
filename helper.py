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