import numpy as np
import h5py

def convertir_a_hd5(nombre_txt, nombre_hd5):
    datos = np.loadtxt(nombre_txt)

    if datos.ndim == 1:
        datos = datos.reshape(1, -1)

    # EXISTEN 3??
    if datos.shape[1] != 3:
        raise ValueError("el archivo debe contener exactamente tres columnas.")

    with h5py.File(nombre_hd5, "w") as archivo:
        archivo.create_dataset("propiedad_1", data=datos[:, 0])
        archivo.create_dataset("propiedad_2", data=datos[:, 1])
        archivo.create_dataset("propiedad_3", data=datos[:, 2])

    print(f"archivo creado correctamente: {nombre_hd5}")

convertir_a_hd5("simulacion.txt", "simulacion.hd5")
with h5py.File("simulacion.hd5", "r") as archivo:
    print(list(archivo.keys()))
    print(archivo["propiedad_1"][:])
    print(archivo["propiedad_2"][:])
    print(archivo["propiedad_3"][:])