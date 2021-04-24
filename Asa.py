def area_da_asa(c_r, c_t, b_ret, b_trap):
  S = c_r * b_ret + (c_r + c_t) * b_trap/2
  return S

def afilamento(b_ret, b_trap, c_t, c_r):
  afil = 0
  if(b_ret>0 and b_trap >0):
    afil = (1 + c_t / c_r)/2
  else:
    afil = c_t / c_r
  return afil

def envergadura (b_ret, b_trap):
  b = b_ret + b_trap
  return b

def aspect_ratio(b, S):
  return b**2 / S

def calculo_da_asa(c_r, c_t, b_ret, b_trap):
  b = envergadura(b_ret, b_trap)
  S = area_da_asa(c_r, c_t, b_ret, b_trap)
  afil = afilamento(b_ret, b_trap, c_t, c_r)
  AR = aspect_ratio(b, S)

  resultados = {
    "area da asa": S,
    "afilamento": afil,
    "envergadura": b,
    "AR": AR,
  }
  return resultados

resultado = calculo_da_asa(0.455, 0.455, 2.35, 0)
area_da_asa = resultado["area da asa"]
afilamento = resultado["afilamento"]
envergadura = resultado["envergadura"]
AR = resultado["AR"]

print(f'A area da asa e: {area_da_asa}')
print(f'O afilamento e: {afilamento}')
print(f'A envergadura e: {envergadura}')
print(f'O AR e: {AR}')