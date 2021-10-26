# if 5 > 1
#     println("id normal");
# end;

# if 10 == 11
#     println(0);
# elseif 10 != 11
#     println(1);
# else
#     println(0);
# end;

# if 5 > 1
#     println(1);
#     if true 
#         println(1);

#         if false 
#             println(0);
#         else 
#             println(1);
#         end;
#     elseif false
#         println(0);
#     else
#         println(0);
#     end;
# end;

# a = 0;
# while a < 5
#     global a = a + 1;
#     if a == 2
#         println("a");
#         continue;
#     elseif a == 3
#         println("b");
#         break;
#     end;
#     println("v es: ");
#     println(a);
# end;

# ================================================


# function x()
#     return 4;
# end;
# function y(x)
#     return 5;
# end;

# # println(x());
# y(2);

# function x(n:number):number {
#     return n;
# }

# x(1);


# function x(n)
#     f = 5;
#     return f+n+n;
# end;

# function y(n,b)
#     return n*b;
# end;


# println(y(4,4));


# println(y(4,4));




# function potencia(base, exp)
#     if exp == 0 
#         return 1;
#     end;
#     return base * potencia(base, exp-1);
# end;

# println(potencia(5, 2));

# function factorial(n)

#     if n == 0 
#         return 1;
#     end;
#     return n * factorial(n-1);
# end;

# println(factorial(5));


# # function potencia(base, exp)
# #     if exp == 0 
# #         return 1;
# #     end;
# #     return base * potencia(base, exp-1);
# # end;


# # println(potencia(5, 2));

# function ackerman(m::Int64, n::Int64)
#     if m == 0
#         return n + 1;
#     elseif m > 0 && n == 0
#         return ackerman(m - 1, 1);
#     else
#         return ackerman(m - 1, ackerman(m, n - 1));
#     end;
# end;
# println(ackerman(3, 4));



# function factorial(n::Int64)
#     if n == 0 
#         return 1;
#     end;

#     return n * factorial(n-1);
# end;

# println(factorial(5));


# mutable struct Juguete 
#     name::String;
#     precio::Int64;
# end;

# mutable struct Mascota
#     name::String;
#     juguete::Juguete;
# end;
  
# mutable struct Persona 
#     nombre::String;
#     edad::Int64;
#     mascota::Mascota;
# end;

# j = Juguete("peluche", 56)::Juguete;
# m = Mascota("lucas", j)::Mascota;
# p = Persona("Cristian", 22, m)::Persona;

# println(p.mascota.juguete.name);

# j.name = "hueso";

# println(p.mascota.juguete.name);
# println(j.name);


# math. Esta únicamente aceptará la función 
# math.Mod(VALOR1, VALOR2).


# x = [1,[5,[22,23,["cristian",13,14,15]]],18];
# # x = [4,5,6];

# println(x);

# for letra in "cris"
#     println(letra);
#     continue;
# end;

# x = "cris";

# for letra in x
#     println(letra);
# end;

# x = 21:30;

# for i in x
#     println(i+1);
# end;

# for i in [1,20,3,5,6,[1,5],8]
#     println(i);
# end;



# x = [5,[9,10],7,8];

# x[2][3] = 6; 

# println(x);

# function sumar(a::Float64)
#     b = 2.0;
#     for i in 1:4
#         b = b + a * i;
#     end;
#     return b;
# end;

# print(sumar(5.5));

# function valores(x)
#     println(x);
# end;
# valores(5);

# y = 5 + 6 * 2 % 2;
# println(y);

# # function valores(x)
# #     x[2][2] = 3;
# # end;
# x = [5,7,[9,10],8,11];
# # valores(x);
# print(x);

# =========================================================

# val1 = 1::Int64;
# val2 = 10::Int64;
# val3 = 2021.2020::Float64;

# println("Probando declaracion de variables");
# println(val1, " ", val2, " ", val3);
# println("---------------------------------");
# # COMENTARIO DE UNA LINEA
# val1 = val1 + 41 - 123 * 4 / (2 + 2 * 2) - (10 + (125 % 5)) * 2 ^ 2;
# val2 = 11 * (11 % (12 + -10)) + 22 / 2;
# val3 = 2 ^ (2 * 12 / 6) + 25 / 5#= COMENTARIO
# MULTILINEA =#;
# println("Probando asignación de variables y aritmeticas");
# println(val1, " ", val2, " ", val3);
# println("---------------------------------");

# val1 = 1::Int64;
# val2 = 10::Int64;
# val3 = 2021.2020::Float64;


# f = ((0 == 0) != ((532 > 532)) == ("Hola" == "Hola"));

# println(f);


# rel1 = (((val1 - val2) == 24) && (true && (false || 5 >= 5))) || ((7*7) != (15+555) || -61 > 51);
# rel3 = ((0 == 0) != ((532 > 532)) == ("Hola" == "Hola")) && (false || (false == true));
rel3 = (("Hola" == "Hola") && (false || true));

println(rel3);