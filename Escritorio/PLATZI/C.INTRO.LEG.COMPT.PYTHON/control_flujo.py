def busca_pais(paises,  pais):
    """
    Paises es un diccionario. Pais es la llave
    Codigo con el principio EAFP.
    """
    
    try:
        return paises[pais]
    except KeyError:
        return None
    
    
    
#Javascript

#
#
#/** Paisese es un objeto.Pais es la llave 
# *Codigo con el principio LBYL.
#/
# Function buscaPais(Paises,pais){
#   if(!object.keys(paises).includes(pais)){
#     return null;   
#    }
#   return paises[pais];
#
#   }
#
#
#