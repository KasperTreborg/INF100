import data_normalization

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Normalizing the data to [0, 1] range
a = data_normalization.norm_0_1(data)

# Normalizing the data to [-1, 1] range
b = data_normalization.norm_neg1_1(data)

assert a == [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0]

assert b == [-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0]