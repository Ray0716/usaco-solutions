def spray(grass, intensity, times):
    result = grass
    if intensity > 0:
        for x in range(times):
            #print(x)
            thisIntensity = intensity
            for index in range(len(grass)-1, (len(grass) - thisIntensity - 1), -1):
                #print(index)
                result[index] += thisIntensity
                thisIntensity -= 1
        return result
    else: # negative intensity
        for x in range(times):
            thisIntensity = intensity
            for index in range(len(grass)-1, (len(grass) - abs(thisIntensity) - 1), -1):
                result[index] += thisIntensity
                thisIntensity += 1
        return result

    

print(spray([0, 0, -7, -14, -4], 3, 7))