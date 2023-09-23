#include <stdio.h>
//Tarea de programacion I de python convertida en C ya que estaba aprendiendo a usar C por cuenta propia

void Imprimir(int limit,int edad[limit],int cedula[limit]){
  printf("-------Imprimiendo lista-------\n");
  
  int sCont = 1;
  for(int cont = 0;cont<limit;cont++){
  printf("\tEdad %d: %d\n",sCont,edad[cont]);
  printf("\tCedula %d: %d\n",sCont,cedula[cont]);
  sCont++;
  }
}

void OrdenarCedula(int limit,int edad[limit],int cedula[limit]){
  int est = 1, opc, cont1, cont2,temp1,temp2;
  while(est != 0 ){
    printf("1. Ordenar mayor a menor\n");
    printf("2. Ordenar menor a mayor\n");
    printf("3. Ingrese seleccion: ");
    scanf("%d",&opc);
    if(opc == 1){
      cont1 = 0;
      while(cont1 < limit-1){
        cont2 = cont1 + 1;
        while(cont2 < limit){
        if(cedula[cont1] < cedula[cont2]){
          temp1 = cedula[cont1];
          temp2 = edad[cont1];
          cedula[cont1] = cedula[cont2];
          edad[cont1] = edad[cont2];
          cedula[cont2] = temp1;
          edad[cont2] = temp2;
          }
        cont2 = cont2 + 1;
        }
      cont1 = cont1 + 1;
      }
    est = 0;
    }
    else if(opc == 2){
      cont1 = 0;
      while(cont1 < limit-1){
        cont2 = cont1 + 1;
        while(cont2 < limit){
        if(cedula[cont1] > cedula[cont2]){
          temp1 = cedula[cont1];
          temp2 = edad[cont1];
          cedula[cont1] = cedula[cont2];
          edad[cont1] = edad[cont2];
          cedula[cont2] = temp1;
          edad[cont2] = temp2;
          }
        cont2 = cont2 + 1;
        }
      cont1 = cont1 + 1;
      }
    est = 0;
    }
    else{
      printf("Dato invalido\n");
    }
  }
}

void OrdenarEdad(int limit,int edad[limit],int cedula[limit]){
 int est = 1, opc, cont1, cont2,temp1,temp2;
  while(est != 0 ){
    printf("1. Ordenar mayor a menor\n");
    printf("2. Ordenar menor a mayor\n");
    printf("3. Ingrese seleccion: ");
    scanf("%d",&opc);
    if(opc == 1){
      cont1 = 0;
      while(cont1 < limit-1){
        cont2 = cont1 + 1;
        while(cont2 < limit){
        if(edad[cont1] < edad[cont2]){
          temp1 = cedula[cont1];
          temp2 = edad[cont1];
          cedula[cont1] = cedula[cont2];
          edad[cont1] = edad[cont2];
          cedula[cont2] = temp1;
          edad[cont2] = temp2;
          }
        cont2 = cont2 + 1;
        }
      cont1 = cont1 + 1;
      }
    est = 0;
    }
    else if(opc == 2){
      cont1 = 0;
      while(cont1 < limit-1){
        cont2 = cont1 + 1;
        while(cont2 < limit){
        if(edad[cont1] > edad[cont2]){
          temp1 = cedula[cont1];
          temp2 = edad[cont1];
          cedula[cont1] = cedula[cont2];
          edad[cont1] = edad[cont2];
          cedula[cont2] = temp1;
          edad[cont2] = temp2;
          }
        cont2 = cont2 + 1;
        }
      cont1 = cont1 + 1;
      }
    est = 0;
    }
    else{
      printf("Dato invalido\n");
    }
  }
}

void Menu(int limit,int edad[limit],int cedula[limit]){
  int est = 1,opc;
  while(est != 0){
    printf("-------Menu-------\n");
    printf("1. Ordernar por Edad\n");
    printf("2. Ordernar por Cedula\n");
    printf("3. Imprimir\n");\
    printf("4. Salida\n");
    printf("Ingresar seleccion: ");
    scanf("%d",&opc);
    if(opc == 1){
      //Ordenar Edad
      OrdenarEdad(limit,edad,cedula);
    }
    else if(opc == 2){
      //Ordenar Cedula
      OrdenarCedula(limit,edad,cedula);
    }
    else if(opc == 3){
      //Imprimir
      Imprimir(limit,edad,cedula);
    }
    else if(opc == 4){
      exit(0);
    }
    else{
      printf("Dato invalido");
    }
    
  }
  
}

void Inicio(){
  int limit,sCont;
  printf("Ingrese la cantidad de los datos: ");
  scanf("%d",&limit);
  int edad[limit], cedula[limit];

  sCont = 1;
  for(int cont = 0; cont<limit;cont++){
    printf("Ingrese la edad %d :",sCont);
    scanf("%d",&edad[cont]);
    printf("Ingrese la cedula %d :",sCont);
    scanf("%d",&cedula[cont]);
    sCont++;
  }  
  Menu(limit,edad,cedula);
}



int main(void) {
  Inicio();
    
  return 0;
}
