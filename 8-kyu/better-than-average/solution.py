def better_than_average(class_points, your_points):
    average_points = sum(class_points)/len(class_points)
    if your_points > average_points:
        return True
    else:
        return False
