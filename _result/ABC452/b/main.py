height, width = map(int, input().split())

conma_width = width - 2
for i in range(height):
    if i == 0 or i == height - 1:
        print("#" * width)
    else:
        print("#", "." * conma_width, "#", sep="")
