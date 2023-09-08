def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveryBox = 0
    pickupBox = 0
    for i in range(len(deliveries)-1,-1,-1) :
        count = 0
        while deliveries[i] > deliveryBox or pickups[i] > pickupBox:
            deliveryBox += cap
            pickupBox += cap
            count += 1
        answer += (i+1)*2*count
        deliveryBox -= deliveries[i]
        pickupBox -= pickups[i]
    
    return answer