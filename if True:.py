def tri(a):
  for i in range(a):
    x='*'
    x=x*(500-i)
    print(f'{x:<10}')
  return x
p=tri(500)
print(p)

  