import clienteClassic
import clienteGold
import clienteBlack
from creadorHTML import generate_html

try:
    cliente_Classic = clienteClassic.Classic()
    cliente_Gold = clienteGold.Gold()
    cliente_Black = clienteBlack.Black()
except FileNotFoundError:
    print("Alguno de los archivos Clasic,Gold o Black no existe")
    exit()
generate_html(cliente_Classic, cliente_Gold, cliente_Black)