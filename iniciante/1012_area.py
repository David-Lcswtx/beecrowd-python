import math

pi = 3.14159

entrada = input().split()

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

areaTriangulo = (a * c) / 2
areaCirculo = pi * math.pow(c, 2)
areaTrapezio = ((a + b) * c) / 2
areaQuadrado = math.pow(b, 2)
areaRetangulo = a * b

print(f"TRIANGULO: {areaTriangulo:.3f}")
print(f"CIRCULO: {areaCirculo:.3f}")
print(f"TRAPEZIO: {areaTrapezio:.3f}")
print(f"QUADRADO: {areaQuadrado:.3f}")
print(f"RETANGULO: {areaRetangulo:.3f}")
