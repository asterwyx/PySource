import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())
print(psutil.cpu_times_percent())
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))
print(psutil.virtual_memory())
print(psutil.swap_memory())
print(psutil.disk_partitions())  # 磁盘分区信息
print(psutil.disk_usage('/'))  # 磁盘使用情况
print(psutil.disk_io_counters())  # 磁盘IO
print(psutil.net_io_counters())
print(psutil.net_if_addrs())
print(psutil.net_if_stats())
print(psutil.net_connections())
print(psutil.pids())
p = psutil.Process(1080)
print(p.name())
# print(p.cmdline())
print(p.parent())
print(p.ppid())
print(p.parent().pid)
print(p.parent().name())
print(p.parents())
print(p.children())
print(p.status())
print(p.create_time())
# 因为这个进程刚好是系统进程，所以诸如username(), exe(), cwd(), cmdline()等都是拒绝访问的
# 这个进程没有p.terminal()
print(p.cpu_times())
print(p.memory_info())
# print(p.open_files())
print(p.connections())
print(p.num_threads())
print(p.threads())
# print(p.environ())
print(psutil.Process())  # 不写参数会返回Python的进程id
