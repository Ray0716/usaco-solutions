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


n = int(input())
bacteriaLevels = [int(x) for x in input().split()]
sprayCount = 0

for grassIndex in range(len(bacteriaLevels)):
    if bacteriaLevels[grassIndex] > 0:
        #print(bacteriaLevels, -(len(bacteriaLevels) - grassIndex), abs(bacteriaLevels[grassIndex]))
        sprayCount += abs(bacteriaLevels[grassIndex])
        bacteriaLevels = spray(bacteriaLevels, -(len(bacteriaLevels) - grassIndex), abs(bacteriaLevels[grassIndex]))
        
    elif bacteriaLevels[grassIndex] < 0:
        #print(bacteriaLevels, (len(bacteriaLevels) - grassIndex), abs(bacteriaLevels[grassIndex]))
        #prayCount += bacteriaLevels[grassIndex]
        sprayCount += abs(bacteriaLevels[grassIndex])
        bacteriaLevels = spray(bacteriaLevels, (len(bacteriaLevels) - grassIndex), abs(bacteriaLevels[grassIndex]))
        

print(sprayCount)