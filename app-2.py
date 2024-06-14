import math

# 1. Noktaların tanımlanması
points = [
    (1, 2),
    (4, 6),
    (5, 5),
    (3, 3)
]

# 2. Öklid mesafesi için bir fonksiyon yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 3. Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Minimum mesafenin bulunması
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)
