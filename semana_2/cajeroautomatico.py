class cajero:
  nombre="*At&t"
  teclas="*20 teclas"
  tarjetas="*devito y credito"
  horarios="*24 horas"
  lugar="*floresta"
  direccion="*centro"
  cubiculos="*1 para persona sola"
  pnatalla="*tactil"
  red_bancaria="*At&t"
  tramites="*consulta de saldos"
  def retirar (sel):
    print("Retirar")
  def depositar (sel):
    print("Depositar")
  def transferir (sel):
    print("Transferir")
  def abonar (sel):
    print("Abonar")
  def pagar_servicios_(sel):
    print("Pagar servicios ")
caj=cajero()
print(caj.nombre)
print(caj.teclas)
print(caj.tarjetas)
print(caj.horarios)
print(caj.lugar)
print(caj.direccion)
print(caj.cubiculos)
print(caj.pnatalla)
print(caj.red_bancaria)
print(caj.tramites)
caj.retirar()
caj.depositar()
caj.transferir()
caj.abonar()
caj.pagar_servicios_()