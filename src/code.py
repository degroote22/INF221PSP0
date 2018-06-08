#
def impedido(filename):
  file = open(filename, "r")
  res = ""

  while(True):
    firstLine = file.readline()
    try:
      [numAtac, numDef] = map(int, firstLine.split(' '))
    except ValueError:
      print "O numero de atacentes ou numero de defensores esta fora do padrao (numeros inteiros)"
      raise ValueError

    if(numAtac == 0 and numDef == 0):
      return res

    atacLine = file.readline()
    defLine = file.readline()

    try:
      atacs = map(int, atacLine.split(" "))
    except ValueError:
      print "A posicao de algum atacante esta fora do padrao (numeros inteiros)"
      raise ValueError
    
    try:
      defs = map(int, defLine.split(" "))  
    except ValueError:
      print "A posicao de algum defensor esta fora do padrao (numeros inteiros)"
      raise ValueError
    defs.sort()
    penultimo = defs[1]
    toAdd = "N"
    for atacante in atacs:
      if (atacante < penultimo):
        toAdd = "Y"
    res = res + toAdd + "\n"
    
  return res