function StringFunction()

    str1 = "Sale Compiladores 2"::String;

    println("FUNCIONES STRING:");
    println("Concatenacion:");
    println(str1 * " C3D - segundo Proyecto");
    println("UpperCase:");
    println(uppercase(str1));
    println("LowerCase:");
    println(lowercase(str1 * " SI SALE"));

    println("Concatenacion + :");
    println("string * string");
    println(str1 * " C3D - segundo Proyecto");
    println("string * numero entero");
    println("entero = " * "125");  ## NO STRING()
    println("string * numero decimal");
    println("decimal = " * "45.3246");  ## NO STRING()
    println("decimal = " * "176/3");  ## NO STRING()
end;

function testambito()
    numberstring= "100" * "Usac"::String;  ## NO STRING()
    stringnumber= "Usac" * "2500"::String;
    stringstring= "Universidad" * " San Carlos"::String;
    println(numberstring);
    println(stringnumber);
    println(stringstring);
end;

function todas(parametro::String)
    println(uppercase(lowercase(parametro)));
end;

StringFunction();
testambito();
todas("hoy ganO compi2");
