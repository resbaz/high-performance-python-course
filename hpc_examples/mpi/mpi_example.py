import random
from mpi4py import MPI


def monte_carlo_pi_part(n):
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()

        if x * x + y * y <= 1:
            count += 1
    return count


def master():
    points_per_node = int(n / (size - 1))

    for worker in range(1, size):
        comm.send(points_per_node, dest=worker)

    received_processes = 0
    count = 0

    # Await results
    while received_processes < (size - 1):
        count += comm.recv(source=MPI.ANY_SOURCE)
        received_processes += 1

    print('Estimated value of Pi: %f ' % (count / (n * 1.0) * 4))


def slave():
    points_to_calculate = comm.recv(source=0)
    count = monte_carlo_pi_part(points_to_calculate)
    comm.send(count, dest=0)


# Who am I?
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Number of points to simulate (10 million)
n = 10000000

print('My rank: %d' % rank)

if rank == 0:
    # I'm the master, tell other nodes to do.
    print('Simulate %d million points across %d workers' % (n / 1e6, size))
    master()
else:
    # I'm the slave... await instructions then shutdown.
    slave()