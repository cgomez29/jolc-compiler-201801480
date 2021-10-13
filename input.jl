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



# mutable struct Juguete 
#     name;
#     precio;
# end;

# mutable struct Mascota
#     name;
#     juguete;
#   end;
  
# mutable struct Persona 
#     nombre;
#     edad;
#     mascota;
# end;
  
# j = Juguete("j", 56);
# m = Mascota("m", j);
# p = Persona("cr", 22, m);

# println(p.mascota.juguete.name);


# x = [1,["cris"],"gomez",[4,5,"guzman"],7,8];
# x = [1,["cris",[22,23,["u","s","a","c"]]],"gomez"];

# println(x);

# function factorial(n)
#     if(n == 0)
#         return 1;
#     end;

#     # return n * factorial(n-1);
# end;

# println(factorial(5));

# ======================================================

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


# id normal
# 1
# 1
# 1
# 1
# El valor de a es: 
# 1
# a
# b

# a = 0;

# while a < 5
#     a = a + 1;
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


a = 0;

a = a + 1;

println(a);
