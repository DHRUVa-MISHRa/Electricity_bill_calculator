# Electricity bill calculator
cn=input("enter customer name:")
con=int(input("enter connection no.: "))
print("choose connection type:\n1. Domestic \n2.commercial")
ct=input("write connection type:")
pr=int(input("previous reading:"))
cr=int(input("current reading:"))
tu=cr-pr
if(ct=="Domestic"):
    puc=8
if(ct=="Commercail"):
    puc=14
tb=puc*tu
gst=tb*18/100
nb=tb+gst
print("\n\n\n")
print("\t\t-----------------Electicity Bill---------------")
print("\t\tCustomer Name:",cn)
print("\t\tConnection no.:",con)
print("\t\tConnection Type:",ct)
print("\t\tPrevious Reading:",pr)
print("\t\tCurrent Reading:",cr)
print("\t\t--------------------------------")
print("\t\tTotal unit:",tu)
print("\t\tPer unit Charge:",puc)
print("\t\tTotal Bill:",tb,"Rs.")
print("\t\tGST @18%:",gst)
print("\t\tNet Bill:",nb,"Rs.")
print("\t\t--------------------------------")


