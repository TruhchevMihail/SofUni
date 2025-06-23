import collections

def main():
    drones = {
        100: "Sentinel-X",
        85: "Viper-MKII",
        75: "Aegis-7",
        65: "Striker-R",
        55: "Titan-Core"
    }
    sorted_requirements = sorted(drones.keys(), reverse=True)
    
    mech_parts = list(map(int, input().split()))
    power_cells = collections.deque(map(int, input().split()))
    
    assembled_drones = []
    built_drones = set()
    
    while mech_parts and power_cells and len(assembled_drones) < 5:
        part = mech_parts.pop()
        cell = power_cells.popleft()
        total = part + cell
        
        if total in drones and drones[total] not in built_drones:
            drone_name = drones[total]
            assembled_drones.append(drone_name)
            built_drones.add(drone_name)
        else:
            candidate = None
            for req in sorted_requirements:
                if req <= total and drones[req] not in built_drones:
                    candidate = req
                    break
                    
            if candidate is not None:
                drone_name = drones[candidate]
                assembled_drones.append(drone_name)
                built_drones.add(drone_name)
                new_energy = cell - 30
                if new_energy > 0:
                    power_cells.append(new_energy)
            else:
                new_energy = cell - 1
                if new_energy > 0:
                    power_cells.append(new_energy)
    
    if len(assembled_drones) == 5:
        print("Mission Accomplished! All Guardian Drones activated!")
    else:
        print("Mission Failed! Some drones were not built.")
        
    if assembled_drones:
        print(f"Assembled Drones: {', '.join(assembled_drones)}")
    
    if mech_parts:
        mech_remaining = list(reversed(mech_parts))
        print(f"Mechanical Parts: {', '.join(map(str, mech_remaining))}")
    
    if power_cells:
        power_list = list(power_cells)
        print(f"Power Cells: {', '.join(map(str, power_list))}")


main()