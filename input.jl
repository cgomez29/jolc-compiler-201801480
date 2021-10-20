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


x = 21.1 % 2;

println(x);
