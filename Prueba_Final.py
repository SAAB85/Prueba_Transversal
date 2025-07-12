productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
    }

stock = {
    '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
    }

def menu():
    while True:
        print("***MENU PRINCIPAL***")
        print("1.►Stock por marca")
        print("2.►Buscar por rango de precios")
        print("3.►Actualizar precios")
        print("4.►Salir")
        opcion=input("Ingrese una opcion (1-4): ")
        
        if opcion =='1':
            marca=input("Ingrese marca: ")
            stock_marca(marca)
        
        elif opcion=='2':
            try:
                p_min=int(input("Ingrese el precio minimo: "))
                p_max=int(input("Ingrese el precio maximo: "))
                buscar_por_precio(p_min,p_max)
            except ValueError:
                print("Porfavor ingrese un valor correcto")
        
        elif opcion=='3':
            modelo=input("Ingrese modelo a actualizar: ").strip().upper()
            try:
                nuevo_precio=int(input("Ingrese precio nuevo: "))
            except ValueError:
             print("Ingrese un precio valido!!!")
             continue
            
            if actualizar_precio(modelo, nuevo_precio):
                print("Precio actualizado")
            else:
                print("El modelo no existe!!")
            
            otro=input("¿Debe actualizar otro precio(s/n)?: ").strip().lower()
            if otro !='s':
               break
        elif opcion=='4':
            print("Programa finalizado")
            break
        else:
            print("Porfavor ingrese una opcion valida (1-4)")
        

def stock_marca(marca):
    total=0
    for modelo,datos in productos.items():
        if datos[0].lower()== marca.lower():
            total+= stock.get(modelo,[0,0])[1]
    print(f"El stock es:{total}")

def buscar_por_precio(p_min,p_max):
    disponibles=[]
    for modelo, (precio, cantidad) in stock.items():
        if p_min <=precio <=p_max and cantidad >0:
            marca=productos[modelo][0]
            disponibles.append(f"{marca}--{modelo}")
    if disponibles:
        disponibles.sort()
        print(f"Computadores disponibles:{disponibles}")
    else:
        print("No hay computadores disponibles en este rango de precio")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0]=nuevo_precio
        return True
    return False
menu()