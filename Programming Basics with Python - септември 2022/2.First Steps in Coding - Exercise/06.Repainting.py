needed_nylon = int(input()) + 2
needed_pait = int(input()) * 1.1
needed_solvent = int(input())
total_work_hours = int(input())


nylon_price = 1.50 * needed_nylon
paint_price = 14.50 * needed_pait
solvent = 5.00 * needed_solvent
packets = 0.40
work_price = total_work_hours * 0.3 * (nylon_price + paint_price + solvent + packets)

total_price = work_price + nylon_price + paint_price + solvent + packets
print(total_price)
