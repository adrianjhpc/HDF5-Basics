import h5py


f = h5py.File('example.h5')
dataset = f['dset']
for i in range(6):
    print('%0d: %s' % (i, ','.join(map(str, dataset[i][:]))))

print(dataset[1, 5])
print(dataset[1, 5:11:2])
print(dataset[..., 3])
print(dataset[4, ...])

group = f.create_group("Earthquake")
laq = group.create_group("/Earthquake/Laquila")
laq.create_group("Visualisation")
laq.create_group("Traces")
group.create_group("Christchurch")

dataset = laq.create_dataset("day1", (5, 10), dtype='i')

value = "Amy Krause"
attr = f.attrs.create('author', value)
print(f.attrs.get('author'))

f.move("dset", "Earthquake/Laquila/Traces/dset")
print(group.keys())

group = f['Earthquake/Laquila/Traces/']
group.move("dset", "day2")
print(group.keys())


def print_name(name):
    print(name)

group.visit(print_name)

dataset = f['Earthquake/day2']
dataset[1:3, 2:5] = [[0,0,0], [0,0,0]]
print(dataset[:,:])
print(dataset[0, [1,3,8]])
dataset[0, [1,3,8]] = [9,9,9]
print(dataset[0, [1,3,8]])
