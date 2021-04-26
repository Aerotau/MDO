def trapezoidal_wing_area(c_r, c_t, b_rect, b_trap):
  """
  Computes the area for a trapezoidal wing
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

if __name__ == "__main__":
  c_r, c_t, b_rect, b_trap = 0.455, 0.455, 2.35, 0
  print("When the inputs are:")
  print(f'c_r = {c_r} \nc_t = {c_t} \nb_rect = {b_rect} \nb_trap = {b_trap}\n')

  b = wingspan(b_rect, b_trap)
  s = wing_area(c_r, c_t, b_rect, b_trap)
  afil = taper_ratio(b_rect, b_trap, c_t, c_r)
  ar = aspect_ratio(b, s)

  results = {
    "Area": s,
    "Taper ratio": afil,
    "Wingspan": b,
    "Aspect ratio": ar,
  }
  print("The results are:")
  for key, value in results.items():
      print(f'{key} = {value}')