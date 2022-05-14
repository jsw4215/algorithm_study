consume = ["public_transport 10000", "public_transport 10000", "shopping 377000", "food 16000", "public_transport 2000"]
cards = [["food 5 30000", "convenience_store 20 10000", "public_transport 15 2000"], ["food 5 30000", "shopping 10 15000", "movie 7 5000"]]

function indexOfMax(arr) {
    if (arr.length === 0) {
        return -1;
    }

    var max = arr[0];
    var maxIndex = 0;

    for (var i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            maxIndex = i;
            max = arr[i];
        }
    }

    return maxIndex;
}

function calcCost(card, consume){

    cardInfo = card.map((item)=>{
        return item.split(" ")
    })

    console.log("info", cardInfo)

    res = consume.map((item)=>{

        let buy = item.split(" ")
        let match = cardInfo.filter((cardDetail)=>{
            return cardDetail[0]===buy[0]
        })
        
        if (match.length!==0){
        let discountPricelist = match.map((matchInfo)=>{
            discountPrice = Number(matchInfo[1])/100*Number(buy[1])
            if(discountPrice > matchInfo[2]) {
                
                return matchInfo[2]
            }
            return discountPrice
        })

        discountPrice = Math.max(...discountPricelist)
        console.log("match", match, discountPrice)
        return Math.min(discountPrice, match[0][2])
        }

        return 0
    })
    console.log("res", res)
    return res
}

function solution(consume, cards){
    res = -1
    arr = []
    for(let i =0;i<cards.length;i++){
    
        temp = calcCost(cards[i], consume)
        arr.push(temp)
    }

    res = indexOfMax(arr)

    if(res===-1){
        return res
    }else{
        return res+1
    }

}


console.log(solution(consume, cards))