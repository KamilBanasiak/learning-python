def square_root_bisection(number, tolerance=1e-7, max_iterations=20):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number
    elif number > 0 and number < 1:
        low = number
        high = 1
        iterations = max_iterations
        while low <= high and iterations != 0:
            mid = (low + high) / 2
            quadrat_mid = mid ** 2
            if high - low <= tolerance:
                print(f'The square root of {number} is approximately {mid}')
                return mid
            elif quadrat_mid - number < 0:
                low = mid
            else:
                high = mid
            iterations -= 1
    else:
        low = 0
        high = number
        iterations = max_iterations
        while low <= high and iterations != 0:
            mid = (low + high) / 2
            quadrat_mid = mid ** 2
            print(quadrat_mid - number)
            if abs (quadrat_mid - number) <= tolerance:
                print(f'The square root of {number} is approximately {mid}')
                return mid
            elif quadrat_mid - number < 0:
                low = mid
            else:
                high = mid
            iterations -= 1
    print(f'Failed to converge within {max_iterations} iterations')
    return None