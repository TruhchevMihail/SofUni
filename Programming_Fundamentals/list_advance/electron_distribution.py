def electron_distribution(electrons):
    shells = []
    n = 1
    while electrons > 0:
        max_electrons_in_shell = 2 * n ** 2
        if electrons >= max_electrons_in_shell:
            shells.append(max_electrons_in_shell)
            electrons -= max_electrons_in_shell
        else:
            shells.append(electrons)
            electrons = 0
        n += 1
    return shells

electrons = int(input())
print(electron_distribution(electrons))