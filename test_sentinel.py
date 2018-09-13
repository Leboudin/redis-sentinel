from redis.sentinel import Sentinel


if __name__ == '__main__':
    sentinel = Sentinel(
        [('119.23.146.211', 26379),
         ('120.79.129.231', 26379),
         ('176.122.188.100', 26379)],
        socket_timeout=0.1
    )

    print(sentinel.discover_master('mymaster'))
    print(sentinel.discover_slaves('mymaster'))

    master = sentinel.master_for('mymaster', socket_timeout=0.5)
    slave = sentinel.slave_for('mymaster', socket_timeout=0.5)

    print(master.set('test2', 'redis-py sentinel'))
    try:
        print(slave.get('test2'))
    except Exception as e:
        print(slave)
        print(e)
        pass


    # print(slave.get('test2'))
