/* Sergio Paredes - Legajo 260.861-3 - Comision S1554 - Sede: Campus - Horario: Jue 18:15 a 21:30 */
/* Este programa sirve para registrar las ventas de una farmacia controlando el stock, buscar medicamentos por nombre en la base ordenada (busqueda binaria), actualizar precios, reponer stock e informar existencias nulas, medicamentos a reponer y la recaudacion por obra social */

#include <iostream>
#include <iomanip>
#include <string.h>
#include <cctype>
#include <cstdlib>
#include <cmath>

using namespace std;

// ---------------------------------------------------------------
// FUNCION DE BUSQUEDA BINARIA
// Se escribe como funcion porque la usan cuatro opciones del menu
// (ventas, consulta, precio y reposicion): asi la busqueda esta en
// un solo lugar y, si hubiera que corregirla, se corrige una vez.
// Recibe la matriz de nombres YA ORDENADA, la cantidad de nombres
// y el nombre buscado YA EN MAYUSCULAS. Devuelve la posicion donde
// esta (de 1 a cant), o 0 si no esta.
// ---------------------------------------------------------------
int buscarMedicamento(char nombres[][30], int cant, char buscado[])
{
    int inicio = 1;
    int fin = cant;
    int medio;
    int posicion = 0;          // 0 = todavia no lo encontre

    // El motor se detiene por dos razones: lo encontre (posicion
    // distinta de 0) o la zona de busqueda quedo vacia (inicio > fin).
    while (inicio <= fin && posicion == 0)
    {
        medio = (inicio + fin) / 2;
        if (strcmp(buscado, nombres[medio]) == 0)
            posicion = medio;                  // es este
        else if (strcmp(buscado, nombres[medio]) < 0)
            fin = medio - 1;                   // esta en la mitad de arriba
        else
            inicio = medio + 1;                // esta en la mitad de abajo
    }
    return posicion;
}

// ---------------------------------------------------------------
// FUNCIONES DE LECTURA VALIDADA
// El programa lee datos del teclado en muchos lugares. Cada lectura
// necesita el mismo control: destrabar cin si escribieron algo
// invalido, descartar el resto de la linea y repetir la pregunta.
// Con estas tres funciones ese control esta escrito una sola vez.
// Las tres terminan el programa si se acaba la entrada de datos
// (Ctrl+Z en Windows, Ctrl+D en Linux): sin teclado no hay forma
// de seguir, y si no se cortara repetiria el error para siempre.
// ---------------------------------------------------------------

// Lee un entero entre minimo y maximo (ambos incluidos).
int leerEntero(int minimo, int maximo)
{
    int valor;
    int valido = 0;
    while (valido == 0)
    {
        cin >> valor;
        if (cin.eof())             // se acabo la entrada: no hay mas que leer
        {
            cout << endl << "Fin de la entrada de datos: el programa termina." << endl;
            exit(0);
        }
        // invalido si escribieron letras (cin falla) o si despues del
        // numero quedo algo que no es el ENTER, como en 12abc o 2.5
        if (cin.fail() || cin.peek() != '\n')
        {
            cin.clear();           // destraba cin
            valor = minimo - 1;    // valor invalido a proposito, no depende de cin
        }
        cin.ignore(1000, '\n');    // descarta el resto de la linea
        if (valor >= minimo && valor <= maximo)
            valido = 1;
        else
            cout << "   Valor invalido. Ingrese un entero entre " << minimo << " y " << maximo << ": ";
    }
    return valor;
}

// Lee un numero real mayor que 0 y como mucho igual a maximo.
double leerPositivo(double maximo)
{
    double valor;
    int valido = 0;
    while (valido == 0)
    {
        cin >> valor;
        if (cin.eof())
        {
            cout << endl << "Fin de la entrada de datos: el programa termina." << endl;
            exit(0);
        }
        // invalido si fallo o si quedo algo despues del numero, como la
        // coma de 5600,50 (C++ solo entiende el punto decimal)
        if (cin.fail() || cin.peek() != '\n')
        {
            cin.clear();
            valor = 0;             // valor invalido a proposito, no depende de cin
        }
        cin.ignore(1000, '\n');
        if (valor > 0 && valor <= maximo)
            valido = 1;
        else
            cout << "   Valor invalido. Ingrese un numero mayor que 0 y hasta " << maximo
                 << " (use punto para los decimales): ";
    }
    return valor;
}

// Lee un nombre de medicamento: hasta 29 letras, sin los espacios del
// final y en mayusculas, listo para buscarlo. Si es demasiado largo
// avisa y lo deja vacio; quien llama no busca un nombre vacio.
void leerNombre(char texto[])
{
    int largo, k;

    cin.getline(texto, 30, '\n');
    if (cin.eof())
    {
        cout << endl << "Fin de la entrada de datos: el programa termina." << endl;
        exit(0);
    }
    if (cin.fail())                    // 30 letras o mas: cin queda trabado
    {
        cin.clear();
        cin.ignore(1000, '\n');        // descarta lo que no entro
        texto[0] = '\0';               // se vacia: no queda el nombre anterior
        cout << "   Nombre demasiado largo (maximo 29 letras)" << endl;
    }

    // saca los espacios del final: mientras el ultimo caracter sea un
    // espacio, se corta el texto una posicion antes
    largo = strlen(texto);
    while (largo > 0 && texto[largo - 1] == ' ')
    {
        largo--;
        texto[largo] = '\0';
    }

    for (k = 0; texto[k] != '\0'; k++)     // pasa el nombre a mayusculas
        texto[k] = toupper((unsigned char)texto[k]);   // (unsigned char): una letra con tilde
                                                        // seria negativa y toupper no la acepta
}

int main()
{
    // ---------------------------------------------------------------
    // BASE INICIAL DE MEDICAMENTOS (vectores paralelos)
    // Cada posicion i (de 1 a CANT) es un medicamento: su codigo esta
    // en codMed[i], su nombre en nomMed[i], su precio en precioMed[i]
    // y su stock en stockMed[i]. La posicion 0 no se usa, para contar
    // de 1 en adelante como en el apunte.
    // Se carga desordenada a proposito: el programa la ordena despues.
    // Precios e importes van en double y no en float: float guarda
    // unos 7 digitos exactos y una suma de 6 cifras con centavos ya
    // podria correr los centavos; double guarda unos 15.
    // ---------------------------------------------------------------
    const int CANT = 18;
    const int STOCK_CRITICO = 5;   // con esta cantidad o menos, hay que reponer

    int codMed[CANT + 1] = { 0,
        1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109,
        1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118 };

    char nomMed[CANT + 1][30] = { "",
        "PARACETAMOL", "IBUPROFENO", "OMEPRAZOL", "AMOXICILINA",
        "LORATADINA", "ENALAPRIL", "METFORMINA", "ATORVASTATINA",
        "DICLOFENAC", "LOSARTAN", "ACIDO FOLICO", "SALBUTAMOL",
        "CLONAZEPAM", "LEVOTIROXINA", "AZITROMICINA", "BUDESONIDA",
        "CETIRIZINA", "ATENOLOL" };

    double precioMed[CANT + 1] = { 0,
        2350.00, 2890.50, 4120.00, 6750.00, 3180.00, 3540.75,
        4890.00, 8920.00, 2640.00, 5310.00, 1980.00, 7450.00,
        5780.00, 6230.00, 9850.00, 11200.00, 3360.00, 2970.00 };

    int stockMed[CANT + 1] = { 0,
        40, 35, 20, 12, 25, 18, 30, 10, 22,
        15, 3, 6, 8, 14, 2, 5, 4, 16 };

    // variables de trabajo
    int i, j, pasada, huboCambio;
    int auxInt;
    double auxPrecio;
    char auxNom[30];
    int opcion, pos;
    char buscado[30];

    // variables de las ventas
    int cantidad, obraSocial;
    double importe;
    double recaudOS[21] = { 0 };   // importe por obra social: recaudOS[1] a recaudOS[20], todo en 0
    int loteOk, loteRech;          // ventas aceptadas y rechazadas del lote actual
    double importeLote;
    int ventasOk = 0, ventasRech = 0;   // totales de toda la sesion
    double recaudTotal = 0;
    int hayNulos, hayVentasOS, hayReponer;

    // variables de precios y reposicion
    double precioAnterior, porcentaje;
    int stockAnterior;

    cout << fixed << setprecision(2);   // importes siempre con 2 decimales

    // en esta linea comienza el proceso de ordenamiento
    // Burbujeo por nombre (orden alfabetico). Se comparan vecinos j y j+1
    // y, si estan al reves, se intercambian LOS CUATRO vectores juntos,
    // para que cada codigo, precio y stock siga con su nombre.
    // Si en una pasada no hubo ningun intercambio, ya esta ordenado.
    huboCambio = 1;
    pasada = 0;
    while (huboCambio == 1)
    {
        huboCambio = 0;
        for (j = 1; j < CANT - pasada; j++)
        {
            if (strcmp(nomMed[j], nomMed[j + 1]) > 0)
            {
                strcpy(auxNom, nomMed[j]);
                strcpy(nomMed[j], nomMed[j + 1]);
                strcpy(nomMed[j + 1], auxNom);

                auxInt = codMed[j];
                codMed[j] = codMed[j + 1];
                codMed[j + 1] = auxInt;

                auxPrecio = precioMed[j];
                precioMed[j] = precioMed[j + 1];
                precioMed[j + 1] = auxPrecio;

                auxInt = stockMed[j];
                stockMed[j] = stockMed[j + 1];
                stockMed[j + 1] = auxInt;

                huboCambio = 1;
            }
        }
        pasada++;
    }

    // en esta linea comienza el menu principal
    opcion = -1;
    while (opcion != 0)
    {
        cout << endl << "===== FARMACIA - MENU =====" << endl;
        cout << "1. Cargar lote de ventas" << endl;
        cout << "2. Consultar un medicamento" << endl;
        cout << "3. Actualizar precio de un medicamento" << endl;
        cout << "4. Reponer stock" << endl;
        cout << "5. Listado de medicamentos" << endl;
        cout << "6. Aumento general de precios" << endl;
        cout << "0. Terminar e informar" << endl;
        cout << "Opcion: ";
        opcion = leerEntero(0, 6);

        // Las opciones 2, 3 y 4 empiezan igual: piden un nombre y lo buscan.
        // Esa parte se hace una sola vez aca; despues cada opcion usa pos.
        pos = 0;
        if (opcion >= 2 && opcion <= 4)
        {
            cout << "Nombre del medicamento: ";
            leerNombre(buscado);
            if (buscado[0] != '\0')          // un nombre vacio no se busca
            {
                pos = buscarMedicamento(nomMed, CANT, buscado);
                if (pos == 0)
                    cout << "   " << buscado << ": no figura en la base de la farmacia" << endl;
            }
        }

        if (opcion == 1)
        {
            // en esta linea comienza el lote de ventas
            // Se lee el primer nombre ANTES del while y el siguiente al final
            // de cada vuelta (como en el apunte), asi la clave PPPPPPP se
            // controla antes de procesar nada.
            loteOk = 0;
            loteRech = 0;
            importeLote = 0;

            cout << "Nombre del medicamento (PPPPPPP para terminar): ";
            leerNombre(buscado);

            while (strcmp(buscado, "PPPPPPP") != 0)
            {
                if (buscado[0] != '\0')      // un nombre vacio no se busca
                {
                    pos = buscarMedicamento(nomMed, CANT, buscado);
                    if (pos == 0)
                        cout << "   " << buscado << ": no figura en la base de la farmacia" << endl;
                    else
                    {
                        cout << "Cantidad: ";
                        cantidad = leerEntero(1, 10000);
                        cout << "Obra social (1 a 20): ";
                        obraSocial = leerEntero(1, 20);

                        // solo se vende si alcanza el stock para el total pedido
                        if (cantidad <= stockMed[pos])
                        {
                            stockMed[pos] = stockMed[pos] - cantidad;
                            importe = cantidad * precioMed[pos];
                            recaudOS[obraSocial] = recaudOS[obraSocial] + importe;
                            importeLote = importeLote + importe;
                            loteOk++;
                            cout << "   VENDIDO: " << nomMed[pos] << "   Importe total: $ " << importe << endl;
                        }
                        else
                        {
                            loteRech++;
                            cout << "   " << nomMed[pos] << ": sin existencia" << endl;
                        }
                    }
                }

                cout << "Nombre del medicamento (PPPPPPP para terminar): ";
                leerNombre(buscado);
            }

            // resumen del lote y paso a los totales de la sesion
            cout << "--- Lote cerrado: " << loteOk << " aceptadas, " << loteRech
                 << " rechazadas, importe del lote $ " << importeLote << endl;
            ventasOk = ventasOk + loteOk;
            ventasRech = ventasRech + loteRech;
            recaudTotal = recaudTotal + importeLote;
        }
        else if (opcion == 2 && pos != 0)
        {
            // en esta linea comienza la consulta de un medicamento
            cout << "Codigo: " << codMed[pos] << endl;
            cout << "Nombre: " << nomMed[pos] << endl;
            cout << "Precio: " << precioMed[pos] << endl;
            cout << "Stock:  " << stockMed[pos] << endl;
        }
        else if (opcion == 3 && pos != 0)
        {
            // en esta linea comienza la actualizacion del precio de un medicamento
            cout << "Precio actual: $ " << precioMed[pos] << endl;
            cout << "Precio nuevo: ";
            precioAnterior = precioMed[pos];
            precioMed[pos] = leerPositivo(1000000);
            cout << "   " << nomMed[pos] << ": $ " << precioAnterior
                 << " -> $ " << precioMed[pos] << endl;
        }
        else if (opcion == 4 && pos != 0)
        {
            // en esta linea comienza la reposicion de stock
            cout << "Stock actual: " << stockMed[pos] << endl;
            cout << "Cantidad que ingresa: ";
            stockAnterior = stockMed[pos];
            stockMed[pos] = stockMed[pos] + leerEntero(1, 10000);
            cout << "   " << nomMed[pos] << ": stock " << stockAnterior
                 << " -> " << stockMed[pos] << endl;
        }
        else if (opcion == 6)
        {
            // en esta linea comienza el aumento general de precios
            cout << "Porcentaje de aumento (ej. 8.5): ";
            porcentaje = leerPositivo(100);
            for (i = 1; i <= CANT; i++)
            {
                precioMed[i] = precioMed[i] * (1 + porcentaje / 100);
                // redondeo a centavos: se corre la coma 2 lugares, se suma 0.5,
                // floor redondea hacia abajo al entero y se vuelve a correr la coma
                // (no se usa (int) porque desborda pasando unos 21 millones)
                precioMed[i] = floor(precioMed[i] * 100 + 0.5) / 100;
            }
            cout << "   Precios aumentados un " << porcentaje << " %" << endl;
        }

        // El listado se muestra al elegir 5 y tambien despues del aumento
        // general (6), para ver los precios nuevos sin repetir este bloque.
        if (opcion == 5 || opcion == 6)
        {
            // en esta linea comienza el listado ordenado de la base
            cout << endl << "LISTADO DE MEDICAMENTOS (orden alfabetico)" << endl;
            cout << left  << setw(5)  << "POS" << setw(8) << "CODIGO" << setw(16) << "MEDICAMENTO"
                 << right << setw(12) << "PRECIO" << setw(8) << "STOCK" << endl;
            for (i = 1; i <= CANT; i++)
            {
                cout << left  << setw(5)  << i << setw(8) << codMed[i] << setw(16) << nomMed[i]
                     << right << setw(12) << precioMed[i] << setw(8) << stockMed[i];
                if (stockMed[i] > 0 && stockMed[i] <= STOCK_CRITICO)
                    cout << "   STOCK CRITICO";
                cout << endl;
            }
        }
    }

    // en esta linea comienzan los informes finales
    cout << endl << "===== INFORMES FINALES =====" << endl;

    // punto 2: medicamentos que quedaron con existencia nula
    cout << endl << "Medicamentos con existencia nula:" << endl;
    hayNulos = 0;
    for (i = 1; i <= CANT; i++)
    {
        if (stockMed[i] == 0)
        {
            cout << "   " << codMed[i] << "  " << nomMed[i] << endl;
            hayNulos = 1;
        }
    }
    if (hayNulos == 0)
        cout << "   Ninguno: todos los medicamentos tienen stock" << endl;

    // medicamentos a reponer: stock nulo o critico
    cout << endl << "Medicamentos a reponer (stock " << STOCK_CRITICO << " o menos):" << endl;
    hayReponer = 0;
    for (i = 1; i <= CANT; i++)
    {
        if (stockMed[i] <= STOCK_CRITICO)
        {
            cout << "   " << codMed[i] << "  " << left << setw(16) << nomMed[i]
                 << right << "stock " << setw(3) << stockMed[i] << endl;
            hayReponer = 1;
        }
    }
    if (hayReponer == 0)
        cout << "   Ninguno" << endl;

    // punto 3: importe total abonado por cada obra social
    cout << endl << "Importe por obra social:" << endl;
    hayVentasOS = 0;
    for (i = 1; i <= 20; i++)
    {
        if (recaudOS[i] > 0)
        {
            cout << "   Obra social " << setw(2) << i << ":  $ " << setw(12) << recaudOS[i] << endl;
            hayVentasOS = 1;
        }
    }
    if (hayVentasOS == 0)
        cout << "   No hubo ventas" << endl;

    // totales de la sesion
    cout << endl << "Ventas aceptadas:   " << ventasOk << endl;
    cout << "Ventas rechazadas:  " << ventasRech << endl;
    cout << "Recaudacion total:  $ " << recaudTotal << endl;

    // en esta linea comienza la pausa final
    // El menu ya descarto su ENTER (cin.ignore dentro de leerEntero),
    // asi que cin.get() espera de verdad a que se presione ENTER.
    cout << endl << "Presione ENTER para salir...";
    cin.get();

    return 0;
}
