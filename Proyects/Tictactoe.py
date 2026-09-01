print("""
████████╗██╗ ██████╗████████╗ █████╗  ██████╗████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔════╝
   ██║   ██║██║        ██║   ███████║██║        ██║   ██║   ██║█████╗
   ██║   ██║██║        ██║   ██╔══██║██║        ██║   ██║   ██║██╔══╝
   ██║   ██║╚██████╗   ██║   ██║  ██║╚██████╗   ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝
""")
# Si no tiene la funcion int() no podra funcionar ya que mas abajo pide que sea igual a un numero pero si lo dejamos sin el int() la variable seria "1" en texto no como un numero entero.
user_answer = int(
    input("Would you like to play the game?\n1.Yes\n2. No\nSelect one option (1-2):")
)

if user_answer == 1:
    print("Starting...")
elif user_answer == 2:
    print("Bye..")
