import pyjokes # importar la libreria, hay que instalarla con el comando pip install pyjokes

# generar la broma
broma = pyjokes.get_joke(language='es')



print(f"Aqui tienes una broma de programacion:  {broma}")