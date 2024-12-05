# Part 1 solution
def process_input(data):
    def is_safe(array):
        orderIsAscending = array[0] < array[1]

        if orderIsAscending:
            for i in range(1, len(array)):
                diff = array[i] - array[i - 1]
                if not 1 <= diff <= 3:
                    return False
            return True
        else:
            for i in range(1, len(array)):
                diff = array[i] - array[i - 1]
                if not -3 <= diff <= -1:
                    return False
            return True

    safe_reports = 0
    for line in data:
        array = [int(x) for x in line.split()]
        if is_safe(array):
            safe_reports += 1

    print(safe_reports)
