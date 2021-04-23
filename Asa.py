def area_da_asa(c_r, c_t, b_ret, b_trap):
  return c_r * b_ret + (c_r + c_t) * b_trap/2

def afilamento(b_ret, b_trap, c_t, c_r):
  afil = 0
  if(b_ret>0 and b_trap >0):
    afil = (1 + c_t / c_r)/2
  else:
    afil = c_t / c_r
  return afil

def calculo_da_asa(c_r, c_t, b_ret, b_trap):
  resultados = {
    "area_da_asa": area_da_asa(c_r, c_t, b_ret, b_trap),
    "afilamento": afilamento(b_ret, b_trap, c_t, c_r)
  }
  return resultados

resultado = calculo_da_asa(0.455, 0.455, 2.35, 0)
area_da_asa = resultado["area_da_asa"]

print(f'A area da asa e: {area_da_asa}')