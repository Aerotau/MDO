def wing_area(c_r, c_t, b_rect, b_trap):
  """
  >>> wing_area(2,2,4,5)
  18.0
  """
  S = c_r * b_rect + (c_r + c_t) * b_trap/2
  return S

def taper_ratio(b_rect, b_trap, c_t, c_r):
  """
  >>> taper_ratio(4,2,2,1)
  1.5
  """
  
  if(b_rect>0 and b_trap >0):
    afil = (1 + c_t / c_r)/2 #entender
  else:
    afil = c_t / c_r
  return afil

def wingspan(b_rect, b_trap):
  """
  >>> wingspan(2,4)
  6
  """

  b = b_rect + b_trap
  return b

def aspect_ratio(b, S):
  """
  >>> aspect_ratio (2,4)
  1.0
  """

  return b**2 / S

def calculo_da_asa(c_r, c_t, b_rect, b_trap):
  b = wingspan(b_rect, b_trap)
  S = wing_area(c_r, c_t, b_rect, b_trap)
  afil = taper_ratio(b_rect, b_trap, c_t, c_r)
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