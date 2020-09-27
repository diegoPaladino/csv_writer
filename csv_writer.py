#csv_writer
#UNSUCESSFUL - but was sucessful in the Jupyter notebook ()

#libraries
import csv
import investpy as inv


#declarations


#execution
lista = inv.get_stocks('brazil')

# with open('arquivos/saida.csv','w',newline='') as f:
#     thewriter = csv.writer(f)

#     thewriter.writerow(lista)

lista.to_excel('lista.xlsx',encoding='utf-8',index=False)
